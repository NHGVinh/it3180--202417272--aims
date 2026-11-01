# Lab 03 – Câu hỏi thảo luận

## Câu 1. Merge base là gì?

Merge base là commit tổ tiên chung tốt nhất giữa hai nhánh trong lịch sử Git. Git sử dụng merge base để xác định trạng thái gốc khi so sánh và tích hợp các thay đổi.

Trong quá trình merge, Git thực hiện so sánh ba phía (three-way merge):

- Phiên bản tại merge base.
- Phiên bản hiện tại của nhánh đang đứng (HEAD).
- Phiên bản của nhánh được merge vào.

Nếu hai nhánh thay đổi cùng một vùng mã nguồn theo những cách không tương thích, Git có thể phát sinh merge conflict và yêu cầu người phát triển giải quyết thủ công.

Trong Lab 03, hai nhánh `feature/vietnamese-messages` và `feature/show-added-title` cùng thay đổi thông báo khi thêm DVD. Vì vậy, khi merge đã xuất hiện xung đột trong `aims/cart.py`.

## Câu 2. Vì sao phải dùng revert trên master/release/* thay vì reset?

Vì `master` và `release/*` là các nhánh chia sẻ, được sử dụng để quản lý phiên bản và lưu giữ lịch sử thay đổi của dự án.

`git reset` có thể dịch chuyển con trỏ nhánh về commit trước đó, làm thay đổi lịch sử. Nếu sử dụng trên các commit đã chia sẻ, thao tác này có thể gây mất đồng bộ giữa các thành viên và ảnh hưởng đến khả năng truy vết.

Ngược lại, `git revert` tạo một commit mới để đảo ngược thay đổi mà không xóa hoặc viết lại các commit trước đó.

Trong Lab 03, chúng ta sử dụng `git revert -m 1 cb35ade` để hoàn tác PR #16. Git tạo commit `8158505`, trong khi commit merge ban đầu `cb35ade` vẫn được giữ nguyên.

Vì vậy, revert là phương pháp phù hợp hơn để hoàn tác những thay đổi đã được tích hợp vào các nhánh dùng chung, giúp bảo toàn lịch sử và hỗ trợ kiểm toán cấu hình.