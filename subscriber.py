import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from std_msgs.msg import String
from math import sqrt

distanceFromOrigin = 0

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

        self.publisher_ = self.create_publisher(String, '/turtle1/distance_from_origin', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def listener_callback(self, msg):
        distanceTurtleSim = distanceFromOrigin(msg.x, msg.y)

    
    def timer_callback(self):
        msg = String()
        msg.data = 'The distance from origin is: {}'.format(distanceTurtleSim)
        self.get_logger().info('Publishing: {}'.format(msg.data))


def main(args=None):
    rclpy.init(args=args)

    poseSubscriber = PoseSubscriber()

    rclpy.spin(poseSubscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
