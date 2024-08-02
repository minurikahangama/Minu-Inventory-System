from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.common.exceptions import TimeoutException

class ProductCRUDTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")  # Replace with your login URL
        
        # Log in
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success[type='submit']")
        
        username_input.send_keys("admin")
        password_input.send_keys("1234")
        login_button.click()
        
        # Ensure login is successful
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://127.0.0.1:8000/dashboard/")  # Replace with your dashboard URL
        )

    def test_create_product(self):
        driver = self.driver

        # Navigate to the product page
        driver.get("http://127.0.0.1:8000/product/")  # Replace with your product page URL

        # Enter product details
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        category_input = driver.find_element(By.NAME, "category")
        quantity_input = driver.find_element(By.NAME, "quantity")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-success.btn-block[type='submit']")

        name_input.send_keys("Test Product")
        category_input.send_keys("Stationary")  # Adjust based on your category options
        quantity_input.send_keys("10")
        submit_button.click()

        # Verify product is listed
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Test Product")
        )

    def test_read_product(self):
        driver = self.driver

        # Navigate to the product page
        driver.get("http://127.0.0.1:8000/product/")  # Replace with your product page URL

        # Verify that a specific product is displayed
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Test Product")
        )

        # Optionally, you can add more specific checks if needed
        product_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Test Product')]"))
        )
        self.assertIsNotNone(product_name, "Product 'Test Product' is not displayed on the page")

    def test_update_product(self):
        driver = self.driver

        # Navigate to the product page
        driver.get("http://127.0.0.1:8000/product/")  # Replace with your product page URL

        # Find and click the edit button for the specific product
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-info.btn-sm"))
        )
        edit_button.click()

        # Update product details
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "name"))
        )
        category_input = driver.find_element(By.NAME, "category")
        quantity_input = driver.find_element(By.NAME, "quantity")
        submit_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-info.btn-sm[type='submit']")

        # Use JavaScript to clear fields if necessary
        driver.execute_script("arguments[0].value = '';", category_input)
        name_input.clear()
        name_input.send_keys("Updated Test Product")
        category_input.send_keys("Electronics")  # Adjust based on your category options
        quantity_input.clear()
        quantity_input.send_keys("20")
        submit_button.click()

        # Verify product details are updated
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Updated Test Product")
        )

    def test_delete_product(self):
        driver = self.driver

        # Navigate to the product page
        driver.get("http://127.0.0.1:8000/product/")  # Replace with your product page URL

        # Find and click the delete button for the specific product
        delete_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-danger.btn-sm"))
        )
        delete_button.click()

        # Confirm deletion on the confirmation page
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-danger"))
        )
        confirm_button.click()

        # Verify product is no longer listed
        try:
            WebDriverWait(driver, 10).until_not(
                EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Test Product')]"))
            )
        except TimeoutException:
            self.fail("Product 'Test Product' was not deleted successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
