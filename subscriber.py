import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose

class PoseSubscriber(Node):

    def __init__(self):
        super().__init__('poseSubscriber')
        self.subscription = self.create_subscription(
                Pose,
                '/turtle1/pose',
                self.listener_callback,
                10
                )
    
    def listener_callback(self, msg):
        self.get_logger().info('The x coordinate is: "%d"' % msg.x)

def main(args=None):
    rclpy.init(args=args)

    poseSubscriber = PoseSubscriber()

    rclpy.spin(poseSubscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
