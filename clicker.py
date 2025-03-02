import time
import pyautogui
import keyboard

def main():
    print("程序启动：初始等待3秒后读取鼠标位置并开始连点")
    time.sleep(3)
    x, y = pyautogui.position()
    print(f"开始连点：当前点击位置为({x}， {y})")
    print("按空格键暂停/恢复（恢复时等待3秒重新获取鼠标位置），按ESC退出程序。")

    paused = False  # 当前是否处于暂停状态

    while True:
        # 检测退出
        if keyboard.is_pressed('esc'):
            print("检测到ESC键，程序退出")
            break

        # 检测暂停或恢复的切换
        if keyboard.is_pressed('space'):
            if not paused:
                paused = True
                print("程序已暂停，等待再次按空格键恢复...")
            else:
                print("检测到恢复指令，3秒后重新获取鼠标位置开始连点")
                time.sleep(3)
                x, y = pyautogui.position()
                print(f"新鼠标位置：({x}， {y})")
                paused = False

            # 防止按键抖动，等待空格键释放
            while keyboard.is_pressed('space'):
                time.sleep(0.1)

        # 如果没有暂停，则执行连点操作
        if not paused:
            pyautogui.click(x, y)
            # 每秒10次点击，间隔0.1秒
            time.sleep(0.2)
        else:
            # 暂停状态下稍作等待，减小CPU占用
            time.sleep(0.1)

if __name__ == "__main__":
    main()
