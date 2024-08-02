from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AdminLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/')  # Replace with your admin login URL

    def test_admin_login(self):
        driver = self.driver
        
        # Find and fill in the username field
        username_field = driver.find_element(By.NAME, 'username')
        username_field.send_keys('ken')  # Replace with your admin username
        
        # Find and fill in the password field
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('1234minu')  # Replace with your admin password
        
        # Click the login button
        login_button = driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-success')
        login_button.click()
        
        # Print the current URL for debugging
        print(f"Current URL before waiting: {driver.current_url}")
        
        # Wait for the URL to be the dashboard URL
        try:
            WebDriverWait(driver, 10).until(EC.url_to_be('http://127.0.0.1:8000/staff_index.html'))
            print("Redirected to dashboard URL.")
        except Exception as e:
            print(f"Failed to redirect to dashboard URL. Exception: {e}")
            self.fail(f"Redirection to dashboard URL failed. Exception: {e}")
        
        # Print the current URL after redirection
        print(f"Current URL after waiting: {driver.current_url}")

        # Wait for the dashboard container to be visible
        try:
            # Use a specific unique element on the dashboard page
            dashboard_element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'user-dashboard-container'))  # Replace with an actual unique element ID or selector
            )
            self.assertTrue(dashboard_element.is_displayed())
            print("Dashboard element is visible.")
        except Exception as e:
            print(f"Error: {e}")
            self.fail(f"Dashboard element not found or not visible. Exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
