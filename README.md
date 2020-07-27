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
Further we will be testing our code using the turtlesim node. So, make sure that you have turtlesim package installed in your dccker container.

To install turtlesim use the following command
```
apt-get install ros-noetic-turtlesim
```

Now, we are ready with all the pre-requistes to test our code. Let's get started into building own packages and test our code on turtlesim's turte node.

### Creating your own package
Use the following commands to create your own package,
```
cd ~/catkin_ws

### The following is the general architecture of the catkin_create_pkg
# catkin_create_pkg [package_name] [dependancy1] [dependancy2]

# In our case use,
catkin_create_pkg my_turtle roscpp rospy std_msgs           # to create the package
catkin_make           #to build the package
```

You have successfully created a package and now let's create the script file to make our turtle move and make a star.

### Moving the turlte and making a star
Now enter the following the commands,

```
roscd my_turtle

mkdir scripts
cd scripts
wget -O making_star.py https://raw.githubusercontent.com/rsharanesh-iitm/ROS-Codes/master/making_star.py
chmod +x making_star.py ## making it as executable file
```
Before running our script file, make the following changes in the `CMakelists.txt` file of the `my_turtle` package.

The `CMakelists.txt` file should have the `find_package` function as,
```
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  rospy
  std_msgs
)
```


