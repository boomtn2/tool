import save_file
import os
import shutil
import re

log_directory = 'C:/Users/PC/Desktop/auto/text/log.txt'
# Đường dẫn đến thư mục nguồn 
source_directory = 'C:/Users/PC/Desktop/auto/data'

backup_directory = 'C:/Users/PC/Desktop/auto/data/backup'

# Đường dẫn đến thư mục cần di chuyển
destination_directory = 'C:/Users/PC/Desktop/auto/data/text'

def getPathText(dataMap):
    # Danh sách các định dạng file ảnh phổ biến
    image_extensions = ['.txt']
    # Kiểm tra nếu thư mục đích không tồn tại thì tạo mới
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    # Lặp qua tất cả các file trong thư mục nguồn
    for filename in os.listdir(source_directory):
        # Lấy phần mở rộng của file
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Kiểm tra nếu file là ảnh
        if file_ext in image_extensions:
            source_file_path = os.path.join(source_directory, filename)
            text = save_file.read_file(source_file_path)
            data = extract_text_from_chapter(text,'Chương')

            for i in data:
                try:
                    stKey = i.upper()
                    stKey = stKey.strip()
                    stRepeat = dataMap[stKey]
                    text = text.replace(i, stRepeat)
                except:
                    save_file.write_to_file(log_directory,'\n'+i)
            moveFile(source_file_path, backup_directory)
            save_file.write_repeat_to_file(source_file_path, text)
     


def moveFile(source_file_path, destination_file_path):
    try:
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved image: {source_file_path}")
    except Exception as e:
        print(f"Could not move image {source_file_path}: {e}")


 

def replace_rep(text):
    # Thay thế các từ "REP" bằng "\n REP \n"
    return text.replace("REP", "\n REP \n")


def extract_text_between_reps(text):
    # Tìm tất cả các đoạn văn bản nằm giữa các từ REP
    pattern = r"REP(.*?)(?=REP|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def extract_text_between_img(text, key):
    # Tìm tất cả các đoạn văn bản nằm giữa các từ REP
    pattern = rf"{key}(.*?)(?={key}|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    return matches

def extract_text_from_chapter(text, chapter_keyword):
    # Biểu thức chính quy tìm đoạn văn bản từ từ khóa "Chương" đến hết dòng
    pattern = rf"{chapter_keyword}[^\r\n]*"
    matches = re.findall(pattern, text, re.MULTILINE)
    return matches
 
text = save_file.read_file('C:/Users/PC/Desktop/auto/text/repeat.txt')
new_text = replace_rep(text)
dataRepeat = extract_text_between_reps(new_text)

dataMap = {}
for i in dataRepeat:
    key = extract_text_from_chapter(i,'Chương')
    if(len(key)> 0):
        data = i.replace(key[0], "")
        stKey = key[0].upper()
        stKey = stKey.strip()
        dataMap[stKey] = data

getPathText(dataMap)