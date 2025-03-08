 = 0

def calcDistance(x: float, y: float):
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

    def listener_callback(self, msg):
        distanceFromOrigin = calcDistance(msg.x, msg.y)

        outputMsg = String()
        outputMsg.data = "The distance from origin is: {}".format(distanceFromOrigin)
        self.publisher_.publish(outputMsg)
        self.get_logger().info("Publishing: {}".format(outputMsg.data))


def main(args=None):
    rclpy.init(args=args)

    poseSubscriber = PoseSubscriber()

    rclpy.spin(poseSubscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
