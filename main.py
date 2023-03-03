import unittest
import register
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

AMAZON_COM_TR_URL         = "https://www.amazon.com.tr/"
TEST_EMAIL                = "beyzanurtitiz98@gmail.com"
CORRECT_PASSWORD          = "qaengineer01"
WELCOME_TEXT_NAME         = "Beyza"
WRONG_PASSWORD_ERROR_TEXT = "Şifreniz yanlış"

class AmazonComTRLogin(unittest.TestCase):

  def setUp(self):  
    self.driver = webdriver.Chrome()

  def go_to_login_page_helper(self):
    driver = self.driver
    driver.get(AMAZON_COM_TR_URL)
    time.sleep(3)
    login_button = driver.find_element(By.XPATH, '//*[@id="nav-signin-tooltip"]/a')
    login_button.click()
    email_input = driver.find_element(By.XPATH, '//*[@id="ap_email"]')
    email_input.send_keys(TEST_EMAIL)
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
  
  def test_login_with_correct_credentials(self):
    self.go_to_login_page_helper()
    driver = self.driver
    password_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    password_input.send_keys(CORRECT_PASSWORD)
    login_button = driver.find_element(By.XPATH, '//*[@id="auth-signin-button"]')
    login_button.click()
    time.sleep(3)
    welcome_text = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]')
    self.assertEqual(welcome_text.text, WELCOME_TEXT_NAME)
  
  def test_login_with_wrong_password(self):
    self.go_to_login_page_helper()
    driver = self.driver
    password_input = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
    password_input.send_keys('wrongpassword')
    login_button = driver.find_element(By.XPATH, '//*[@id="auth-signin-button"]')
    login_button.click()
    time.sleep(3)
    error_message = driver.find_element(By.XPATH, '//*[@id="auth-error-message-box"]/div/div/ul/li/span')
    error_message_text = error_message.text.strip()
    self.assertEqual(error_message_text, WRONG_PASSWORD_ERROR_TEXT)

  def tearDown(self):
    self.driver.close()

def main():
  print("---- Welcome to Amazon.com.tr login test script ----")
  print("Before starting login test, do you need an Amazon.com.tr account? 'y' or 'n'")
  need_amazon_account = input('> ')
  if need_amazon_account == 'y':
    register.create_account()

  unittest.main()

if __name__ == "__main__":
  main()