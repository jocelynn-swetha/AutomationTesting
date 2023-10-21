from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service("C:\\Users\\swthas\\Desktop\\ChromeDriver\\chromedriver-win64\\chromedriver.exe")
driver = Chrome(options=options, service=service)
driver.get("http://www.theTestingWorld.com")
act = ActionChains(driver)

# Click operation
# act.click().perform()
# act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# Context Click(Right Click)
# act.context_click().perform()
# act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

# act.double_click().perform()
# act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

act.move_to_element(driver.find_element('xpath',"//span[contains(text(),'TUTORIAL')]")).perform()