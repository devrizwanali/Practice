from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:\\Users\HAIER\Desktop\selenium\chromedriver.exe")

driver.get("http://127.0.0.1:8000/accounts/login/")
driver.find_element_by_id("id_username").send_keys("selenium4")
driver.find_element_by_id("id_password").send_keys("sqa12345")
driver.find_element_by_xpath("/html/body/div/div[1]/div/form/input[2]").click()
driver.close()
