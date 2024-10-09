from selenium import  webdriver
from selenium.webdriver.common.by import By

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge()

driver.get("https://en.wikipedia.org/wiki/Main_Page")


number_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')

print(number_of_articles.text)

driver.quit()  # quit the browser
