import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Zillow_Clone_Website = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = "https://forms.gle/VmA5nE1E2vQmvPUR6"
SPREADSHEET_LINK = ("https://docs.google.com/spreadsheets/d/1cDu0h7X56No4CgAYmyjLs7RpUjjY9MpxfysguiqIGzA/edit?usp=sharing")

response = requests.get(Zillow_Clone_Website)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

all_anchor_tags = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
links = [tag.get("href") for tag in all_anchor_tags]

# print(links)

all_address_tags = soup.find_all(name="address")
addresses = [tag.text.replace("\n", "").replace("|", "").strip(" ") for tag in all_address_tags]

# print(addresses)

price_tag = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices = [tag.getText().strip("+/mo").strip("+ 1bd") for tag in price_tag]

# print(prices)

# Keep edge open after the program finished
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

for n in range(len(links)):
    driver.get(FORM_LINK)
    time.sleep(2)
    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit_button.click()
    time.sleep(2)

driver.get(SPREADSHEET_LINK)
