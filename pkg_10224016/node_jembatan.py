# ~/ros_ws/src/ms2-tb1-cakrai17-13523093/pkg_13523093/pkg_13523093/bridge_node.py

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class BridgeNode(Node):
    def __init__(self):
        super().__init__('bridge_node')
        self.publisher_cmd_vel = self.create_publisher(Twist, 'cmd_vel', 10)
        self.publisher_cmd_type = self.create_publisher(String, 'cmd_type', 10)
        self.subscription = self.create_subscription(Twist, 'autonomous_vel', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.publisher_cmd_vel.publish(msg)

        cmd_type_msg = String()
        cmd_type_msg.data = 'autonomous'
        self.publisher_cmd_type.publish(cmd_type_msg)

        self.get_logger().info('Relayed Twist → cmd_vel and sent cmd_type: "autonomous"')

def main(args=None):
    rclpy.init(args=args)
    node = BridgeNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
