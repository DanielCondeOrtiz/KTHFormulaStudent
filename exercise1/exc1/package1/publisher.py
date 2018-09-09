#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('Conde', Int32, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(0.05)
    number = 1
    n=4

    while not rospy.is_shutdown():
        rospy.loginfo(number)
        pub.publish(number)
        number = number + 4
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
