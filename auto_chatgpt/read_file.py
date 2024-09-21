import json

def getData():
        # Đường dẫn tới tệp JSON
    file_path = 'E:/code/tool/auto_chatgpt/data.json'

    # Đọc tệp JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    text =  []
    for item in data:
        text.append(item.get("data_input"))

    return text
    