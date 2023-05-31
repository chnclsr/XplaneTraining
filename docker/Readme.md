------------
#### Example folder
---------------
Sample example for using the gym_xplane environment.

-----------------
##### Usage
--------------------

1. Copy Dockerfile and its sh to near XPlane 11 folder
2. docker build -t xplane_gpu .
4. xhost +local:docker
3. docker run --network host --privileged --gpus all --name xp11_ins_1 -e DISPLAY=$DISPLAY -v /#tmp/.X11-unix:/tmp/.X11-unix -di xplanehost

    ```
