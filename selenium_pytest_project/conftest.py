import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Wait until page is fully loaded
    def wait_for_page_load():
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    driver.wait_for_page_load = wait_for_page_load
    yield driver
    driver.quit()

