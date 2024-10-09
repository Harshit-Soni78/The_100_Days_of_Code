from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep edge open after the program finished
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.XPATH, value='/html/body/form/button')

f_name.send_keys("Harshit")
l_name.send_keys("Soni")
email.send_keys("example@gmail.com")
submit.send_keys(Keys.ENTER)

# driver.close()  # close particular tab
# driver.quit()  # quit the browser
