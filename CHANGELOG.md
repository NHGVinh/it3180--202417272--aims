
# Changelog

Tài liệu này ghi nhận những thay đổi quan trọng của AIMS-mini qua các phiên bản.

## [Unreleased]

## [1.1.0] - 2026-11-01

### Added
- Bổ sung phương thức `sort_by_title()` để sắp xếp DVD theo tên.
- Bổ sung phương thức `sort_by_cost()` để sắp xếp DVD theo giá.
- Bổ sung chức năng `search_by_category()` để tìm kiếm DVD theo danh mục.
- Bổ sung unit test cho chức năng sắp xếp và tìm kiếm theo danh mục.

## [1.0.0] - 2026-11-01

### Added
- Bổ sung phương thức `Cart.print_cart()` để hiển thị thông tin giỏ hàng.
- Bổ sung chức năng tìm kiếm DVD theo tên bằng `search_by_title()`.
- Bổ sung chức năng tính tổng tiền sau giảm giá bằng `total_cost_with_discount()`.
- Bổ sung thông báo tiếng Việt khi thêm DVD vào giỏ hàng.
- Bổ sung unit test cho giới hạn giỏ hàng và chức năng giảm giá.
- Bổ sung Pull Request Template và tài liệu Use Case.

### Changed
- Chuẩn hóa quy trình phát triển bằng Pull Request.
- Hoàn tác tính năng hiển thị tên DVD khi thêm vào giỏ hàng (PR #16).

### Fixed
- Sửa lỗi giỏ hàng chấp nhận DVD thứ 21 mặc dù giới hạn là 20 (Issue #11).
- Sửa công thức tính số tiền sau giảm giá.
- Bổ sung kiểm tra phần trăm giảm giá hợp lệ trong khoảng 0–100.
