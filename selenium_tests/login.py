from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginFlowTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://127.0.0.1:8000/')  # Change this to your actual login URL
    
    def test_login_flow(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Wait for the username input to be present
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            print("Username input found")
            
            # Wait for the password input to be present
            password_input = wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )
            print("Password input found")
            
            # Wait for the login button to be clickable
            login_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-success"))
            )
            print("Login button found and is clickable")
            
            # Perform login action
            username_input.send_keys("admin")
            password_input.send_keys("1234")
            login_button.click()
            print("Login submitted")
            
            # Wait for redirection to the dashboard page
            wait.until(EC.url_contains('/dashboard/'))
            print("Dashboard page loaded")
            
            # Verify that the dashboard content is present
            dashboard_header = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'canvas'))  # Use a specific selector to verify content
            )
            self.assertTrue(dashboard_header.is_displayed(), "Dashboard header is not displayed")
            print("Dashboard content verified")

        except Exception as e:
            print(f"Error during test: {e}")
            self.fail(f"Test failed due to: {str(e)}")
    
    @classmethod
    def tearDownClass(cls):
        # Ensure the driver quits properly
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
