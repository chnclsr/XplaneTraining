------------
#### Example folder
---------------
Sample example for using the gym_xplane environment.

-----------------
##### Usage
--------------------

1. Copy Dockerfile and its sh to near XPlane 11 folder

Sadece bir defa başlangıçta çalıştır.
```
sudo nvidia-xconfig -a --allow-empty-initial-configuration --use-display-device=None --virtual=1920x1200 --busid {busid}
```

```
docker build -t xplane_gpu .
xhost +local:docker
docker run --network host --privileged --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -di xplane_gpu
```

İlk kurulumda lisans aktifleştirme için gerekli
```
docker exec -it xp11_ins_1 bash
env VGL_DISPLAY=$DISPLAY vglrun XPlane11/run --no_sound
```


