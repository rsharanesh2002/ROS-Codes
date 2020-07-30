FROM osrf/ros:noetic-desktop-full
LABEL description=" This docker image for making star in turtlesim"

SHELL ["/bin/bash","-c"]

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y \
    iputils-ping \
    wget \
    ros-noetic-turtlesim \
    python3

ENV CATKIN_WS = /root/catkin_ws
RUN mkdir -p ~/catkin_ws/src
WORKDIR $CATKIN_WS/src

RUN source /opt/ros/${ROS_DISTRO}/setup.bash \
    && apt-get update \
    && cd ~/catkin_ws \
    #&& rosdep install -y --from-paths . --ignore-src --rosdistro ${ROS_DISTRO} \
    && catkin_make \
    && source ~/catkin_ws/devel/setup.bash \
    && cd ~/catkin_ws/src \
    && catkin_create_pkg my_turtle rospy std_msgs turtlesim \
    && cd my_turtle \
    && mkdir scripts \
    && cd scripts \
    && wget -O making_star.py https://raw.githubusercontent.com/rsharanesh-iitm/ROS-Codes/master/making_star.py \
    && chmod +x * \
    && cd .. \
    && rm CMakeLists.txt \
    && wget -O CMakeLists.txt https://raw.githubusercontent.com/rsharanesh-iitm/ROS-Codes/master/CMakeLists.txt \
    && cd ~/catkin_ws \
    && catkin_make
