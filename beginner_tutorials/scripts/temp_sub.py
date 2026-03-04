#!/usr/bin/env python3

import rospy

from std_msgs.msg import Float32

def callback(msg):

    rospy.loginfo("온도: %0.1f", msg.data)

def listener():

    rospy.init_node('temp_sub')

    rospy.Subscriber('temperature', Float32, callback)

    rospy.spin()

if __name__ == '__main__':

    listener()