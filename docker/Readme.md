------------
#### Example folder
---------------
Sample example for using the gym_xplane environment.

-----------------
##### Usage
--------------------

1. Copy Dockerfile and its sh to near XPlane 11 folder
```
docker build -t xplane_gpu .
xhost +local:docker
docker run --network host --privileged --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -di xplanehost
```
