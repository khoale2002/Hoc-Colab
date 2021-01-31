#Đồ án Image Crawler (Web scarping)    LÊ ĐÌNH ĐĂNG KHOA
#Các thư viện cần sử dụng
import requests
from bs4 import BeautifulSoup
import urllib.request
import time

#url cần để lấy ảnh
url = 'https://www.nhc.noaa.gov/'

#Gửi yêu cầu từ client lên sever
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#Tìm tất cả các file ảnh
images = soup.find_all('img')

links = []

#Xử lý file ảnh
for img in images:
    link = img.get('src')
    if "data" not in link:
        if "https://" not in link:
            link = url + link
        print(link)
        links.append(link)
print("Số ảnh web có là: ", str(len(links)))


#Lưu số ảnh mong muốn
a = input("Số ảnh bạn muốn lấy: ")
if int(a) > len(links):
    print("Quá số ảnh web có:")
else:
# Bộ đếm thời gian bắt đầu
    start = time.time()
    for i in range(int(a)):
        #Nạo ảnh
        filename = "img{}.jpg".format(i)
        urllib.request.urlretrieve(links[i], filename)
#KẾt thúc đém giờ
    end = time.time()
#Thơi gian
    print("Thoi gian tai anh:",round(end - start,3))

print("Hoàn thành ")
