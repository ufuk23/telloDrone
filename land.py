from time import sleep
import tellopy


def test():
    drone = tellopy.Tello()
    try:
        drone.connect()
        drone.wait_for_connection(60.0)
        drone.land()
        sleep(5)
    finally:
        drone.quit()

if __name__ == '__main__':
    test()