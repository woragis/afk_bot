from pyautogui import move, click, keyUp, keyDown, sleep


def move_little():
    keyDown("a")
    print("A pressed")
    sleep(2)
    keyUp("a")
    print("A unpressed")
    sleep(2)


while True:
    move(3, 3)
    print("Moved")
    sleep(2)
