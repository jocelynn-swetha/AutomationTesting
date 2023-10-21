import time
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
#from selenium.webdriver.firefox.options import Options

#options = webdriver.firefoxOptions()
#options.add_experimental_option("detach", True)
service = Service("C:\\Users\\swthas\\Desktop\\Firefox Driver\\geckodriver.exe")
driver = Firefox(service=service)
driver.get("https://www.thetestingworld.com/testings/")

#validate maximize

driver.maximize_window()

#Enter the data into the textbox
driver.find_element('name','fld_username').send_keys('hello')
driver.find_element('xpath',"//input[@name='fld_email']").send_keys('testingworldindia@gmail.com')
driver.find_element('name','fld_password').send_keys('abcd123')
driver.find_element('name','fld_username').clear()
driver.find_element('name','fld_username').send_keys('abcd123')

# Working on Radio button
driver.find_element('xpath',"//input[@value='office']").click()

#  Work on Dropdown
obj = Select(driver.find_element('name',"sex"))
#obj.select_by_visible_text("Male")
#obj.select_by_value("2")
obj.select_by_index(1)

# Working on Checkbox
driver.find_element('name',"terms").click()

# Work on Button
driver.find_element('xpath',"//input[@type='submit']").click()

# Work on Links
driver.find_element('xpath',"//a[text()='Read Detail']").click()
#driver.close()




