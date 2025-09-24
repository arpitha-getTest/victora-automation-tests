import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    # Maximize the browser window
    driver.maximize_window()

    yield driver
    # driver.quit()


def test_enter_valid_username_password(driver):
    driver.get("https://victoraauto-asterisksc-uat-landing.ey.com/auth/login")

    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "login-header"))
    )

    # def test_enter_valid_username_password(driver):
    # Wait for username field and enter credentials
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'text')]"))
    ).send_keys("arpitha.atharga@in.ey.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, " //input[contains(@type,'password')]"))
    ).send_keys("password")

    # Click login button
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),' Login ')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Ok')]"))
    ).click()

    time.sleep(3)

    assert "Asterisk" in driver.title


