# 🏦 TEXO Hub - Trạm Điều Khiển Trung Tâm

Cổng kết nối tập trung cho tất cả các ứng dụng kỹ thuật tại Phòng Kỹ thuật TEXO.

## 🚀 Cách thêm ứng dụng mới vào Hub

Để thêm một ứng dụng mới vào danh sách hiển thị, Anh Vũ chỉ cần chỉnh sửa file `apps_config.json` theo mẫu sau:

```json
{
    "id": "ten_app_moi",
    "name": "Tên Ứng Dụng",
    "icon": "🚀",
    "description": "Mô tả ngắn gọn về tính năng.",
    "url": "Link_Online_Của_Anh",
    "local_url": "http://localhost:XXXX",
    "category": "Loại"
}
```

Sau khi lưu file, Hub sẽ tự động cập nhật giao diện mà không cần khởi động lại.

---
**Trưởng phòng:** Hoàng Đức Vũ
