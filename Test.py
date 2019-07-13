import HtmlTestRunner
import unittest
from selenium import webdriver

class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"D:\Drive\chromedriver.exe")
        self.driver.implicitly_wait(1)

    def test_user_login_in_mail_box(self):
        driver = self.driver
        driver.get("https://runday.org/ua/")
        login_field = driver.find_element_by_id("wpcrl_username")
        login_field.send_keys("pinkangelssugar@gmail.com")
        password_field = driver.find_element_by_id("wpcrl_password")
        password_field.send_keys("Flylucky22!")
        button_login = driver.find_element_by_xpath("//*[@class='btn btn-submit']")
        button_login.click()
#reca = driver.find_element_by_xpath("//*[@class='login-button__user']")
#reca.click()
#user_mail = driver.find_element_by_xpath("//*[@class='login-button__user']")
#assert user_mail.text == "au"

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"D:/pytest/my_report"))
