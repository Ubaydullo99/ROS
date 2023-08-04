# setting up system locale
# ensure environment supports UTF-8
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Adding ros2 repositories
sudo apt update 
sudo apt install curl gnupg2 lsb-release
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add 

sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'


# Installing development and ROS tools
sudo apt update
sudo apt install -y build-essential cmake git python3-colcon-common-extensions python3-lark-parser python3-pip python-rosdep python3-vcstool wget
sudo apt install --no-install-recommends -y libasio-dev libtinyxml2-dev


# Gettings the ROS2 source code
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
wget https://raw.githubusercontent.com/ros2/ros2/release-latest/ros2.repos
vcs import src < ros2.repos

# Innstalling dependencies using rosdep
sudo rosdep init
rosdep update
rosdep install --from-paths src --ignore-src --rosdistro dashing -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 rti-connext-dds-5.3.1 urdfdom_headers"


### DDS ?

# Building code



