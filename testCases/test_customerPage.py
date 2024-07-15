import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random



class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("*************Test_003_AddCustomer****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***********Login Successfull**************")
        self.logger.info("**********Starting Add Customer Test*************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(2)
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("*********Adding Customer Information***********")
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        #self.addcust.setCustomerRoles("Guests")
        #self.addcust.setManagerOFVendor("Vendor 2")
        self.addcust.selectGender("Male")
        self.addcust.setFirstName("Shivakumar")
        self.addcust.setLastName("Mp")
        self.addcust.setDob("8/09/1996")
        self.addcust.setCompanyName("HLT")
        self.addcust.setAdminContent("This is for testing...")
        self.addcust.clickOnSave()

        self.logger.info("***********Saving Customers Info************")
        self.logger.info("********Add Customer Validation Started*********")

        self.msg=self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)

        if "customer has been added successfully." in self.msg:
            assert True == True
            self.logger.info("********Add Customer Test Passed**********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert True == False

        self.driver.close()
        self.logger.info("********Ending Add Customer Test*********")

    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))
