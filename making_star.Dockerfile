FROM osrf/ros:noetic-desktop-full
RUN source /opt/ros/noetic/setup.bash

RUN apt-get update && apt-get upgrade
RUN apt-get install -y \
  wget \
  ros-noetic-turtlesim \
  python3 \

RUN mkdir -p ~/catkin_ws/src
RUN cd ~/catkin_ws
RUN catkin_make
RUN source devel/setup.bash

RUN cd ~/catkin_ws/src
RUN create_catkin_pkg my_turtle rospy std_msgs turtlesim
RUN cd my_turtle
RUN mkdir scripts
RUN cd scripts
RUN wget -O making_star.py https://raw.githubusercontent.com/rsharanesh-iitm/ROS-Codes/master/making_star.py
RUN chmod +x *
RUN cd ..
RUN rm CMakeLists.txt
RUN wget -O CMakeLists.txt https://raw.githubusercontent.com/rsharanesh-iitm/ROS-Codes/master/CMakeLists.txt
RUN cd ~/catkin_ws
RUN catkin_make

CMD rosrun my_turtle making_star.py
