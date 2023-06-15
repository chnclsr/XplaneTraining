import time
from ray.tune.registry import register_env
import ray
import ray.rllib.agents.ppo as ppo
from gym_xplane.gym_xplane.envs.xplane_envBase import XplaneEnv
import gym_xplane
from ray import tune
from ray.rllib.agents.ppo.ppo import DEFAULT_CONFIG, PPOTrainer

# def start_xplane(start):
#     if start:
#         import os
#         import subprocess
#         from time import sleep
#         print("X-Plane is starting...")
#         current_path = os.getcwd()
#         xplane_path = os.environ["XPLANE_11_PATH"]
#         os.chdir(xplane_path)
#         cmd = "X-Plane.exe"
#         proc = subprocess.Popen(cmd, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         sleep(2)
#         proc.kill()
#         os.chdir(current_path)
#         print("X-Plane started")
#         print("waiting 60 secs for loading..")
#         sleep(60)
#         print("X-Plane loaded!")

def main ():
    import subprocess
    from subprocess import PIPE
    # # init directory in which to save checkpoints
    chkpt_root = ""
    # shutil.rmtree(chkpt_root, ignore_errors=True, onerror=None)
    #
    # # init directory in which to log results
    # ray_results = "{}/ray_results/".format(os.getenv("HOME"))
    # shutil.rmtree(ray_results, ignore_errors=True, onerror=None)
    #
    # subprocess.run(['ray', 'start', '--head', '--node-ip-address', 'gymxplane_ry'])

    # print("starting head node")
    # time.sleep(10)
    ray.init(address='ray://10.0.135.54:10001')

    trainingID = "3instances_roll_control"
    #register_env(select_env, lambda config: Fail_v1())
    n_gpus = int(ray.cluster_resources().get("GPU", 0))
    n_cpus = int(ray.cluster_resources().get("CPU", 0))
    print(n_cpus, n_gpus)

    # configure the environment and create agent
    config_t = ppo.DEFAULT_CONFIG.copy()
    config_t["log_level"] = "WARN"
    config_t["kl_coeff"] = 0
    config_t["kl_target"] = 0
    config_t['num_gpus'] = 0
    config_t['num_workers'] = 3
    config_t['framework'] = 'torch'
    config_t['num_gpus_per_worker'] = 0.1 #don't use GPU
    config_t['num_cpus_per_worker'] = 1
    config_t["train_batch_size"] = 2100 # for PPO
    config_t["rollout_fragment_length"] = 700
    # config_t["sgd_minibatch_size"] = 128
    config_t["num_sgd_iter"] = 10
    # config_t["record_env"] = False
    config_t["remote_worker_envs"] = False
    config_t["model"] = {"fcnet_activation":"tanh"}
    config_t['env_config'] = {"closeHRLimit": config_t["rollout_fragment_length"]}

    # config_t['local-mode'] = False


    # TRAIN

    tune_s = True
    if tune_s:
        from ray.rllib.agents.ppo.ppo import DEFAULT_CONFIG, PPOTrainer
        status = "{:2d} reward {:6.2f}/{:6.2f}/{:6.2f} len {:4.2f}"
        # register the custom environment
        select_env = "gymXplane-v2"
        # start_xplane("start")
        register_env(select_env, lambda config: XplaneEnv(config))
        config_t["env"] = select_env
        trainer = PPOTrainer(config_t, select_env)
        time.sleep(10)
        for i, w in enumerate(trainer.workers._remote_workers):
            w_ip = ray.get(w.get_node_ip.remote())
            print(w_ip)


        # time.sleep(50)
        # trainer = DDPPOTrainer(trainer_config, SimpleCorridor)
        for i in range(5000):
            print("Training iteration {}...".format(i))
            result = trainer.train()
            print(status.format(
                i + 1,
                result["episode_reward_min"],
                result["episode_reward_mean"],
                result["episode_reward_max"],
                result["episode_len_mean"]
            ))
    else:
        from ray import tune
        select_env = "gymXplane-v2"
        # select_env = "fail-v1"
        register_env(select_env, lambda config: XplaneEnv())
        config_t["env"] = select_env
        # trainer_config["env"] = "CartPole-v0"
        # trainer_config['env'] = "BipedalWalker-v2"
        # tune.run("DDPPO", config=config, local_dir="Xplane-ray")
        # configure how checkpoints are sync'd to the scheduler/sampler
        # sync_config = tune.syncConfig()  # the default mode is to use use rsync

        # this starts the run!
        tune.run(
            "PPO",
            config=config_t,
            # a directory where results are stored before being
            # sync'd to head node/cloud storage
            local_dir="/home/pc_3971/Desktop/Cihan/Xplane-ray-0.25",
            #restore="/home/pc_3971/Desktop/Cihan/Xplane-ray-0.25/PPO/deneme/checkpoint_000007",
            checkpoint_freq=20,  # iterations
            checkpoint_at_end=True,
        )

    # # examine the trained policy
    # policy = agent.get_policy()
    # model = policy.model
    # #print(model.base_model.summary())
    #
    #
    # # apply the trained policy in a rollout
    # agent.restore(chkpt_file)
    # env = gym.make(select_env)
    #
    # state = env.reset()
    # sum_reward = 0
    # n_step = 200
    #
    # for step in range(n_step):
    #     action = agent.compute_single_action(state)
    #     state, reward, done, info = env.step(action)
    #     sum_reward += reward
    #
    #     env.render()
    #
    #     if done == 1:
    #         # report at the end of each episode
    #         print("cumulative reward", sum_reward)
    #         state = env.reset()
    #         sum_reward = 0


if __name__ == "__main__":
    main()