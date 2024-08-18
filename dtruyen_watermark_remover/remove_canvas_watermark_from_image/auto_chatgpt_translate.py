import pyautogui
import time
import os
import chardet
import clipboard

print("Kết thúc.")

def merge_txt_files(directory_path, output_file_path):

    def detect_file_encoding(file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            return result['encoding']

    txt_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]
    txt_files.sort()

   
    for txt_file in txt_files:
        file_path = os.path.join(directory_path, txt_file)
        file_encoding = detect_file_encoding(file_path)

        with open(file_path, 'r', encoding=file_encoding) as infile:
            contents = infile.read()
            pyautogui.click(400, 985)
            clipboard.copy(contents)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(2)
            pyautogui.click(913, 982)
            time.sleep(120)
            pyautogui.hotkey('f5')
            time.sleep(5)
            pyautogui.click(871, 903)
            time.sleep(20)
            pyautogui.click(373, 881)
            
            text = clipboard.paste()    
            with open(output_file_path+txt_file, 'w', encoding="utf-8") as outfile:
                outfile.write(text)
            print(f"{file_path}")

if __name__ == "__main__":
    directory = "C:/Users/PC/Desktop/Thập niên 90, ta nhặt ve chai mua nửa con phố/"
    output_file = "C:/Users/PC/Desktop/Thập niên 90, ta nhặt ve chai mua nửa con phố/dich/"
    merge_txt_files(directory, output_file)
    print(f"Files merged into {output_file}")


