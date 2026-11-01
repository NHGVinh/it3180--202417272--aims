# Lab 02 – Câu hỏi thảo luận

## Câu 1. Vì sao phải đồng bộ master trước khi tạo Pull Request?

Đồng bộ với `master` giúp nhánh đang phát triển nhận được các thay đổi mới nhất từ nhánh chính.

Việc này giúp phát hiện và giải quyết xung đột sớm, đồng thời kiểm tra tính tương thích của tính năng mới với mã nguồn hiện tại trước khi tích hợp.

Trong bài thực hành, nhánh `feature/search-by-title` được kiểm tra và đồng bộ bằng `git fetch origin` và `git merge origin/master`.

## Câu 2. Khi nào không được rebase?

Không nên rebase các commit đã được chia sẻ và đang được người khác sử dụng, vì rebase có thể viết lại lịch sử commit và thay đổi mã SHA.

Điều này có thể gây khó khăn cho việc đồng bộ repository và tạo ra xung đột lịch sử.

Theo quy tắc của bài thực hành, chỉ nên viết lại lịch sử đối với các commit chưa được chia sẻ.

## Câu 3. Nhánh feature/* khác topic/* như thế nào?

- `feature/*`: Sử dụng để phát triển chức năng mới của phần mềm, ví dụ `feature/cart-print`, `feature/search-by-title`.
- `topic/*`: Sử dụng cho một công việc hoặc chủ đề cụ thể, thường liên quan đến tài liệu, cấu hình hoặc những thay đổi không trực tiếp bổ sung tính năng, ví dụ `topic/pr-template`, `topic/use-case-diagram`.

Cả hai loại nhánh đều được tạo từ `master` và tích hợp trở lại `master` thông qua Pull Request.