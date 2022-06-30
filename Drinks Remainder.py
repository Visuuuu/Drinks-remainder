import time 
from plyer import notification
if __name__ == "__main__":
    while True :
        notification.notify(
            title = " Time for drinks and break ",
            message = " It's been long time coding and gaming you need some water to keep yourself hydrated ~ constant use of laptop and computer can also affect eyesights ",
            app_icon = "D:\VS Code work space\icon.ico",
            timeout = 20
        )
        time.sleep (60*30)