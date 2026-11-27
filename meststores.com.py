# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import csv

# driver = webdriver.Chrome()


# for pages in range (2,3) :
#     driver.get(f"https://meststores.com/product-category/printers/page/{pages}")
#     pig_container = driver.find_element(By.XPATH , '//div[contains(@class , "porto-posts-grid")]')

#     # print(pig_container.get_attribute("outerHTML"))
#     # if "Zebra ZD220T Thermal Transfer Desktop Label Printer" in pig_container.text:
#     #     print("Product found")
#     # else:
#     #     print("Product not found")

    
#     discription = pig_container.find_element(By.XPATH , './/h3[contains(@class , "porto-heading")]').text
#     print(discription)

# ======================================
# beautifulsoup
# ======================================

import requests
from bs4 import BeautifulSoup
import csv

all_products = []

for pages in range (1,11) :
    url = f"https://meststores.com/product-category/printers/page/{pages}/"
    print("👉👉👉 page :" , pages)
    open_page = requests.get(url)
    # print(open_page)
    soup = BeautifulSoup(open_page.text , "html.parser")
    # print(soup)

    pig_container = soup.find("div" , class_="posts-wrap products-container products has-ccols ccols-sm-3 ccols-2 has-ccols-spacing")
    # print(pig_container)

    # if "HP Laser MFP 137fnw Mono Laser Multi-Function Printer – Wireless, ADF, 20 ppm (4ZB84A) + Azhar A4 Paper 80gsm 1 Ream" in pig_container.text :
    #     print("found")
    # else:
    #     print("not found")

    container = pig_container.find_all("div" , class_="porto-section product-type-advanced p-0")
    for item in container:
        description = item.find("h3" , class_="porto-heading porto-gb-609569037b9abfd6854d6b3c2b5e7311 post-title").text
        print("description :" , description)

        price = item.find_all("span" , class_="woocommerce-Price-amount amount")[1].text
        print("price :" , price)

        discount = item.find_all("span" , class_="woocommerce-Price-amount amount")[0].text
        print("discount :" , discount)

        rating = item.find("strong" , class_="rating").text
        print("rating :" , rating)

        product_link = item.find("a" , {"aria-label" : "post content"})["href"]
        print("product_link :" , product_link)

        product_img = item.find("img")["src"]
        print("product_img :" , product_img)

        print("="*20)

        dict_products = {
            "description" : description ,
            "price" : price ,
            "discount" : discount ,
            "rating" : rating ,
            "product_link" : product_link ,
            "product_img" : product_img ,
        }
        all_products.append(dict_products)

header = all_products[0].keys()
path = "all products.csv"

with open (path , "w" , encoding="utf-8" , newline="") as file :
    writer = csv.DictWriter(file , header)
    writer.writeheader()
    writer.writerows(all_products)


