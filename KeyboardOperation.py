from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service("C:\\Users\\swthas\\Desktop\\ChromeDriver\\chromedriver-win64\\chromedriver.exe")
driver = Chrome(options=options, service=service)
driver.get("http://www.theTestingWorld.com/testings")
driver.find_element('name',"fld_username").send_keys("Hello")
act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').perform()
