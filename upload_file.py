from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import pywinauto  as application
import time
from selenium import webdriver
from datetime import datetime, timedelta
import path_img
import save_file        
 

# # Tùy chọn để sử dụng hồ sơ
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--user-data-dir=/Users/PC/AppData/Local/Google/Chrome/User Data/")
# chrome_options.add_argument("--profile-directory=Default")

# # Khởi tạo trình duyệt với tùy chọn
# driver = webdriver.Chrome(options=chrome_options)

# # Mở URL của truyện
# base_url = "https://keep.google.com"
def autoIMG( driver ):
    # driver.get(base_url)
    driver.find_element(By.CSS_SELECTOR, "div[data-tooltip-text='Ghi chú mới có hình ảnh']").click()
    time.sleep(2)
    upload_element = driver.find_element(By.XPATH, '//input[@type="file"]')

    # Đường dẫn đến các file bạn muốn tải lên

    # Gửi các file đến phần tử input
    time.sleep(2)
    data = path_img.getPathImg()
    if data:
        upload_element.send_keys('\n'.join(path_img.getPathImg()))
        time.sleep(1)
        # Đống dialog Open
        app = application.Application().connect(title_re=".*Open*")
        dialog = app.window(title_re=".*Open*")
        dialog.close()
        
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tạo ghi chú…']").click()
        time.sleep(25)

        
        loopFindThem = True
        count = 0
        while loopFindThem:
            webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
            time.sleep(0.5)
            active_element = driver.switch_to.active_element

            count += 1
            # Lấy giá trị của thuộc tính data-tooltip-text
            tooltip_text = active_element.get_attribute('data-tooltip-text')

            # Kiểm tra giá trị của thuộc tính
            if tooltip_text == 'Thêm':
                loopFindThem = False
                webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
            if(count > 20):
                break


        for i in range(6):
            webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(0.5)

        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform() 


        time.sleep(2)
        caption = driver.find_elements(By.CSS_SELECTOR,'[contenteditable="true"]')[1].text


        file_path = 'C:/Users/PC/Desktop/auto/text/repeat.txt'
        save_file.write_to_file(file_path,caption)

        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        webdriver.ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform() 
        
        path_img.moveALLFile()
    # actions = ActionChains(driver)
    # actions.key_down(Keys.ALT).send_keys(Keys.ALT).key_up(Keys.ARROW_LEFT).perform()
    # time.sleep(20)
    # driver.close()

 