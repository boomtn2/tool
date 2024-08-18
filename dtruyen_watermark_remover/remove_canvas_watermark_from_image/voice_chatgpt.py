def split_string_at_sentence_end(input_string, max_chunk_size):
    chunks = []
    start = 0
    while start < len(input_string):
        # Tìm vị trí của dấu chấm gần 1000 ký tự kế tiếp
        end = input_string.rfind('.', start, start + max_chunk_size + 1)
        if end == -1:
            # Nếu không tìm thấy dấu chấm, chọn ngắt ở vị trí max_chunk_size
            end = start + max_chunk_size
            if end > len(input_string):
                end = len(input_string)
        else:
            # Cộng thêm 1 để bao gồm dấu chấm vào trong chuỗi
            end += 1
        
        # Thêm đoạn văn bản vào danh sách
        chunks.append(input_string[start:end])
        start = end
    
    return chunks

# Chuỗi ban đầu
original_string = """“Vì này phiến đại lục an bình, ta Long Thí Thiên có thể trả giá hết thảy, cho dù là chính mình sinh mệnh cũng không tiếc!” Vẻ mặt chính nghĩa thiếu niên tay cầm lợi kiếm đứng ở lộng lẫy thủy tinh dưới đèn, hắn thân khoác kim sắc chiến bào, khuôn mặt tuấn mỹ, một đôi mắt gắt gao trừng hướng trước mặt hắn nam nhân, toát ra thực cốt hận ý, nhưng mơ hồ lại lộ ra một chút sợ hãi.

Chỉ sợ liền chính hắn cũng không biết, liền tính là đã khám phá Võ Thánh chi cảnh, thành này trên đại lục duy nhất tôn giả, hắn lại vẫn là bản năng sợ hãi trước mặt người này.

Ngồi ng·ay ngắn ở màu đen vương tọa thượng anh tuấn nam tử mặt vô b·iểu t·ình mà nhìn về phía hắn, thần thái cao ngạo thanh quý, thon dài năm ngón tay đáp ở được khảm mỹ lệ Hồng Bảo Thạch trên tay vịn, móng tay mượt mà, tu bổ đến cực kỳ san bằng.

Hắn khoác kiện màu đen áo gấm, quá dài vạt áo kéo trên mặt đất, cũng không có cái gì quá nhiều trang trí, thêu công lại cực kỳ tinh mỹ, mỗi một tấc đều dùng ám kim sắc sợi tơ phác hoạ hoa văn, từ đai lưng đến y khấu đều bị để lộ ra xa hoa xa hoa lãng phí hơi thở.

Làn da thực bạch, bạch đến gần như trong suốt, mang theo cổ xưa quý tộc đặc có hơi thở, ở hắc y làm nổi bật hạ càng là oánh oánh như nguyệt, da bạch tựa ngọc.

Mắt là đen như mực màu sắc, hơi hơi thượng chọn mắt đào hoa, nhìn về phía ngươi khi lạnh băng đến xương, phảng phất trước mặt chỉ là cái vật ch·ết.

Rối tung ở hai vai biến thành màu đen đến cùng tơ lụa giống nhau, đơn điệu hắc bạch hai sắc phản chiếu người nam nhân này càng thêm quạnh quẽ mê người.

Không sai, vị này hắc y mỹ nam chính là Huyền Thiên Đại Lục mạnh nhất Boss, Mặc Nguyệt Yển, Mặc gia ngàn năm khó được một ngộ thiên tài.

Thân phụ ám hắc hệ ma pháp nguyên tố, thiên phú vượt xa người thường, hậu thế bất dung, một cái chớp mắt nhập ma, sát phụ thí mẫu, trong một đêm tàn sát sạch sẽ Mặc gia trên dưới mấy trăm khẩu người lãnh tâm quạnh quẽ vô ái vô dục cường đại vô cùng giai đoạn trước bá chủ.

Đương nhiên, cũng là vai chính Long Thí Thiên đánh quái thú tìm linh đan diệu dược thu mỹ nữ kiến hậu cung trên đường lớn nhất chướng ngại vật, tuy rằng cuối cùng kết cục khẳng định là đến bị pháo hôi.

Nhưng Mặc Nguyệt Yển Boss giống như là vì vai chính trưởng thành mà tồn tại, mỗi lần lên sân khấu đều là các loại huyễn khốc cuồng bá túm, lấy không ai bì nổi tư thái đem trưởng thành kỳ vai chính đạp lên dưới chân."""  # Thay thế bằng chuỗi của bạn

# Chia chuỗi thành các đoạn kết thúc bằng dấu chấm
max_chunk_size = 1000
chunks = split_string_at_sentence_end(original_string, max_chunk_size)

# In kết quả ra màn hình
for index, chunk in enumerate(chunks):
    print(f"Chunk {index + 1}: {chunk}")
