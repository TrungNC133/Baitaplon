# Bài Tập Lớn Tự Động Hóa - Thu Thập Dữ Liệu BĐS từ Dothi.net 🏘️

Project Python sử dụng Selenium để tự động thu thập thông tin nhà đất tại Đà Nẵng từ trang [dothi.net](https://dothi.net), sau đó xuất dữ liệu ra file Excel.

---

## ✅ Chức năng chính

- Truy cập trang dothi.net và thực hiện tìm kiếm BĐS tự động.
- Chọn loại nhà đất là **Nhà mặt phố**, khu vực **Đà Nẵng**.
- Lấy thông tin từng bài đăng gồm: `Tiêu đề`, `Mô tả`, `Giá`, `Diện tích`, `Địa chỉ`, `Link`.
- Lưu toàn bộ dữ liệu thành file Excel `BDS_output.xlsx`.
- Thiết lập chạy tự động lúc **6h sáng mỗi ngày** bằng thư viện `schedule`.

---

## 📁 Cấu trúc thư mục

bai_tap_lon_tudonghoa/
├── baitaplon_chitrung.py
├── requirements.txt
└── README.md

Yêu cầu hệ thống
Python 3.8+
Google Chrome đã cài đặt
ChromeDriver tương ứng với phiên bản Chrome
Kết nối Internet

Hướng dẫn cài đặt
### 1. Clone project
git clone https://github.com/TrungNC133/bai_tap_lon_tudonghoa.git
cd bai_tap_lon_tudonghoa
