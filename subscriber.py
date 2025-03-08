import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from math import sqrt

def distanceFromOrigin(x: float, y: float):
    return sqrt(x**2 + y**2)

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
        distanceTurtleSim = distanceFromOrigin(msg.x, msg.y)
        self.get_logger().info('The distance from origin is: {}'.format(distanceTurtleSim))

def main(args=None):
    rclpy.init(args=args)

    poseSubscriber = PoseSubscriber()

    rclpy.spin(poseSubscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
