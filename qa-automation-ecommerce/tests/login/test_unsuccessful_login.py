import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_login_unsuccessful(driver):
    driver.get("https://www.saucedemo.com/")

    # špatné přihlašovací údaje
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    # Ověříme, že se zobrazuje chybová zpráva
    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
    assert error_message.is_displayed()
    assert error_message.text == "Epic sadface: Username and password do not match any user in this service"