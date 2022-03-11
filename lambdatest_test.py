import os
import unittest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By

username = os.environ.get("LT_USERNAME")
access_key = os.environ.get("LT_ACCESS_KEY")


class FirstSampleTest(unittest.TestCase):

    # setUp runs before each test case
    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "user": username,
                "accessKey": access_key,
                "build": "UnitTest - Python",
                "name": "UnitTest Demo Test",
                "platformName": "Windows 11",
                "selenium_version": "4.0.0"
            },
            "browserName": "Chrome",
            "browserVersion": "latest",
        }

        self.driver = webdriver.Remote(
            command_executor="http://hub.lambdatest.com:80/wd/hub",
            desired_capabilities=desired_caps)


# tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

    def test_demo_site(self):
        # try:
        driver = self.driver

        # Url
        print('Loading URL')
        driver.get("https://stage-demo.lambdatest.com/")

        # Let's select the location
        driver.find_element(By.ID, "headlessui-listbox-button-1").click()
        location = driver.find_element(By.ID, "Bali")
        location.click()
        print("Location is selected as Bali.")

        # Let's select the number of guests
        driver.find_element(By.ID, "headlessui-listbox-button-5").click()
        guests = driver.find_element(By.ID, "2")
        guests.click()
        print("Number of guests are selected.")

        # Searching for the results
        search = driver.find_element(By.XPATH, "//*[@id='search']")
        search.click()
        driver.implicitly_wait(3)

        # Let's select one of the hotels for booking
        reserve = driver.find_element(By.ID, "reserve-now")
        reserve.click()
        driver.implicitly_wait(3)
        proceed = driver.find_element(By.ID, "proceed")
        proceed.click()
        driver.implicitly_wait(3)
        print("Booking is confirmed.")

        # Let's download the invoice
        download = driver.find_element(By.ID, "invoice")
        if (download.is_displayed()):
            download.click()
            driver.execute_script("lambda-status=passed")
            print("Tests are run successfully!")
        else:
            driver.execute_script("lambda-status=failed")


if __name__ == "__main__":
    unittest.main()
