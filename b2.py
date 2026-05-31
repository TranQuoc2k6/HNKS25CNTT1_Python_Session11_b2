"""
* Phân tích 
- Dictionary employee gồm những key nào?
    + Gồm : employee_id, full_name, department, status
- Vì sao dòng sau gây lỗi?
employee_id = employee[0]
    + Vì employee_id là key trong dictionary chứ không phải list nên không thể truy cập
- Dictionary có truy cập phần tử bằng index giống list không?
    + dictionary không cho phép truy cập phần tử bằng index
- Muốn lấy mã nhân viên "NV001", cần viết lệnh như thế nào?
    + employee["employee_id"]
- Vì sao dòng sau gây lỗi?
full_name = employee["name"]
    + Vì key name không tồn tại trong dictionary
- Key đúng để lấy họ tên nhân viên là gì?
    + key đúng là "full_name"
- Vì sao dòng sau chưa cập nhật đúng trạng thái nhân viên?
employee["employee_status"] = "official"
    + vì không có key nào là employee_status trong dictionary, nên nó sẽ tạo ra một key mới trong dictionary có giá trị là official
- Muốn cập nhật trạng thái nhân viên, cần dùng key nào?
    + cần dùng key "status"
- Vì sao dòng sau gây lỗi?
employee.append("base_salary", 15000000)
    + Vì trong dictionary không tồn tại phương thức append()
- Dictionary có phương thức append() không?
    + Không
- Muốn thêm lương cơ bản base_salary bằng 15000000, cần viết lệnh như thế nào?
employee["base_salary"] = 15000000
- Vì sao dòng sau gây lỗi?
del employee["team"]
    + Vì không tồn tại key để xóa
- Muốn xóa thông tin phòng ban, cần dùng key nào?
    + dùng key "department"
"""


# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa phòng ban
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)