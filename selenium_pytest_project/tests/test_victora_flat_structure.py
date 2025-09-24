import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestVictora:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # Maximizes the browser window

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_url(self):
        self.driver.get("https://victoraauto-asterisksc-uat-landing.ey.com/auth/login")
        WebDriverWait(self.driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login-header"))
        )
        time.sleep(1)

    def test_enter_valid_username_password(self):
        # Optionally call test_url if needed
        # self.test_url()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'text')]"))
        ).send_keys("arpitha.atharga@in.ey.com")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'password')]"))
        ).send_keys("password")

        # Click login button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),' Login ')]"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Ok')]"))
        ).click()

        time.sleep(2)
