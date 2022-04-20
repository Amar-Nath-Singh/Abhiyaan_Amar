#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def callback(data):
    s = str(data.data)[::-1] #Reversing the given data
    p = rospy.Publisher("/naayihba_maet",String,queue_size = 10)
    rate = rospy.Rate(10)
    #Publishing to node "/naayihba_maet" until rospy shutsdown
    while not rospy.is_shutdown():
        rospy.loginfo(s)
        p.publish(s)
        rate.sleep()
def main():
    #initializing Node
    rospy.init_node('node')
    rospy.Subscriber("/team_abhiyaan", String, callback)
    #Subscribed to node '/team_abhiyaan' 
    rospy.spin()
if __name__ == '__main__':
    main()
