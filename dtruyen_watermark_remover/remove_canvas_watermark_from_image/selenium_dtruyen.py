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

# Tùy chọn để sử dụng hồ sơ
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/Users/PC/AppData/Local/Google/Chrome/User Data/")
chrome_options.add_argument("--profile-directory=Default")

# Khởi tạo trình duyệt với tùy chọn
driver = webdriver.Chrome(options=chrome_options)

# Mở URL của truyện
base_url = "https://dtruyen.com/ve-que-truoc-nam-70-toi-dung-khong-gian-don-sach-ke-thu/dai-ket-cuc-2_5375980.html"
driver.get(base_url)
time.sleep(1)

chapter_number = 1  # Số chương hiện tại
part_number = 1  # Số tập hiện tại
chapter_content_list = []  # Danh sách chứa nội dung chương
chapter_name_list = []  # Danh sách chứa tên của từng chương

while True:
    chapter_name_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "chapter-title")))
    chapter_name = chapter_name_element.text
    chapter_name_list.append(f"{chapter_number}. {chapter_name}")

    print(f"Success {chapter_number}: {chapter_name}")

    chapter_content_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#chapter-content > *")))

    for element in chapter_content_elements:
        if element.tag_name == "canvas":
            # Click chuột phải vào phần tử canvas
            action = ActionChains(driver)
            action.context_click(element).perform()
            time.sleep(1)
            pyautogui.press('down', presses=2)  # Nhấn phím mũi tên xuống hai lần
            pyautogui.press('enter')
            time.sleep(1)
            driver.execute_script("window.open('https://keep.google.com')")
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tạo ghi chú…']").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "div[role='textbox']").send_keys(Keys.CONTROL, 'v')
            time.sleep(6)
            pyautogui.press('tab', presses=8)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('down', presses=6)
            pyautogui.press('enter')
            caption = driver.find_element(By.CSS_SELECTOR,
                                          "div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.h1U9Be-YPqjbf[contenteditable='true'][role='textbox']").text
            time.sleep(2)
            chapter_content_list.append(caption)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        elif element.tag_name == "img":
            # Click chuột phải vào phần tử canvas
            action = ActionChains(driver)
            action.context_click(element).perform()
            time.sleep(1)
            pyautogui.press('down', presses=3)  # Nhấn phím mũi tên xuống hai lần
            pyautogui.press('enter')
            time.sleep(1)
            driver.execute_script("window.open('https://keep.google.com')")
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(3)
            driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tạo ghi chú…']").click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, "div[role='textbox']").send_keys(Keys.CONTROL, 'v')
            time.sleep(6)
            pyautogui.press('tab', presses=8)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('down', presses=6)
            pyautogui.press('enter')
            time.sleep(1)
            caption = driver.find_element(By.CSS_SELECTOR,
                                          "div.notranslate.IZ65Hb-YPqjbf.fmcmS-x3Eknd.h1U9Be-YPqjbf[contenteditable='true'][role='textbox']").text
            time.sleep(2)
            chapter_content_list.append(caption)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        elif element.find_elements(By.CSS_SELECTOR,'span.bebi'):
            result = driver.execute_script("""
                            const bebi = document.querySelector('.bebi');
                            if (bebi) {
                                const bebiSpans = Array.from(bebi.querySelectorAll('span'));
                                const sortedBebiSpans = bebiSpans.sort((a, b) => {
                                    const styleA = window.getComputedStyle(a);
                                    const styleB = window.getComputedStyle(b);
                                    return styleA.order - styleB.order;
                                });
                                return sortedBebiSpans.map(span => span.textContent);
                            }
                        """)
            if result is not None:
                if isinstance(result, str):  # Kiểm tra nếu kết quả là một chuỗi
                    chapter_content_list.append(result)
                elif isinstance(result, list):  # Kiểm tra nếu kết quả là một danh sách
                    chapter_content_list.extend(result)
        else:
            chapter_content_list.append(element.text)
        # if not element.find_elements(By.CSS_SELECTOR,
        #                                                                                     'span.bebi'):
        #     chapter_content_list.append(element.text)
        # else:
        #     result = driver.execute_script("""
        #                 const bebi = document.querySelector('.bebi');
        #                 if (bebi) {
        #                     const bebiSpans = Array.from(bebi.querySelectorAll('span'));
        #                     const sortedBebiSpans = bebiSpans.sort((a, b) => {
        #                         const styleA = window.getComputedStyle(a);
        #                         const styleB = window.getComputedStyle(b);
        #                         return styleA.order - styleB.order;
        #                     });
        #                     return sortedBebiSpans.map(span => span.textContent);
        #                 }
        #             """)
        #     if result is not None:
        #         if isinstance(result, str):  # Kiểm tra nếu kết quả là một chuỗi
        #             chapter_content_list.append(result)
        #         elif isinstance(result, list):  # Kiểm tra nếu kết quả là một danh sách
        #             chapter_content_list.extend(result)
    
   # if chapter_number % 2 == 0 or driver.find_elements(By.CSS_SELECTOR, "a.chap-nav[title='Chương Sau'].disabled"):
    try:
        updated_list = [s.replace('ℓ', 'l') for s in chapter_content_list]
        with open(f"namechapter.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(chapter_name_list))
        with open(f"{part_number}_text.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(updated_list))
        part_number += 1
        chapter_content_list = []
        chapter_name_list = []
        updated_list = []
    except:
        with open(f"error.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(chapter_name_list))
    
    # Kiểm tra nếu đã hết truyện thì dừng vòng lặp
    if driver.find_elements(By.CSS_SELECTOR, "a.chap-nav[title='Chương Sau'].disabled"):
        break

    # Tìm và nhấn vào thẻ <a>Chương sau</a>
    next_chapter_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Sau')]")))
    next_chapter_link.click()

    # Đợi một thời gian trước khi lấy nội dung của chương tiếp theo
    time.sleep(1)
    chapter_number += 1

# Đóng trình duyệt khi hoàn thành
driver.quit()