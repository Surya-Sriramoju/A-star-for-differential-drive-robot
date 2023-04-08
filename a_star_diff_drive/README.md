# A-Star-for differential-drive-robot

Dependencies required:
* Ubuntu 20.04
* Gazebo
* ROS Noetic
* turtlebot3 packages
* Python packages: Numpy, opencv, queue, time

libraries used in this algorithm
* numpy
* opencv
* queue
* time
* rospy
* geometry_msgs

package directory structure

a_star_diff_drive
|- launch/
|- src|
|     |-astar.py
|     |-map.py
|     |-ros_messenger.py
|     |-ros_messenger.py
|
|-source_code.py
|map|
|   |-map.world
|-package.xml
|-README.md

# Stepts to run the algorithm
1. Paste the a_star_diff_drive in the src folder of ros workspace
2. build the package using catkin_make
3. In one terminal, paste : "roslaunch a_star_diff_drive a_star.launch", once the gazebo is launched, in another terminal, enter into the directory catkin_ws/src/a_star_diff_drive/, and execute "python3 source_code.py"
4. Enter the clearance value, start position, goal position.
5. Once the goal is reached, the node exploration and path will be visualised using opencv.
6. After the visualization, the turtlebot3 will start moving to the goal location.


project members: 
1. Sai Surya
Directory ID - saisurya
UID -119224113

2. Dhruv Sharma
Directory ID - dhruvsh
UID - 119091586

Github Repo - https://github.com/Surya-Sriramoju/A-star-for-differential-drive-robot

link to the video: https://drive.google.com/file/d/1PLs5c8GCXTIwWq1v8pyAN5shnO4Z0-_v/view?usp=sharing
