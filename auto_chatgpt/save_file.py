def write_to_file(file_path, text_to_write):
    # Mở tệp ở chế độ append (ghi thêm) hoặc tạo mới nếu chưa có
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(text_to_write)
        file.flush()  # Đảm bảo dữ liệu được ghi ngay lập tức

def write_repeat_to_file(file_path, text_to_write):
    # Mở tệp ở chế độ ghi (ghi đè), tạo mới nếu chưa có
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text_to_write)
        file.flush()

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# # Đường dẫn đến tệp txt
# file_path = 'path/to/your/file.txt'  # Thay đổi đường dẫn đến tệp của bạn

# # Đọc nội dung tệp
# content = read_file(file_path)
# print(content)

# # Đường dẫn đến tệp txt
# file_path = 'C:/Users/PC/Desktop/auto/text/repeat.txt'  # Thay đổi đường dẫn đến tệp của bạn

# # Văn bản bạn muốn ghi vào tệp
# text_to_write = 'Đây là một dòng văn bản mới.\n'

# # Ghi văn bản vào tệp
# write_to_file(file_path, text_to_write)

# print(f'Đã ghi văn bản vào {file_path}')
