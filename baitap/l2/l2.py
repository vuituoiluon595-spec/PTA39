# Khai báo lớp
class QuanLyDiemHS:
    def __init__(self, hoTen, lop, truong, diemToan, diemVan, diemAnh):
        self.hoTen = hoTen
        self.lop = lop
        self.truong = truong
        self.diemToan = diemToan
        self.diemVan = diemVan
        self.diemAnh = diemAnh

    # Hàm tính điểm trung bình
    def tinh_diem_tb(self):
        return (self.diemToan + self.diemVan + self.diemAnh) / 3


# Tạo danh sách học sinh
ds_hs = [
    QuanLyDiemHS("Lam", "10A1", "MindX", 8, 7, 9),
    QuanLyDiemHS("An", "10A2", "MindX", 9, 8, 9),
    QuanLyDiemHS("Binh", "10A3", "MindX", 9, 8, 9)
]

# Tìm điểm trung bình cao nhất
max_tb = 0
for hs in ds_hs:
    if hs.tinh_diem_tb() > max_tb:
        max_tb = hs.tinh_diem_tb()

# Lọc các học sinh có điểm cao nhất
hs_max = []
for hs in ds_hs:
    if hs.tinh_diem_tb() == max_tb:
        hs_max.append(hs)

# In kết quả
print("Học sinh có điểm trung bình cao nhất:")
for hs in hs_max:
    print("Tên:", hs.hoTen)
    print("Lớp:", hs.lop)
    print("Trường:", hs.truong)
    print("Điểm TB:", hs.tinh_diem_tb())
    print("-------------------")