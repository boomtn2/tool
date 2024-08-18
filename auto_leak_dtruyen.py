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
import upload_file
import save_file

# init config
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=/Users/PC/AppData/Local/Google/Chrome/User Data/")
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

jsCanvas = save_file.read_file('C:/Users/PC/Desktop/code_tool/dtruyen_watermark_remover/dtruyen_watermark_remover/remove_canvas_watermark_from_image/canvas.txt')

jsText = save_file.read_file('C:/Users/PC/Desktop/code_tool/dtruyen_watermark_remover/dtruyen_watermark_remover/remove_canvas_watermark_from_image/js_clone_dtruyen.txt')

# Website leak
base_url = "https://dtruyen.com/quan-cuoi-thap-nien-80-thay-chi-ga-chong/xau-ho_5927412.html"
driver.get(base_url)



while True:
    time.sleep(5)
    
    driver.execute_script(jsCanvas)
    time.sleep(1)
    driver.execute_script(jsText)
    time.sleep(1)
    

    try:
        driver.execute_script("window.open('https://keep.google.com')")
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        upload_file.autoIMG(driver)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
    finally:
        # [title="Chương Sau"]
        try:
            if driver.find_elements(By.CSS_SELECTOR, "a.chap-nav[title='Chương Sau'].disabled"):
                break
            driver.find_element(By.CSS_SELECTOR, "a.chap-nav[title='Chương Sau']").click()
        except:
            break
