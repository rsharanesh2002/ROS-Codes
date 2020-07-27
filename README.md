# ROS-Codes

This codes are written with ros noetic. There are two options of having ROS noetic on your machine. You can either download ROS from the official page on your local machine, or pull the docker image. 

To run these codes first you need to pull the docker image of ros/noetic
```
docker pull osrf/ros:noetic-desktop-full # Pull the latest version of ROS Noetic
```

After pulling the docker image run the docker image in your terminal with the following command
```
xhost +
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY osrf/ros:noetic-desktop-full
```
This command will open up the docker image and run it in interactive mode and also allows you to have external displays

