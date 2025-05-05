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

# Test úspěšné registrace
def test_register_successful(driver):
    driver.get("https://www.saucedemo.com/")  # Zadej správnou URL s registračním formulářem

    driver.find_element(By.ID, "register-link").click()  # Kliknutí na registrační odkaz
    driver.find_element(By.ID, "first-name").send_keys("John")  # Zadání jména
    driver.find_element(By.ID, "last-name").send_keys("Doe")  # Zadání příjmení
    driver.find_element(By.ID, "email").send_keys("john.doe@example.com")  # Zadání emailu
    driver.find_element(By.ID, "password").send_keys("secret_password")  # Zadání hesla
    driver.find_element(By.ID, "register-button").click()  # Odeslání formuláře

    # Ověření, že po úspěšné registraci jsme přesměrováni na přihlašovací stránku
    assert driver.current_url == "https://www.saucedemo.com/login.html"

# Test neúspěšné registrace
def test_register_unsuccessful(driver):
    driver.get("https://www.saucedemo.com/")  # Zadej správnou URL s registračním formulářem

    driver.find_element(By.ID, "register-link").click()  # Kliknutí na registrační odkaz
    driver.find_element(By.ID, "first-name").send_keys("")  # Nevyplněné jméno
    driver.find_element(By.ID, "last-name").send_keys("")  # Nevyplněné příjmení
    driver.find_element(By.ID, "email").send_keys("john.doe.com")  # Nesprávný formát emailu
    driver.find_element(By.ID, "password").send_keys("short")  # Příliš krátké heslo
    driver.find_element(By.ID, "register-button").click()  # Odeslání formuláře

    # Ověření, že se zobrazuje chybová hláška
    error_message = driver.find_element(By.CSS_SELECTOR, ".error-message")
    assert error_message.is_displayed()