# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://www.google.com/")
    self.driver.set_window_size(923, 1033)
    self.driver.find_element(By.CSS_SELECTOR, ".FPdoLc").click()
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("python")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .tF2Cxc .LC20lb").click()
  
