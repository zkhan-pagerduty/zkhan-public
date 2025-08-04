import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# This script automates the login process for multiple ServiceNow instances using Selenium.
# It reads the URLs and credentials from a JSON file and logs into each instance sequentially.
# Make sure to replace the path with the actual path to your JSON file containing URLs and credentials.

with open("/Users/..../url_and_creds.json", "r") as f:
    data = json.load(f)

for d in data["instances"]:
    print(f"Processing {d['url']}")
    driver = webdriver.Chrome()
    driver.get(d["url"])

    try:
        user = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user_name"))
        )
        current_url = driver.current_url
        user.clear()
        user.send_keys(d["username"])
        time.sleep(1)  # Wait for the input to be processed

        passwd = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user_password"))
        )

        passwd.clear()
        passwd.send_keys(d["password"])
        time.sleep(1)  # Wait for the input to be processed

        login_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "sysverb_login"))
        )
        login_btn.click()
        print("Login button clicked, waiting for URL change...")
        WebDriverWait(driver, 15).until(EC.url_changes(current_url))

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.close()
        print(f"Finished processing {d['url']}")


driver.quit()
