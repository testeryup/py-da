while(1):
    welcome = """Vui lòng chọn loại dữ liệu muốn scrape:
    1. Dữ liệu tổng hợp khách quốc tế theo tháng
    2. Dữ liệu tổng hợp theo phương tiện
    3. Dữ liệu theo quốc gia và vùng lãnh thổ"""
    print(welcome)
    str_input = input()
    
    if str_input == None or str_input == "":
        print("Kết thúc thôi!")
        break


