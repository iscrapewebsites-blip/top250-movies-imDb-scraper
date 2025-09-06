# import undetected_chromedriver as uc
import time
from lxml import html
import json

# if __name__ == '__main__':
#      driver = uc.Chrome(headless=False, use_subprocess=False)
#      driver.get("https://www.imdb.com/chart/top/")
#      input('Clear Access..')
#      with open("page.html", 'w', encoding='utf-8') as f:
#           f.write(driver.page_source)
#      driver.quit()

#      time.sleep(10)

page = ''
with open('page.html', 'r', encoding='utf-8') as f:
     page = f.read()

tree = html.fromstring(page)


elems = tree.xpath('//div[contains(@class, "sc-15ac7568-0")]')
data = []
for elem in elems:
     title = elem.xpath('.//a/h3[contains(@class, "ipc-title__text")]')

     t = ''
     if title:
          t = title[0].text_content()
     else:
          pass

     year = ""
     hour = ""
     R = ""

     subs = elem.xpath('.//span[contains(@class, "sc-15ac7568-7")]')
     if subs:
          year = subs[0].text_content()
          if len(subs)>1:
               hour = subs[1].text_content()
          else:
               pass
          if len(subs)>2:
               R = subs[2].text_content()
          else:
               pass
     else:
          pass

     dict = {}
     dict['title'] = t
     dict['year'] = year
     dict['hour'] = hour
     dict['Rated'] = R

     data.append(dict)

# from list of dict to json
data_str = json.dumps(data)
with open('output.json', 'w', encoding='utf-8') as f:
     f.write(data_str)