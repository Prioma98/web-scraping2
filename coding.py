import pandas
import requests
from bs4 import BeautifulSoup
book_page=requests.get('http://books.toscrape.com/')
soup=BeautifulSoup(book_page.content,'html.parser')
#print(arranged)


#variable needed to store
book_name=[]
price=[]
availability=[]

#store all the list items or all the books
all_product = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

#iterating over all the list to access the name price quantity
for items in all_product:
  name=items.h3.a.text
  book_name.append(name)

  prices=items.find('div',class_='product_price').p.text
  price.append(prices)

  #status=items.find('div',class_='product_price').find('p',class_='instock availability').i
  status="In stock"
  availability.append(status)

  total_dict=pandas.DataFrame(
    {
        'Book name':book_name,
        'Book price':price,
        'Status':availability

    })

print(total_dict)
total_dict.to_csv("Book_list_1.csv")