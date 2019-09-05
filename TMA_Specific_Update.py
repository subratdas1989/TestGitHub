from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest
from pyunitreport import HTMLTestRunner

class TerminalConfigurationSpecificUpdate(unittest.TestCase):

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

        print("/////click on Terminal Management Menu /////")
        self.driver.find_element_by_xpath("//a[contains(text(),'Terminals management')]").click()
        print("/////clicks on Terminal Configuration Menu /////")
        self.driver.find_element_by_xpath("//span[text()='Terminals configuration']").click()
        print("/////Terminal Range Selected /////")
        selectRange = Select(self.driver.find_element_by_xpath("//select[@id='gamme']"))
        selectRange.select_by_visible_text('6xxxi')
        print("/////clicks on Expert Tab /////")
        self.driver.find_element_by_xpath("//a[contains(text(),' Expert ')]").click()
        print("/////Selecting sip backup proxy ip settings /////")
        self.driver.find_element_by_xpath("//td[text()='sip backup proxy ip']").click()
        print("/////selecting sip backup proxy IP Value as SPECIFIC /////")
        self.driver.find_element_by_xpath("//div[@id='TYPE8']//div[2]//table[1]//tbody[1]//tr[19]//td[7]//input[1]").click()
        print("/////Selecting sip backup registrar ip settings /////")
        self.driver.find_element_by_xpath("//td[text()='sip backup registrar ip']").click()
        print("selecting sip backup registrar ip value  as SPECIFIC !!!!!")
        self.driver.find_element_by_xpath("//div[@id='TYPE8']//div[2]//table[1]//tbody[1]//tr[20]//td[7]//input[1]").click()
        print("Save the Updated Settings !!!!!! :)")
        self.driver.find_element_by_xpath("//input[@value='Save']").click()
        print("Allocate values the global parameter")
        self.driver.find_element_by_xpath("//input[@value='Allocate']").click()
        print("Click on Yes Button")
        self.driver.find_element_by_xpath("/html/body/div[4]/a[1]").click()
        print("Modify the Specific Settings !!!!")
        self.driver.find_element_by_xpath("//a[contains(text(),'Modify specific settings')]").click()
        selectList = Select(self.driver.find_element_by_xpath("//select[@id='nomListe']"))
        selectList.select_by_visible_text('all')
        print("go to Expert Tab")
        self.driver.find_element_by_xpath("//a[contains(text(),' Expert ')]").click()
        print("Selecting  the sip backup proxy ip value !!!")
        self.driver.find_element_by_xpath("//input[@id='checksip backup proxy ip']").click()
        BackupProxyIP = self.driver.find_element_by_xpath("//input[@id='valsip backup proxy ip']")
        BackupProxyIP.send_keys(Keys.CONTROL + 'a')
        BackupProxyIP.send_keys(Keys.DELETE)
        BackupProxyIP.send_keys('10.211.216.166')

        print("Selecting  the sip backup registrar ip value !!!")
        self.driver.find_element_by_xpath("//input[@id='checksip backup registrar ip']").click()
        BackupProxyIP = self.driver.find_element_by_xpath("//input[@id='valsip backup registrar ip']")
        BackupProxyIP.send_keys(Keys.CONTROL + 'a')
        BackupProxyIP.send_keys(Keys.DELETE)
        BackupProxyIP.send_keys('10.211.216.166')

        print("Click on Save button")
        self.driver.find_element_by_xpath("//input[@value='Save']").click()
        print("Select all the terminals for Update")
        self.driver.find_element_by_xpath("//a[contains(text(),'Select all')]").click()

        print("click on validate Button to Proceed !!!!")
        self.driver.find_element_by_xpath("//input[@value='Validate']").click()
        print("click on Next to proceed")
        self.driver.find_element_by_xpath("//input[@value='Next']").click()
        print("Create Action clicked ")
        self.driver.find_element_by_xpath("//input[@name='creatAction']").click()

        print("Create Action Name")
        ActionName = self.driver.find_element_by_xpath("//input[@id='nomaction']")
        ActionName.send_keys('AutoSpecificUpdate')

        print("Click on Validate Button to Finish Update")
        self.driver.find_element_by_xpath("//input[@name='validateAction']").click()
        time.sleep(20)

        print("Check Event Log For Success or Failure result of action")
        self.driver.find_element_by_xpath("//a[contains(text(),'Actions follow-up')]").click()
        self.driver.find_element_by_xpath("//td[text()='TestGlobalAutomate']").click()
        print("clicks on Terminal Configuration Menu to unlock setting !!!!")
        self.driver.find_element_by_xpath("//span[text()='Terminals configuration']").click()
        print("Proceed for Unlock the allocation !!!")
        self.driver.find_element_by_xpath("//a[contains(text(),'Unlock the allocation')]").click()
        print("click on yes to Unlock allocation !!!!")
        self.driver.find_element_by_xpath("/html/body/div[4]/a[1]").click()
        print("Go to Web Admin Home Page !!!!")
        self.driver.find_element_by_xpath("//span[text()='Web Admin home']").click()
        print("Exited from Web Admin Browser")
        self.driver.quit()





    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        print ("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HTMLTestRunner(output="C:\\Users\\rioadmin\\PycharmProjects\\MV5000WebAutomation\\Report"))