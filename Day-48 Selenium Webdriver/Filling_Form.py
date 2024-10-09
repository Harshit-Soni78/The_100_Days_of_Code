from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep edge open after the program finished
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Click any element or link
# number_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# number_of_articles.click()

# Click any link by its name/text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "search" <input> by name
search = driver.find_element(By.NAME, value="search")
search.send_keys("Python", Keys.ENTER)
