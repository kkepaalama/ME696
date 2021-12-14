#!/usr/bin/env python

import rospy
from math import sqrt, sin, cos, pi
from geometry_msgs.msg import Pose, Twist
import numpy as np

class Waypoint():

    def __init__(self):

        self.x_k = 100   #desired x-position
        self.y_k = 100   #desired y-position
        self.x_k0 = 0   #pervious/starting x-position
        self.y_k0 = 0   #previous/starting y-position
        self.x_pos = 0  #current x-position
        self.y_pos = 0  #current y-position
        self.forward_speed = 2

        rospy.Subscriber("coordinates", Pose, queue_size = 10)

        pub = rospy.Publisher('', Twist, queue_size = 10)
        rospy.init_node('waypoint', String, queue_size = 10)
        rate = rospy.Rate(10)

    def pose(self):
        self.pose()

    def enu2ned():
        R = np.array([[0, 1, 0],
                      [1, 0, 0],
                      [0, 0, -1]])
        return R


    if __name__ == '__main__':
        try:
        talker()
        except rospy.ROSInterruptException:
        pass
