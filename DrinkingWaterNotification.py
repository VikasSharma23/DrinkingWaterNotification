import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="Please Drink water now !!!",
            message="Jal hi Jivan hai",
            timeout=15
        )
        time.sleep(3600)