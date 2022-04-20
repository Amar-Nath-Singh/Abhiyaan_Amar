#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def main():
    p = rospy.Publisher("/team_abhiyaan",String,queue_size = 10)
    rospy.init_node("node1")
    rate = rospy.Rate(10)
    
    #Publishing to node "/team_abhiyaan" until rospy shutsdown
    
    while not rospy.is_shutdown():
        s = "Team Abhiyaan rocks:" # String to be published
        p.publish(s)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
