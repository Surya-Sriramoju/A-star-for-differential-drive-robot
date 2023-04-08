import rospy
from geometry_msgs.msg import Twist
import time

# Method to move turtlebot on ROS Gazebo with cmd_vel topic
def velocity_pub(direction, robot_radius, wheel_d, stepsize):
    rospy.init_node('command_passer', anonymous=True)
    pub_topic = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    msg = Twist()
    for _, action in direction:
        cnt = 0
        msg_publisher(msg, 0, 0, pub_topic)
        print('Sending RPM\'s to turtlebot: ', (action[0], action[1]))
        while cnt < 50:
            cnt += 1
            v_ang = (robot_radius / wheel_d) * (action[1] - action[0])
            v_lin = 0.5 * robot_radius * (action[0] + action[1])
            msg_publisher(pub_topic, v_lin, v_ang, msg)
    return True


def msg_publisher(pub, vel_lin, vel_ang, msg):
    msg.angular.z = vel_ang / 4.5
    msg.angular.x = 0
    msg.angular.y = 0
    msg.linear.x = vel_lin / 455
    msg.linear.y = 0
    msg.linear.z = 0
    pub.publish(msg)
    time.sleep(0.1)