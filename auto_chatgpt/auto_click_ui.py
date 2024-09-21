import pyautogui
import time
import clipboard
import read_file
import porm
import save_file


def clickSend():
    x = 902
    y = 946
    pyautogui.click(x,y)
    

def sendText(contents):
    text = porm.porm + contents
    x = 371
    y = 951
    time.sleep(1)
    pyautogui.click(x,y)
    clipboard.copy(text)
    time.sleep(1) 
    pyautogui.hotkey('ctrl', 'v')

def clickCoppy():
    x = 487
    y = 500
    pyautogui.click(x,y)
    scroll()
    clipboard.copy("")
    time.sleep(1) 
    pyautogui.click(x,y)
    # pyautogui.press('tab', presses=2)
    time.sleep(2)
    pyautogui.click(125,855) 
    # pyautogui.press('enter')

def scroll():
    pyautogui.scroll(500)
    time.sleep(2) 
    pyautogui.scroll(-5000)
    
def saveFile(text, path):
    save_file.write_to_file(path, text)

def close():
    x = 28
    y = 114



def position():
    while True:
        x, y = pyautogui.position()

    # In tọa độ
        print(f"Tọa độ con trỏ chuột: ({x}, {y})")
        time.sleep(2)
    
def newChat():
    pyautogui.click(507,146)
    time.sleep(1)
    pyautogui.click(463,206)
    time.sleep(5)


path = "E:/code/tool/auto_chatgpt/save/"
pathError = "E:/code/tool/auto_chatgpt/error/"
count = 0
chuong = 4
start_index = 28
 

data = read_file.getData()
time.sleep(2) 
for i in range(start_index, len(data)):
    item = data[i]
    sendText(item) 
    time.sleep(2) 
    clickSend()
    time.sleep(50) 
    clickCoppy()
    time.sleep(2)
    text = clipboard.paste()
   
    saveFile(f"\n{i}\n", pathError+f"log.txt")
 
    print(i)
    if not text:
        saveFile(f"\nchuong_{chuong} error_{count} \n {item}\n", pathError+f"error.txt")
        saveFile(f"\nerror_{count} \n", path+f"chuong_{chuong}.txt")
    else:
        saveFile(clipboard.paste(), path+f"chuong_{chuong}.txt")
    count += 1
    if count > 10 :
        count = 0
        chuong += 1
    
    if chuong % 2 == 0:
        newChat()

