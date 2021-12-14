#!/usr/bin/evn python

import rospy

from heading import LosGuidance
from waypoint import Waypoint
from geometry_msgs.msg import Twist, Pose
from nav_msgs.msg import Odometry

class GuidanceROSWrapper:

        def __init__(self):
            self.los = LosGuidance()

            rospy.Subscriber("odometry/filtered", Odometry)

            rospy.Publisher("",  ,  )



if __name__=='main':
    try:
        rospy.init_node('line_of_sight')
        los_wrapper = LosROSWrapper()
        rospy.loginfo("Vechile enroute")
        rospy.sipn()
    except rospy.ROSInterruptException
        pass
