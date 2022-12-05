from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver_path = r'/home/estudiante/Descargas/chrome/chromedriver_linux64 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element('name', 'name').send_keys('Wagner VArgas Challa')
driver.find_element('name', 'email').send_keys('wagner.vargas@gmail.com')
driver.find_element('id', 'exampleInputPassword1').send_keys('123456')

elementcss = driver.find_element(By.ID, 'exampleCheck1').click()

gender = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
option = gender.options

for index in range(0, len(option) -1):
    gender.select_by_index(1)


estatus1 = driver.find_element(By.ID, 'inlineRadio1')
estatus2 = driver.find_element(By.ID, 'inlineRadio2')
estatus2.click()

driver.find_element('name', 'bday').send_keys('12/12/2020')

driver.find_element(By.XPATH, '//input[@class="btn btn-success"]').click()

time.sleep(10)
driver.close()

time.sleep(10)
driver.quit()

