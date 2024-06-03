# импортируем модули и отдельные классы
import pytest
from selenium.webdriver.common.by import By

URL = "https://testqastudio.me/"

def test_product_view_sku(test_product_view_sku):
    """
    TMS-1:[web][catalog] Проверка SKU товара
    """
    test_product_view_sku.get(url=URL)
    test_product_view_sku.find_element(by=By.CSS_SELECTOR, value="[class*='tab-best_sellers']").click()
    test_product_view_sku.find_element(by=By.CSS_SELECTOR, value='[class*="post-11341"]').click()
    sku = test_product_view_sku.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"
