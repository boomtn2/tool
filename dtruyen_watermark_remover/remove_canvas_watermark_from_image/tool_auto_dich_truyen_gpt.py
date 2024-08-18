# chrome
import pyautogui
import pyperclip
import time
import os

# Đường dẫn đến thư mục chứa các file txt cần dịch
folder_path = r"C:\Users\PC\Desktop\Thập niên 90, ta nhặt ve chai mua nửa con phố"
# Đường dẫn đến tệp log
log_file_path = r"C:\Users\PC\Desktop\\Thập niên 90, ta nhặt ve chai mua nửa con phố\translation_log.txt"

save_path = r"C:\Users\PC\Desktop\Thập niên 90, ta nhặt ve chai mua nửa con phố\autodich"

# Hàm để ghi số thứ tự của file cuối cùng đã xử lý vào trạng thái
def update_last_processed_index(index):
    pass  # Không cần thực hiện ghi vào trạng thái


# Tạo danh sách các tệp tin
file_list = [str(i) for i in range(62, 119)]  # Bắt đầu từ file ?
global flag
flag = 0
global f5
f5 = 0
# Hàm để sao chép nội dung của một file vào clipboard và dịch nó
def translate_and_save(file_path, output_folder_path):
    global flag
    global f5
    # Đọc nội dung từ file và sao chép vào clipboard
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    # Thêm chuỗi "Dịch Sang TIẾNG VIỆT" vào trước nội dung
    translated_content = "Dựa vào hướng dẫn đã được đào tạo. Hãy dịch văn bản sau, không dược giữ 1 từ tiếng Trung nào trong câu trả lời và chỉ trả lời nội dung truyện: \n" + content

    # Copy nội dung đã được dịch vào clipboard
    pyperclip.copy(translated_content)

    # Tọa độ của điểm cần click để dán nội dung
    paste_x, paste_y = 941, 982
    # Tọa độ của nút copy
    copy_x, copy_y = 790, 870
    scr_x, scr_y = 1200, 922
    time.sleep(5)
    # Click vào điểm cần dán
    pyautogui.click(paste_x, paste_y)
    # Dán nội dung từ clipboard
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Chờ 1 giây
    # pyautogui.press('enter')  # Nhấn phím Enter
    pyautogui.click(1447, 979)
    time.sleep(5)

    # Xóa nội dung trên clipboard
    pyperclip.copy('')

    #click theo chat
    pyautogui.click(1230, 935)
    time.sleep(5)
    #click theo chat
    pyautogui.click(1230, 935)
    time.sleep(5)
    pyautogui.click(1230, 935)
    time.sleep(55)
    #click vi tri de scroll
    pyautogui.click(scr_x, scr_y)
    pyautogui.scroll(-100000)
    time.sleep(1)
    # pyautogui.click(copy_x, copy_y)
    pyautogui.click(759, 870)
    # [746, 897]
    # Lấy nội dung đã dịch từ clipboard
    translated_content = pyperclip.paste()
    if translated_content == '':
        pyautogui.click(copy_x, copy_y)
        translated_content = pyperclip.paste()
    if translated_content == '':
        pyautogui.click(758,870)
        translated_content = pyperclip.paste()
    
    #TH: nút có các bản trc đó nút coppy ở xa
    if translated_content == '':
        pyautogui.click(877,866)
        translated_content = pyperclip.paste()
    f5 = f5 + 1
    if f5 == 3:
        f5 = 0
        # click refesh
        pyautogui.click(91, 61)
        time.sleep(10)
    flag = flag + 1
    if flag == 10:
        # pyautogui.click(83, 160)
        pyautogui.click(111, 396)
        time.sleep(10)
        flag = 0
    if translated_content == '':
        error_message = f"Error: Empty translation for file: {file_path}\n"
        print(error_message)
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(error_message)
        return
    # Tạo và lưu nội dung đã dịch vào file mới
    output_file_path = os.path.join(output_folder_path, "{}.txt".format(os.path.basename(file_path).split(".")[0]))
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(translated_content)


# Duyệt qua từng file và dịch chúng
for filename in file_list:
    file_path = os.path.join(folder_path, filename + ".txt")
    translate_and_save(file_path, r"C:\Users\PC\Desktop\Thập niên 90, ta nhặt ve chai mua nửa con phố\autodich")