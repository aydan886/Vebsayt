import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Amazon məhsul linki (misal üçün bir məhsul səhifəsi)
url = "https://www.amazon.com/dp/B08N5WRWNW"

# Saytı yükləyirik
response = requests.get(url, headers=headers)

# HTML kodu parse edirik
soup = BeautifulSoup(response.content, "html.parser")

# Məhsul adını tapırıq
title = soup.find(id="productTitle")
if title:
    print("Məhsul adı:", title.get_text(strip=True))
else:
    print("Məhsul adı tapılmadı.")

# Məhsul qiymətini tapırıq
price = soup.find("span", {"class": "a-offscreen"})
if price:
    print("Qiymət:", price.get_text(strip=True))
else:
    print("Qiymət tapılmadı.")
