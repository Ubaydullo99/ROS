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
# In ROS-2, we use an upgraded tool that's an iteration of catkin_make, catkin_make_isolated, catkin_tools, and ament_tools (a build system used in the first ROS-2 distro ardent) called colcon.
# This means that colcon can also build ROS-1 packages and those without manifests alongside ROS-2 packages.
sudo apt install python3-colcon-common-extensions
cd ~/ros2_ws/
colcon build --symlink-install

# issue existed with markupsafe so below only for issue confronts
pip uninstall markupsafe
pip install markupsafe
colcon build --symlink-install
colcon clean
colcon build --symlink-install


# Setting up ros1, ros2 or both environments
# Instead of typing the source command every time, we could make use of the alias command and add them to the bash script using the following steps:
sudo gedit ~/.bashrc # it will opens up bash script

# add these line codes below
alias initros1='source /opt/ros/melodic/setup.bash'
alias initros2='source ~/ros2_ws/install/local_setup.bash'

# delete or commente lines below
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash

# save close bash script
# Now, save and close the bash script. This is to ensure that, when you open your Terminal, neither the ROS-1 or ROS-2 workspace is invoked. Now that these changes have been made to the bash file
source ~/.bashrc


# Running test nodes
initros2 # if it is successful - it show ros_distro was set to melodic before...
ros2 run demo_nodes_cpp talker # outputs the hello world: 8 .. 

# in another terminal , initialize ros2 again using traditional listener node
initros2
ros2 run demo_nodes_py listener
# You should see talker saying that it's Publishing: 'Hello World: 1,2...' and listener saying I heard: [Hello World: <respective count>]



