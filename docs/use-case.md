# Use Case – AIMS-mini

## 1. Tổng quan

AIMS-mini là ứng dụng quản lý giỏ hàng DVD, cho phép người dùng thêm, xóa, tìm kiếm và xem thông tin giỏ hàng.

## 2. Tác nhân

**Người dùng:** Người sử dụng ứng dụng AIMS-mini.

## 3. Danh sách Use Case

| Mã | Use Case | Mô tả |
|---|---|---|
| UC-01 | Thêm DVD | Thêm một DVD vào giỏ hàng |
| UC-02 | Xóa DVD | Xóa DVD khỏi giỏ hàng |
| UC-03 | Xem giỏ hàng | Hiển thị danh sách DVD |
| UC-04 | Tính tổng tiền | Tính tổng chi phí các DVD |
| UC-05 | Tìm kiếm DVD | Tìm DVD theo tên |

## 4. Sơ đồ Use Case

```mermaid
flowchart LR
    U["Người dùng"]
    A(["Thêm DVD"])
    B(["Xóa DVD"])
    C(["Xem giỏ hàng"])
    D(["Tính tổng tiền"])
    E(["Tìm kiếm DVD"])

    U --- A
    U --- B
    U --- C
    U --- D
    U --- E
```

## 5. Kết luận

Các Use Case mô tả những chức năng cơ bản của AIMS-mini, làm cơ sở để phát triển và kiểm thử các tính năng trong những bài lab tiếp theo.