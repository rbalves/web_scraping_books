from selenium import webdriver
from selenium.webdriver.firefox.options import Options


url = 'http://books.toscrape.com/'

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get(url)

ul = driver\
    .find_element_by_xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')\
    .find_elements_by_tag_name('li')

categories = []

for li in ul:
    categories.append(li.text)

print(categories)
