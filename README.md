# ROS-Codes

This codes are written with ros noetic. There are two options of having ROS noetic on your machine. You can either download ROS from the official page on your local machine, or pull the docker image. 

## Basic setup
To run these codes first you need to pull the docker image of ros/noetic
```
docker pull osrf/ros:noetic-desktop-full # Pull the latest version of ROS Noetic
```

After pulling the docker image run the docker image in your terminal with the following command
```
xhost +
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY osrf/ros:noetic-desktop-full
```
This command will open up the docker image and run it in interactive mode and also allows you to have external displays.

If you are using ros for the first time, you must source few setup files before getting started with your actual working of the code. To do this you must actually open your `~/.bashrc` file and add the following commands at the last of the `.bashrc` file for sourcing the setup files,
```
nano ~/.bashrc # opens up the .bashrc file

### After opening the file add the following two lines of code at the bottom of the file

source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
```
By doing so, the sourcing will take place automatically every time you run the docker iamge.

## Moving to turtlesim

