time_str = input("Nhập thời gian (hh:mm:ss): ")

parts = time_str.split(":")

if len(parts) == 3:
    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        print("Hợp lệ")
    else:
        print("Không hợp lệ")
else:
    print("Không hợp lệ")