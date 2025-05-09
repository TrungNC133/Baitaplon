import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule

def chon_thongtin_timkiem(trinh_duyet):
    WebDriverWait(trinh_duyet, 10).until(EC.element_to_be_clickable((By.ID, "cboCate"))).click()
    time.sleep(3)
    danh_sach = trinh_duyet.find_element(By.CSS_SELECTOR, "#cboCate .gridcontainer ul")
    danh_sach.find_element(By.CSS_SELECTOR, "li[rel='163']").click()

    time.sleep(3)
    trinh_duyet.find_element(By.ID, "select2-ddlCity-container").click()
    time.sleep(2)
    thanh_pho = trinh_duyet.find_element(By.XPATH, "//li[contains(@id,'-DDN') and text()='Đà Nẵng']")
    thanh_pho.click()

    time.sleep(2)
    trinh_duyet.find_element(By.ID, "ContentPlaceHolder1_BoxSearch1_lbtSearch").click()


def lay_du_lieu():
    # 1. Truy cập trang web.
    trinh_duyet = webdriver.Chrome()
    trinh_duyet.get("https://dothi.net/")
    WebDriverWait(trinh_duyet, 15)

    # 2-3. Chọn loại BĐS + tỉnh thành + tìm kiếm.
    chon_thongtin_timkiem(trinh_duyet)
    time.sleep(3)

    ket_qua = []
    so_trang = 1

    # 4. Lấy tất cả dữ liệu(Tiêu đề, Mô tả, Hình ảnh, Nội dung bài viết) hiển thị ở bài viết
    # 5. Lấy tất cả dữ liệu của các trang
    while True:
        url = f"https://dothi.net/ban-nha-rieng-da-nang/p{so_trang}.htm"
        trinh_duyet.get(url)
        time.sleep(2)

        bai_viet = trinh_duyet.find_elements(By.CLASS_NAME, "vip-5-highlight")
        if not bai_viet:
            print("Đã duyệt hết các trang.")
            break

        for bv in bai_viet:
            try:
                tieu_de = bv.find_element(By.CLASS_NAME, "vip5").get_attribute("title").strip()
                lien_ket = bv.find_element(By.CLASS_NAME, "vip5").get_attribute("href")

                gia = bv.find_element(By.CSS_SELECTOR, ".price").text.strip() if bv.find_elements(By.CSS_SELECTOR, ".price") else "Không rõ"
                dientich = bv.find_element(By.CSS_SELECTOR, ".area").text.strip() if bv.find_elements(By.CSS_SELECTOR, ".area") else "Không rõ"
                diachi = bv.find_element(By.CSS_SELECTOR, ".location").text.strip() if bv.find_elements(By.CSS_SELECTOR, ".location") else "Không rõ"

                trinh_duyet.get(lien_ket)
                time.sleep(2)
                mo_ta = trinh_duyet.find_element(By.CLASS_NAME, "pd-desc-content").text.strip() if trinh_duyet.find_elements(By.CLASS_NAME, "pd-desc-content") else "Không có mô tả"
                trinh_duyet.back()

                ket_qua.append({
                    "TieuDe": tieu_de,
                    "MoTa": mo_ta,
                    "Gia": gia,
                    "DienTich": dientich,
                    "DiaChi": diachi,
                    "Link": lien_ket
                })

                print(f"[+] {tieu_de}")
            except Exception as err:
                print("Lỗi khi xử lý bài đăng:", err)
                continue

        so_trang += 1

    trinh_duyet.quit()

    # 6. Xuất dữ liệu ra file excel
    pd.DataFrame(ket_qua).to_excel("BDS_output.xlsx", index=False)
    print("✅ Xuất dữ liệu thành công!")


# 7. Thiết lập lịch chạy lúc 6h sáng hàng ngày
schedule.every().day.at("06:00").do(lay_du_lieu)

if __name__ == "__main__":
    lay_du_lieu()  # chạy ngay lần đầu
    while True:
        schedule.run_pending()
        time.sleep(10)
