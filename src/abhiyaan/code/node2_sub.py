#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() +"MSG : "+str(data.data))
    rospy.loginfo(data.data)
def main():
    rospy.init_node('node2')
    rospy.Subscriber("/team_abhiyaan", String, callback)
    #Subscribed to node '/team_abhiyaan' 
    rospy.spin()
if __name__ == '__main__':
    main()
