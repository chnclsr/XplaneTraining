
# rllib kullanımı

# Gereklilikler
> tensorboard > # pip install tensorflow
> 

#### Eğitimi başlat
Worker sayısına göre istenilen sayıda env aç

```
docker network create xplanet
docker run --network xplanet --shm-size 2gb --ip 172.18.0.2 --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -P -di xplane-image:1
```
"Subnet": "172.18.0.0/16", "Gateway": "172.18.0.1" olduğundan 0.2 ile devam ediyor. Sabit
IP ataması xpc.init()'de XPlaneEnv tarafından her worker için otomatik oluşturuluyor


```
python rllib_xpc.py
```
Grafikler için;
```
tensorboard --logdir=~/ray_results
```


