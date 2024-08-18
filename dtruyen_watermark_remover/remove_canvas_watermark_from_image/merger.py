import os
import chardet

def merge_txt_files(directory_path, output_file_path):

    def detect_file_encoding(file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            return result['encoding']

    txt_files = [f for f in os.listdir(directory_path) if f.endswith(".txt")]
    txt_files.sort()
    index =1
    with open(output_file_path, 'w', encoding="utf-8") as outfile:
        for txt_file in txt_files:
            file_path = os.path.join(directory_path, txt_file)
            file_encoding = detect_file_encoding(file_path)

            with open(file_path, 'r', encoding=file_encoding) as infile:
                contents = infile.read()
                # outfile.write(contents)
                outfile.write(f"\n Chương {index}: \n {contents} \n Nghe Audio Trên Ứng dụng: 'Audio Quân Hôn Ngôn Tình' Hoàn toàn miễn phí.")
                index+=1
            print(f"{file_path}")

if __name__ == "__main__":
    directory = "C:/Users/PC/Desktop/Tiểu Thư Phá Sản Tái Sinh Hủy Hôn, Chuyển Xuống Nông Thôn Nuôi Lợn/1_7"
    output_file = directory+"/merged.txt"
    merge_txt_files(directory, output_file)
    print(f"Files merged into {output_file}")
