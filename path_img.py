import os
import shutil

paths = []
pathsMove = []

# Đường dẫn đến thư mục nguồn 
source_directory = 'C:/Users/PC/Desktop/auto/data'
# Đường dẫn đến thư mục cần di chuyển
destination_directory = 'C:/Users/PC/Desktop/auto/data/img'

def getPathImg():
    # Danh sách các định dạng file ảnh phổ biến
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    # Kiểm tra nếu thư mục đích không tồn tại thì tạo mới
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    paths.clear()
    pathsMove.clear()

    # Lặp qua tất cả các file trong thư mục nguồn
    for filename in os.listdir(source_directory):
        # Lấy phần mở rộng của file
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Kiểm tra nếu file là ảnh
        if file_ext in image_extensions:
            source_file_path = os.path.join(source_directory, filename)
            pathMove = os.path.join(destination_directory, filename)
            paths.append(source_file_path)
            pathsMove.append(pathMove)
    return paths


def moveFile(source_file_path, destination_file_path):
    try:
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved image: {source_file_path}")
    except Exception as e:
        print(f"Could not move image {source_file_path}: {e}")

def moveALLFile():
    for i in range(len(paths)):
        moveFile(paths[i], pathsMove[i])

 

