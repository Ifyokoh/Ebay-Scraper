import pandas as pd
import requests

from bs4 import BeautifulSoup



def scrape_data(no_samples_to_scrape, keywords):
  data = {"category": [], "item_title": [], "item_price": [], "item_url": [], "item_image": []}
  for keyword in keywords:
    page_url = []
    for i in range(1,round((no_samples_to_scrape/203) + 1)):
        page_url.append('https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + keyword + '&_sacat=0&_ipg=192&_pgn=' + str(i))
    # details of the info from the website
    for links in page_url:
      print(links)
      response = requests.get(links)
      soup = BeautifulSoup(response.content, 'html.parser')

      
      for title in soup.find_all('h3', { 'class': 's-item__title' }):
        data["item_title"].append(title.text)
        data["category"].append(keyword)
      for price in soup.find_all('span', { 'class':"s-item__price" }):
        data["item_price"].append(price.text)
      for url_of_item in soup.find_all('a', { 'class': 's-item__link' }):
        data["item_url"].append(url_of_item.get('href'))
      for url_of_image in soup.find_all('img', { 'class': 's-item__image-img' }):
        data["item_image"].append(url_of_image['src'])
    page_url.clear()

  df = pd.DataFrame.from_dict(data, orient='index')
  return df.transpose()

