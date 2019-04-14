import requests  
from bs4 import BeautifulSoup  
result = requests.get('http://www.c-sharpcorner.com/')  
print (result.status_code)  
print (result.headers)  
csharpcorner = result.content  
scrap = BeautifulSoup(csharpcorner,'html.parser')  
post = scrap.find_all("div",attrs={'class':'post'})  
for posts in post:  
    postBody = posts.find_all('div',attrs={'class':'media-body'})  
    for i in range(len(postBody)):  
      print (postBody[i].find('a', attrs={'class':'title'}).string.strip())
      print ('Category: ',postBody[i].find('a', '').string.strip())
      print ('By: ',postBody[i].find('a', attrs={'class':'author'}).string.strip())
      print ('Date and Time: ',postBody[i].find('span','hidden-xs').string.strip() )
      print ('----------------------------------------------------------------------------------------------')