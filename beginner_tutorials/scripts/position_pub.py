#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def callback(data):
    if data.x <= 1.0 or data.x >= 10.0 or data.y <= 1.0 or data.y >= 10.0:
        rospy.logwarn("경고! x: %.2f, y: %.2f", data.x, data.y)
    else:
        rospy.loginfo("현재 위치 x: %.2f, y: %.2f", data.x, data.y)

def wall_monitor():
    rospy.init_node('wall_monitor')
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        wall_monitor()
    except rospy.ROSInterruptException:
        pass