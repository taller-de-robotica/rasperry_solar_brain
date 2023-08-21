import cv2
import json

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from .redis_store import get_from_cache

'''
Este nodo esta diseñado para debuguear watcher_pub, solo se puede usar
si se ejecuta en la misma maquina donde se encuentra la instancia de redis
'''
class WatcherSubscriber(Node):

    def __init__(self):
        super().__init__('watcher_subscriber')
        self.subscription = self.create_subscription(
            String,
            'solar_panel_watcher',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        self.get_logger().info('I heard: "%s"' % msg.data)
        try:
            data = json.loads(msg.data)
            ret, image = get_from_cache(data['id'])
            if ret:
                cv2.imshow("watcher_sub", image)
                cv2.waitKey(100)
            else:
                self.get_logger().info('nothing')
        except Exception as ex:
            self.get_logger().warning(f'{ex}')


def main(args=None):
    #cv2.namedWindow("watcher_sub")
    rclpy.init(args=args)

    watcher_subscriber = WatcherSubscriber()

    rclpy.spin(watcher_subscriber)
    cv2.destroyAllWindows()
    watcher_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()