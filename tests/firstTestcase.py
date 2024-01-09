import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.createProjectLocators import Locators

# Use Chrome options when creating the WebDriver
driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php")
# driver.find_element(By.NAME,"username").send_keys("Admin")
elements = driver.find_element("homeslider-container")


print(elements.text)