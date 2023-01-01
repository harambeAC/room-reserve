# from bs4 import BeautifulSoup
# import requests

url = 'https://libcal.dartmouth.edu/space/19054'
# html = requests.get(url)
# print(html.text)
# # soup = BeautifulSoup(html_doc, 'html.parser')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def connect():
    driver = webdriver.Firefox()
    driver.get(url)

    # toggle to week view
    elem = driver.find_element(By.CLASS_NAME, 'fc-resourceTimeGridWeek-button')
    elem.click()

    # toggle to next available
    elem = driver.find_element(By.CLASS_NAME, 'fc-goToNextAvailable-button')
    elem.click()
    return driver

driver = connect()

# TODO: config room
room = "Berry 171A"

# example title attr
# 5:00pm 1/3/2023 - Berry 171A - Available

# TODO: set up a mechanism to add more of thse days
for day in ['1/3/2023', '1/4/2023']:
    # TODO: write a config through the times in day
    for t in ["5:00pm", "5:30pm", "6:00pm"]:

        title = f"{t} {day} - {room} - Available"
        print(f"clicking: {title}")

        # click the correct tile
        elem = driver.find_element(by=By.XPATH, value=f"//a[@title='{title}']")
        elem.click()

# driver.close()