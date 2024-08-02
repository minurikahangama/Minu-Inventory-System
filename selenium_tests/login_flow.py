import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AdminLoginTest(unittest.TestCase):

    def setUp(self):
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://127.0.0.1:8000/")

    def test_admin_login(self):
        driver = self.driver

        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys("admin")  
        password_field.send_keys("1234")  

        login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success")
        login_button.click()

        driver.implicitly_wait(10)  

        print("Current URL after login:", driver.current_url)

        expected_url = "http://127.0.0.1:8000/dashboard"
        actual_url = driver.current_url.rstrip('/')
        self.assertEqual(actual_url, expected_url)
        
        driver.implicitly_wait(10)

    def tearDown(self):
    
        self.driver.quit()
        

if __name__ == "__main__":
    unittest.main()
