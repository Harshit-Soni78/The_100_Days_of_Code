from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep edge open after the program finished
edge_browser = webdriver.EdgeOptions()
edge_browser.add_experimental_option("detach", True)

driver = webdriver.Edge()

driver.get("https://www.python.org/")

date_elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_element = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")

dates = [f"2024-{date.text}" for date in date_elements]
events = [event.text for event in event_element]

events_dict = {i: {dates[i]: events[i]} for i in range(len(events))}

print(events_dict)

driver.quit()  # quit the browser
