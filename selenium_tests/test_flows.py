from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to the ChromeDriver
chrome_driver_path = r'C:\Users\a\Desktop\drivers\chromedriver-win64\chromedriver.exe'

try:
    # Create a Service object
    service = Service(chrome_driver_path)
    # Initialize the WebDriver with the Service object
    driver = webdriver.Chrome(service=service)
    # Open Google
    driver.get('https://www.google.com')
    print("Google opened successfully.")
except Exception as e:
    print(f"Error: {e}")
