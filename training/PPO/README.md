
# rllib kullanımı

# Gereklilikler
> tensorboard > # pip install tensorflow
> 

#### Eğitimi başlat
Worker sayısına göre istenilen sayıda env aç

```
docker network create xplanet
docker tag xplane-image:latest xplane-image:1 # instance No'yu değiştir
docker run --network xplanet --shm-size 2gb --ip 172.18.0.2 --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -P -di xplane-image:1
```

Container ilk kez başlatıldığında;
```
docker exec -it xp11_ins_n bash
#work/$> ps aux
#work/$> kill -9 19 22
#work/$> ./run_vnc.sh
```
VNC Viewer'ı aç;
"172.18.0.2:5901" adresi ile bağlan;

```
#work/$> XPlane11/run --no_sound
```
Lisans key girip aktifleştir. XPlane'i kapat. VNC'yi kapat.

Başka bir terminal açıp;
```
#home$> docker pull xp11_ins_1 xplane-image:1 # Bunu her instance için tekrarla
#home$> docker stop xp11_ins_1 && docker rm xp11_ins_1
#home$> docker run --network xplanet --shm-size 2gb --ip 172.18.0.2 --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -P -di xplane-image:1
```



"Subnet": "172.18.0.0/16", "Gateway": "172.18.0.1" olduğundan 0.2 ile devam ediyor. Sabit
IP ataması xpc.init()'de XPlaneEnv tarafından her worker için otomatik oluşturuluyor

! docker ile GPU'ları kullanabilmek için;

```
# install Nvidia drivers to local
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/#apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```


```
python rllib_xpc.py
```
Grafikler için;
```
tensorboard --logdir=~/ray_results
```


