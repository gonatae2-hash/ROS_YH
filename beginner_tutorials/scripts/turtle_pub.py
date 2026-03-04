#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist

def circle():

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rospy.init_node('turtle_pub')

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2
        msg.angular.z = 1
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':

    try:

        circle()

    except rospy.ROSInterruptException:

        pass