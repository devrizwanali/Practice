import unittest

from selenium import webdriver

# driver = webdriver.Firefox(executable_path="C:\\Users\HAIER\Downloads\Compressed\geckodriver-v0.23.0-win64\geckodriver.exe")
# driver = webdriver.Edge(executable_path="C:\\Users\HAIER\Downloads\Programs\MicrosoftWebDriver.exe")

# driver = webdriver.Opera(executable_path="C:\\Users\HAIER\Downloads\Compressed\operadriver_win64\operadriver_win64\operadriver.exe")
# driver = webdriver.Opera(executable_path="C:\\Users\HAIER\Downloads\Compressed\operadriver_win32\operadriver_win32\operadriver.exe")

class Testingsearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\\Users\HAIER\Desktop\selenium-java\chromedriver.exe")
        cls.driver.get("http://127.0.0.1:8000/accounts/login/")
        # cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_log_in(self):
        self.driver.find_element_by_id("id_username").send_keys("selenium4")
        self.driver.find_element_by_id("id_password").send_keys("sqa12345")
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div/form/input[2]").click()

    def test_google(self):
        self.driver.find_element_by_id("id_q").send_keys("shirts")



    @classmethod
    def tearDown(cls):
        print("completed")
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()



