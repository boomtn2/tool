import pyautogui
import time
# Tọa độ hiện tại: X = 129, Y = 271
# Tọa độ hiện tại: X = 523, Y = 350
# for i in range(10):
#     # Thực hiện công việc ở mỗi vòng lặp ở đây
#     x, y = pyautogui.position()
#     print(f"Tọa độ hiện tại: X = {x}, Y = {y}")
#     # Đợi 10 giây
#     time.sleep(3)

# Tọa độ x và y bạn muốn click
# x = 378
# y = 74
# Click vào tọa độ x, y
def format_text(input_text):
    # Tách chuỗi ban đầu thành mảng các phần tử
    parts = input_text.split(":")
    
    formatted_text = ":".join([part.zfill(2) for part in parts])
    
    return formatted_text
 
total_seconds = 20
 

while total_seconds > 0:  
    # canvas
    pyautogui.click(1364, 936)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)

    #console web
    pyautogui.click(648, 965)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
     
    #js text
    pyautogui.click(1354, 130)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')

    #console web
    pyautogui.click(648, 965)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
   

    time.sleep(30)
    #next chapter
    pyautogui.click(388, 491)

    
    total_seconds -= 1
 

print("Kết thúc.")