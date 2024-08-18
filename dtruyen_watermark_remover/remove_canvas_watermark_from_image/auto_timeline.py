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
h  = 11
hours = 11
minutes = 43
total_seconds = (hours * 3600) + (minutes * 60)  
formatted_time = ""

while total_seconds >= 3 * 60:  # Kiểm tra nếu còn ít nhất 3 phút
    # Tính toán giờ, phút và giây
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # Định dạng thời gian thành chuỗi
    formatted_time = f"{hours:01d}:{minutes:02d}:{seconds:02d}"

    # In thời gian và giảm thời gian đi 3 phút
    pyautogui.click(129, 271)
    time.sleep(1)
    # Gửi văn bản vào cửa sổ đã được focus
    pyautogui.click(420, 320)
    pyautogui.hotkey('ctrl', 'a')
    
    text_to_type = f"{formatted_time}:00"
   
    if(h >= 10):
       text_to_type = format_text(text_to_type)
  
    pyautogui.typewrite(text_to_type)
    time.sleep(1)
    pyautogui.press('enter')
   
    total_seconds -= 3 * 60
 

print("Kết thúc.")



