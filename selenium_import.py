from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

driver = webdriver.Firefox()
# open URI
driver.get("https://awsacademy.instructure.com")
# wait until selenium find button
wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn")))

# click button
btn = driver.find_element(By.CLASS_NAME, "btn")
btn.click()

# Wait until Selenium find input_field
wait.until(EC.presence_of_element_located((By.ID, "pseudonym_session_unique_id")))

# input username & password
user_input_field = driver.find_element(By.ID, "pseudonym_session_unique_id")
password_input_field = driver.find_element(By.ID, "pseudonym_session_password")

user_input_field.send_keys(username)
password_input_field.send_keys(password)

# Click Login Button
driver.find_element(By.CLASS_NAME, "Button--login").click()

# Wait until Selenium find Learner Lab Clickable Text
clickable_link = (By.CLASS_NAME, "ic-DashboardCard__header_content")
wait.until(EC.element_to_be_clickable(clickable_link))
driver.find_element(clickable_link[0], clickable_link[1]).click()

# Wait for module link
module_link = (By.CLASS_NAME, "modules")
wait.until(EC.element_to_be_clickable(module_link))
driver.find_element(module_link[0], module_link[1]).click()

# Wait for Learner Lab link
learner_lab = (By.XPATH, "//a[@title='Learner Lab']")
wait.until(EC.presence_of_element_located(learner_lab))
driver.find_element(learner_lab[0], learner_lab[1]).click()

# Switch from driver to iframe
wait.until(EC.presence_of_element_located((By.ID, "tool_content")))
frame = driver.find_element(By.ID, "tool_content")
driver.switch_to.frame(frame)

# Wait for Start Lab Button
start_lab = (By.ID, "launchclabsbtn")
wait.until(EC.presence_of_element_located(start_lab))
driver.find_element(start_lab[0], start_lab[1]).click()