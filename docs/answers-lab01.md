# Lab 01 – Câu hỏi thảo luận

## Câu 1. Vì sao sử dụng git mv?

Lệnh 'git mv' được sử dụng để di chuyển hoặc đổi tên các file đang được Git theo dõi, đồng thời tự động đưa thay đổi vào Staging Area.

Sử dụng 'git mv' giúp thao tác thuận tiện và dễ theo dõi hơn khi tái cấu trúc mã nguồn. Tuy nhiên, Git vẫn có thể nhận diện việc đổi tên file thông qua so sánh nội dung, ngay cả khi không sử dụng 'git mv'.

Trong bài thực hành, Git nhận diện 'cart.py' và 'dvd.py' được di chuyển vào thư mục 'aims/` với độ tương đồng 100%. Lệnh 'git log --follow' cho phép truy vết lịch sử của các file trước và sau khi di chuyển.

## Câu 2. 'release/lab01' có phải là baseline không?

Có. Trong phạm vi bài thực hành, 'release/lab01' được sử dụng làm baseline, tức là phiên bản cấu hình đã được xác định để nộp và kiểm tra.

Nhánh này được tạo từ 'master' sau khi hoàn thành Lab 01, giúp lưu giữ trạng thái mã nguồn tại thời điểm nộp bài.

Việc sử dụng baseline giúp quản lý phiên bản, kiểm tra lại kết quả và làm cơ sở đối chiếu khi dự án tiếp tục phát triển.

## Câu 3. Vì sao không commit trực tiếp vào 'master' dù làm việc một mình?

Không nên commit trực tiếp vào 'master' vì điều đó bỏ qua quy trình kiểm soát thay đổi.

Việc sử dụng nhánh riêng và Pull Request giúp:

- Tách biệt các thay đổi đang phát triển khỏi phiên bản chính.
- Kiểm tra mã nguồn trước khi tích hợp vào 'master'.
- Ghi nhận mục đích và lịch sử của từng thay đổi.
- Giảm nguy cơ đưa các thay đổi chưa được kiểm tra vào nhánh chính.

Ngay cả khi làm việc một mình, việc tuân thủ quy trình này vẫn giúp hình thành thói quen phát triển phần mềm chuyên nghiệp và đảm bảo khả năng truy vết thay đổi.