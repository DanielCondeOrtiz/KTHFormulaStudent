#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32

def callback(data):
    q=0.15
    rospy.loginfo('Number: %f', data.data/q)

def listener():

    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('Conde', Int32, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
