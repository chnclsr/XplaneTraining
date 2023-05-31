#! /bin/bash
xvfb-run -a -s "-screen 0 1920x1080x24" env VGL_DISPLAY=$DISPLAY vglrun XPlane11/run --no_sound > /dev/null &
echo "X Plane instances started!"
