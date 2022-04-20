#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
def calc(m1,m2,r):
    G=20
    w = (G*(m1+m2)/(r**3))**0.5
    v1 = (m2*r*w)/(m1+m2)
    v2 = (m1*r*w)/(m1+m2)
    return w,v1,v2
def main():
    p1 = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size = 10)
    p2 = rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size = 10)
    rospy.init_node("Tut_Node")
    vm = Twist()
    rate = rospy.Rate(10)
    w,v1,v2 = calc(1,1.5,5)    
    while not rospy.is_shutdown():
        vm.linear.x = v1
        vm.linear.y = 0
        vm.linear.z = 0
        vm.angular.x = 0
        vm.angular.y = 0
        vm.angular.z = -1*w
        p1.publish(vm)
        vm.linear.x = v2
        vm.angular.z = w
        p2.publish(vm)
        rate.sleep()
if __name__ == '__main__':
    main()
