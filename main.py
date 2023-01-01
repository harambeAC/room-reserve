# from bs4 import BeautifulSoup
# import requests

url = 'https://libcal.dartmouth.edu/space/19054'
# html = requests.get(url)
# print(html.text)
# # soup = BeautifulSoup(html_doc, 'html.parser')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get(url)

# toggle to week view
elem = driver.find_element(By.CLASS_NAME, 'fc-resourceTimeGridWeek-button')
elem.click()

# toggle to next available
elem = driver.find_element(By.CLASS_NAME, 'fc-goToNextAvailable-button')
elem.click()

# "5:00pm 1/3/2023 - Berry 171A - Available"
# find the correct tile
elem=driver.find_element(by=By.XPATH, value="//a[@title='5:00pm 1/3/2023 - Berry 171A - Available']")
elem.click()


print(elem)

# driver.close()