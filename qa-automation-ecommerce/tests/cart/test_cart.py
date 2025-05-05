def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/inventory.html")
    
    # Přidání první položky do košíku
    driver.find_element(By.CLASS_NAME, "inventory_item").click()
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()  # Kliknutí na "Přidat do košíku"

    # Ověření, že se položka přidala do košíku
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert cart_count.text == "1"
