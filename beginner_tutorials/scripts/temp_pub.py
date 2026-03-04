#!/usr/bin/env python3

import rospy, random

from std_msgs.msg import Float32

def counter():

    pub = rospy.Publisher('temperature', Float32, queue_size=10)

    rospy.init_node('temp_pub')

    rate = rospy.Rate(0.2)

    while not rospy.is_shutdown():
        temp = random.uniform(20.0, 40.0)
        rospy.loginfo("온도: %.1f", temp)
        pub.publish(temp)
        rate.sleep()

if __name__ == '__main__':

    try:

        counter()

    except rospy.ROSInterruptException:

        pass