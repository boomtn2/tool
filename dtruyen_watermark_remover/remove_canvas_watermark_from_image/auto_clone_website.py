import pyautogui

# Lấy tọa độ hiện tại của con trỏ chuột
import time
 
 

for i in range(3):  # Kiểm tra nếu còn ít nhất 3 phút
    # Tính toán giờ, phút và giây

    # Định dạng thời gian thành chuỗi
   

    pyautogui.click(63, 985)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    # In thời gian và giảm thời gian đi 3 phút
    
    pyautogui.click(760, 393)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(5)
    pyautogui.press('enter')

    pyautogui.click(760, 393)
    time.sleep(5)
 
 
 
 

# print("Kết thúc.")

 
 