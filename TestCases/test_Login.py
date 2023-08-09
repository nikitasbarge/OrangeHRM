from PageObject.LoginPage import LoginHRM
from Utilities.Logger import LogGenerator


class Test_Login:
    log = LogGenerator.loggen()
    def test_Login_page_001(self, setup):
        self.log.info("Testcase test_Login_page_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.log.info("Page title is :" + self.driver.title)
        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_001Pass.png")
            self.driver.close()
            self.log.info("Testcase test_Login_page_001 is completed")
            assert True
        else:
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_001Fail.png")
            self.driver.close()
            self.log.info("Testcase test_Login_page_001 is failed")
            assert False

    def test_Login_page_002(self, setup):
        self.log.info("Testcase test_Login_page_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = LoginHRM(self.driver)
        self.log.info("Entering username")
        self.lp.Enter_Username("Admin")
        self.log.info("Entering password")
        self.lp.Enter_Password("admin123")
        self.log.info("Clicking login button")
        self.lp.Click_Login_Button()
        self.log.info("Checking login status")
        if self.lp.Check_Page_Title() == True:
            self.log.info("Login successively")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_002_Pass.png")
            self.log.info("Clicking menu button")
            self.lp.Click_Menu_Button()
            self.log.info("Clicking logout button")
            self.lp.Click_Logout_Button()
            self.log.info("Logout successively")
            self.log.info("Testcase test_Login_page_002 is completed")
            self.driver.close()
            assert True
        else:
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(
                "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_002_Fail.png")
            self.driver.close()
            self.log.info("Testcase test_Login_page_002 is failed")
            assert False

    # def test_Login_Page_002(self, setup):
    #     self.driver = setup
    #     self.lp = LoginHRM(self.driver)
    #     if self.lp.Check_Url_Logo() == True:
    #         self.driver.save_screenshot(
    #             "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_001_logo_pass.png")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(
    #             "D:\\automation testing\\PYCHARM\\OrangeHrmProject\\Screenshots\\test_Login_page_001_Logo_Fail.png")
    #         self.driver.close()
    #         assert False



