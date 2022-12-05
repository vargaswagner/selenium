from selenium import webdriver
import time

driver_path = r'/home/estudiante/Descargas/chrome/chromedriver_linux64 (1)/chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)

time.sleep(10)
driver.close()

time.sleep(10)
driver.quit()