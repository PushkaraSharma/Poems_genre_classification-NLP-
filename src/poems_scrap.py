import bs4
import urllib.request as url
from selenium import webdriver
import csv
import time

browser = webdriver.Chrome(executable_path='C:\\Users\\dell\\Desktop\\chromedriver.exe')
list_of_poems_no = ['88','20','65','45']

for k in list_of_poems_no:

    for i in range(1,35):
        time.sleep(1)
        browser.implicitly_wait(2)
        list = []
        url_id = 'https://www.poetryfoundation.org/poems/browse#page='+str(i)+'&sort_by=recently_added&topics='+k
        browser.get(url_id)
        hrefs =[]
        elem1 = browser.find_elements_by_xpath('//a[@href]')
        for elem in elem1:
            a = (elem.get_attribute("href"))
            c ='https://www.poetryfoundation.org/poetrymagazine/poems/'
            if c in a:
                hrefs.append(a)

        for href in hrefs:
            browser.implicitly_wait(2)
            browser.get(href)
            #browser.get('https://www.poetryfoundation.org/poetrymagazine/poems/144369/in-the-kitchen-59bc02224ce1e')
            elem2 = browser.find_element_by_tag_name('h1').text
            name = elem2
            #print(elem2)
            elem3 = browser.find_element_by_class_name('c-feature-bd').text
            text = (elem3)
            category = None
            if k =='88':
                category ='Mythology and Folklore'
            elif k =='45':
                category = 'Nature'
            elif k=='65':
                category='Art and Science'
            elif k == '20':
                category = 'Love'
            list.append((name,text,category))
            print(list)

        with open("poem_data.csv", "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(list)