import os
from PIL import Image

def convert_jpegs_to_pdf(directory_path, output_pdf_path):
    # Tìm tất cả các file JPEG trong thư mục
    jpeg_files = [f for f in os.listdir(directory_path) if f.endswith(".jpeg") or f.endswith(".jpg")]

    # Sắp xếp tên file để chúng được thêm vào PDF theo thứ tự
    jpeg_files.sort()

    # Tạo list chứa các hình ảnh
    images = []

    for jpeg_file in jpeg_files:
        image_path = os.path.join(directory_path, jpeg_file)
        image = Image.open(image_path)
        images.append(image)

    # Lưu list hình ảnh như một file PDF
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

if __name__ == "__main__":
    directory = "E:/dtruyen_watermark_remover/dtruyen_watermark_remover/remove_canvas_watermark_from_image/output"  # Thay thế path_to_directory bằng đường dẫn thực sự của bạn
    output_pdf = "E:/dtruyen_watermark_remover/dtruyen_watermark_remover/remove_canvas_watermark_from_image/output/output.pdf"
    convert_jpegs_to_pdf(directory, output_pdf)
    print(f"PDF created at {output_pdf}")
