from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest
from pyunitreport import HTMLTestRunner

class TMAGlobalUpdateDeferredAction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False
        cls.driver = webdriver.Firefox(capabilities=cap,
                                   executable_path="C:\\Users\\rioadmin\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\geckodriver.exe")
    def testCase(self):

        self.driver.get("https://admin:admin@10.211.216.166/rhm")
        self.driver.maximize_window()
        time.sleep(20)


        ######Get Current System Time ############
        self.driver.find_element_by_xpath("//a[contains(text(),'Telephony service')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'System ')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Info ')]").click()
        self.driver.find_element_by_xpath("//a[contains(text(),'Date and time ')]").click()
        self.driver.switch_to.frame('fenetre')
        Date = self.driver.find_element_by_xpath("//input[@id='m4263_p29337']").get_attribute("value")
        Time = self.driver.find_element_by_xpath("//input[@id='m4263_p29338']").get_attribute("value")
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("//a[contains(text(),'Web Admin home')]").click()
        print("/////click on Terminal Management Menu /////")
        self.driver.find_element_by_xpath("//a[contains(text(),'Terminals management')]").click()
        print("/////clicks on Terminal Configuration Menu /////")
        self.driver.find_element_by_xpath("//span[text()='Terminals configuration']").click()
        print("/////Terminal Range Selected /////")
        selectRange = Select(self.driver.find_element_by_xpath("//select[@id='gamme']"))
        selectRange.select_by_visible_text('6xxxi')
        print("/////clicks on Expert Tab /////")
        self.driver.find_element_by_xpath("//a[contains(text(),' Expert ')]").click()
        print("/////Selecting Web Interface enabled settings /////")
        self.driver.find_element_by_xpath("//td[text()='web interface enabled']").click()
        print("/////selecting Web Interface Value as GLOBAL /////")
        self.driver.find_element_by_xpath("//div[2]//table[1]//tbody[1]//tr[44]//td[5]//input[1]").click()
        print("/////Selecting Secure Web Service settings /////")
        self.driver.find_element_by_xpath("//td[text()='secure web service']").click()
        print("selecting Secure Web Service value  as GLOBAL !!!!!")
        self.driver.find_element_by_xpath("//div[2]//table[1]//tbody[1]//tr[45]//td[5]//input[1]").click()
        print("Save the Updated Settings !!!!!! :)")
        self.driver.find_element_by_xpath("//input[@value='Save']").click()
        print("Allocate values the global parameter")
        self.driver.find_element_by_xpath("//input[@value='Allocate']").click()
        print("Click on Yes Button")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[4]/a[1]").click()
        print("Modify the Global Settings !!!!")
        self.driver.find_element_by_xpath("//a[contains(text(),'Modify global settings')]").click()
        print("Go to Expert Tab")
        self.driver.find_element_by_xpath("//a[contains(text(),' Expert ')]").click()
        print("Updating the Web Interface Enabled value !!!")
        self.driver.find_element_by_xpath("//th[text()='web interface enabled']").click()
        print("Checked the Web Interface Enabled button")
        self.driver.find_element_by_xpath("//input[@name='valweb interface enabled']").click()
        print("Updating the Secure Web Service value !!!")
        self.driver.find_element_by_xpath("//th[text()='secure web service']").click()
        print("UnChecked the Secure Web Service button")
        self.driver.find_element_by_xpath("//input[@name='valsecure web service']").click()
        print("click on Next Button to Proceed !!!!")
        self.driver.find_element_by_xpath("//input[@value='Next']").click()
        print("Give the Action Name to validate ")
        ActionName = self.driver.find_element_by_xpath("//input[@name='nomaction']")
        ActionName.send_keys('DeferredGlobalAuto')
        print("Current Date of PBX is:", Date)
        List1 = Date.split('/')
        print(List1)
        InputDate = List1[1] + List1[0] + List1[2]
        print("Current time of PBX is: ", Time)
        List = Time.split(':')
        print(List)
        print("Select Update Type as Delayed and provide date and time")
        self.driver.find_element_by_xpath("//input[@value='1']").click()
        dateEntry = self.driver.find_element_by_xpath("//input[@value='__/__/____']")
        dateEntry.send_keys(str(InputDate))
        hourEntry = self.driver.find_element_by_xpath("//input[@id='hourOfAction']")
        hourEntry.click()
        HR = int(List[0])
        hourEntry.send_keys(str(HR))
        MinEntry = self.driver.find_element_by_xpath("//input[@id='minuteOfAction']")
        MinEntry.click()
        MM = int(List[1]) + 2
        MinEntry.send_keys(str(MM))
        print("Scheduled Update time at:", HR,":" , MM)
        print("Click on Validate Button to Finish Update")
        self.driver.find_element_by_xpath("//input[@name='validateAction']").click()
        print("Check Event Log For Success or Failure result of action")
        time.sleep(140)
        self.driver.find_element_by_xpath("//a[contains(text(),'Actions follow-up')]").click()
        self.driver.find_element_by_xpath("//td[text()='DeferredGlobalAuto']").click()
        print("clicks on Terminal Configuration Menu to unlock setting !!!!")
        self.driver.find_element_by_xpath("//span[text()='Terminals configuration']").click()
        print("Proceed for Unlock the allocation !!!")
        self.driver.find_element_by_xpath("//a[contains(text(),'Unlock the allocation')]").click()
        print("click on yes to Unlock allocation !!!!")
        self.driver.find_element_by_xpath("/html[1]/body[1]/div[4]/a[1]").click()
        print("Go to Web Admin Home Page !!!!")
        self.driver.find_element_by_xpath("//span[text()='Web Admin home']").click()
        print("Exited from Web Admin Browser")
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="C:\\Users\\rioadmin\\PycharmProjects\\MV5000WebAutomation\\Report"))