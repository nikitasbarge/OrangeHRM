from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginHRM:
    Check_URL_Logo = (By.XPATH, "//div[@class='orangehrm-login-logo']//img[@alt='orangehrm-logo']")
    Text_Username_Xpath = (By.XPATH, "//input[@placeholder='Username']")
    Text_Password_Xpath = (By.XPATH, "//input[@placeholder='Password']")
    Click_Login_Xpath = (By.XPATH, "//button[@type='submit']")
    Check_Page_Title_Xpath = (By.XPATH, "//img[@alt='client brand banner']")
    Click_Menu_Button_Xpath = (By.XPATH, "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Click_Logout_Xpath = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Username_Xpath))
        self.driver.find_element(*LoginHRM.Text_Username_Xpath).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Text_Password_Xpath))
        self.driver.find_element(*LoginHRM.Text_Password_Xpath).send_keys(password)

    def Click_Login_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Login_Xpath))
        self.driver.find_element(*LoginHRM.Click_Login_Xpath).click()

    def Check_Page_Title(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.Check_Page_Title_Xpath))
            self.driver.find_element(*LoginHRM.Click_Menu_Button_Xpath)
            return True
        except:
            return False

    def Click_Menu_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.Click_Menu_Button_Xpath))
        self.driver.find_element(*LoginHRM.Click_Menu_Button_Xpath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*LoginHRM.Click_Logout_Xpath).click()

    # def Check_Url_Logo(self):
    #     try:
    #         self.driver.find_element(*LoginHRM.Check_URL_Logo)
    #         return True
    #     except:
    #         return False
