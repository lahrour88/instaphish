import pyautogui ,pyperclip
import time



def login_test(username ,password) :
    print(password)
    try:
        name=pyautogui.locateOnScreen('static/username.png', confidence=0.8)
        if name:
            x ,y= pyautogui.center(name)
            pyautogui.click(x ,y)
            pyperclip.copy(username)
            pyautogui.hotkey('ctrl' ,'v')
            time.sleep(0.3)
            pyautogui.hotkey('tab')
            time.sleep(0.3)
            pyperclip.copy(password)
            pyautogui.hotkey('ctrl' ,'v')
            time.sleep(0.3)
        btn=pyautogui.locateOnScreen('static/button.png', confidence=0.8)
        if btn:
            x ,y= pyautogui.center(btn)
            pyautogui.click(x ,y)
        time.sleep(3)
        error=pyautogui.locateOnScreen('static/incorect.png', confidence=0.8)
        if error:
            return False
        return True
    except Exception as e:
        print(e)

def send_verifications_code(email) :
    try:
        inpute =pyautogui.locateOnScreen("static/username.png" , confidence=0.8)
        if inpute:
            time.sleep(0.3)
            x ,y =pyautogui.center(inpute)
            pyautogui.click(x,y)
            time.sleep(0.3)
            pyperclip.copy(email)
            pyautogui.hotkey('ctrl' ,'v')
            time.sleep(0.3)
            pyautogui.press('enter')
            time.sleep(4)
        kaptchat = pyautogui.locateOnScreen("static/kaptchat.png" , confidence=0.8)
        if kaptchat:
            x ,y =pyautogui.center(kaptchat)
            pyautogui.click(x,y)
            time.sleep(1.3)
            pyautogui.click(pyautogui.locateCenterOnScreen("static/enter.png" ,confidence=0.8))
    except Exception as e:
        print(e)

def write_code(code) :
    try:
        inpute =pyautogui.locateOnScreen("static/code.png" , confidence=0.8)
        if inpute:
            time.sleep(0.3)
            x ,y =pyautogui.center(inpute)
            pyautogui.click(x,y)
            time.sleep(0.3)
            pyperclip.copy(code)
            pyautogui.hotkey('ctrl' ,'v')
            time.sleep(0.3)
            pyautogui.press('enter')
    except Exception as e:
        print(e)