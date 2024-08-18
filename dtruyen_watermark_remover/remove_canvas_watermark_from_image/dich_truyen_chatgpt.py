from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time
from selenium import webdriver
from datetime import datetime, timedelta
import clipboard
from fake_useragent import UserAgent

def split_string_at_sentence_end(input_string, max_chunk_size):
    chunks = []
    start = 0
    while start < len(input_string):
        # Tìm vị trí của dấu chấm gần 1000 ký tự kế tiếp
        end = input_string.rfind('.', start, start + max_chunk_size + 1)
        if end == -1:
            # Nếu không tìm thấy dấu chấm, chọn ngắt ở vị trí max_chunk_size
            end = start + max_chunk_size
            if end > len(input_string):
                end = len(input_string)
        else:
            # Cộng thêm 1 để bao gồm dấu chấm vào trong chuỗi
            end += 1
        
        # Thêm đoạn văn bản vào danh sách
        chunks.append(input_string[start:end])
        start = end
    
    return chunks

# Tùy chọn để sử dụng hồ sơ
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/Users/PC/AppData/Local/Google/Chrome/User Data/")
chrome_options.add_argument("--profile-directory=Default")
chrome_options.add_argument(f"user-agent={UserAgent.random}")


# Khởi tạo trình duyệt với tùy chọn
driver = webdriver.Chrome(options=chrome_options)

# Mở URL của truyện
indexChuong = 161
base_url = "https://truyenwikidich.net/truyen/60-doan-sung-mang-theo-khong-gian-ga-tha/chuong-161-ngo-nu-ten-moc-tui-ZktOLcQsRHkPt3GA"
driver.get(base_url)
time.sleep(1)

chapter_number = 0  # Số chương hiện tại
part_number = 1  # Số tập hiện tại
chapter_content_list = []  # Danh sách chứa nội dung chương
chapter_name_list = []  # Danh sách chứa tên của từng chương
data_translate = []
driver.execute_script("window.open('https://chatgpt.com/')")
time.sleep(3)
porm = '''Nhập vai là nhà văn 'Nam Cao' của văn học việt nam. Hãy thay đổi cách hành văn với các yêu cầu sau. Giữ nội dung của câu văn. Đoạn văn cần thay đổi "'''
while True:
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    chapter_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#bookContentBody")))
    chapter_name = chapter_name_element.text
    chapter_name_list.append(f"{chapter_number}. {base_url}")

    element = porm+chapter_name+'"'
    driver.switch_to.window(driver.window_handles[1])
    
 
    try:
        clipboard.copy(element)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "textarea").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "textarea").send_keys(Keys.CONTROL, 'v')
        time.sleep(1)
        #button send document.querySelector('button[data-testid="fruitjuice-send-button"]')
        driver.find_element(By.CSS_SELECTOR, "button[data-testid='fruitjuice-send-button']").click()
            
        #list button document.querySelectorAll('div[data-scroll-anchor="true"] span[data-state="closed"] button')
        #button coppy index 2
        time.sleep(80)
        try:
            driver.find_element(By.CSS_SELECTOR, "div[style='opacity: 1;'] button").click()
            time.sleep(30)
        except:
            print('Lỗi không tìm tiếp tục')
        finally:
            #button contineus document.querySelector('div[style="opacity: 1;"] button').click()
            try:
                listButton =  driver.find_elements(By.CSS_SELECTOR, "div[data-scroll-anchor='true'] span[data-state='closed'] button") 
                listButton[1].click()
            except:
                time.sleep(20)
                listButton =  driver.find_elements(By.CSS_SELECTOR, "div[data-scroll-anchor='true'] span[data-state='closed'] button") 
                listButton[1].click()
             

        #button contineus document.querySelector('div[style="opacity: 1;"] button').click()
        text = clipboard.paste()
        data_translate.append(text)
    finally:
        print('oke 1 file')
        driver.switch_to.window(driver.window_handles[0])

    try:
        updated_list = [f'Chương {(indexChuong+chapter_number)}'] + data_translate
        with open(f"namechapter.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(chapter_name_list))
        with open(f"translate.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(updated_list))
        part_number += 1
        chapter_content_list = []
        chapter_name_list = []
        updated_list = []
    except:
        with open(f"error.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(chapter_name_list))
    
    # Kiểm tra nếu đã hết truyện thì dừng vòng lặp
    try:
        if driver.find_elements(By.CSS_SELECTOR, "a.chap-nav[title='Chương Sau'].disabled"):
            break
    finally:
        if part_number == 40:
            break
    # Tìm và nhấn vào thẻ <a>Chương sau</a>
    next_chapter_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='btnNextChapter']")))
    next_chapter_link.click()

    # Đợi một thời gian trước khi lấy nội dung của chương tiếp theo
    time.sleep(4)
    chapter_number += 1

# Đóng trình duyệt khi hoàn thành
driver.quit()