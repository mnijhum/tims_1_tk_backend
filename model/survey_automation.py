import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def automate_survey(survey_code):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://parlezatim.com/")
        driver.set_window_size(1470, 798)
        driver.switch_to.frame(0)

        driver.find_element(By.ID, "Q_lang").click()
        time.sleep(2)  # 3-second delay
        dropdown = driver.find_element(By.ID, "Q_lang")
        dropdown.find_element(By.XPATH, "//option[. = 'English']").click()
        time.sleep(2)

        driver.find_element(By.ID, "QR~QID9").click()
        driver.find_element(By.ID, "QR~QID9").send_keys(survey_code)
        driver.find_element(By.ID, "NextButton").click()
        time.sleep(2)

        # Use ActionChains correctly without (0, 0)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "QID14-1-label").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#QID15-5-label > span").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "QR~QID80").click()
        driver.find_element(By.ID, "QR~QID80").send_keys("better taste")
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "QID18-6-label").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#QID19-5-label > span").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#QID20-5-label > span").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c5").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(5) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".bottom > .c5 > .q-radio").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "NextButton").click()
        time.sleep(2)
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ReadableAlt > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c4 > .q-radio").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "QID37-2-label").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.ID, "QID134-2-label").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#QID48-1-label > span").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#QID53-35-label > span").click()
        driver.find_element(By.ID, "NextButton").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#QID57-1-label > span").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(1) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(2) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(3) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(4) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(5) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(6) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(7) > .c5 > .q-radio").click()
        driver.find_element(
            By.CSS_SELECTOR, ".ChoiceRow:nth-child(8) > .c5 > .q-radio").click()
        driver.find_element(By.ID, "NextButton").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "#QID74-4-label > span").click()
        driver.find_element(By.ID, "NextButton").click()
        element = driver.find_element(By.ID, "NextButton")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(5)

        element = driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)

        # driver.find_element(By.ID, "NextButton").click()

        # Extract final discount code
        validation_code_element = driver.find_element(
            By.CSS_SELECTOR, "#EndOfSurvey strong")
        print("validation code element ", validation_code_element)
        validation_code = validation_code_element.text.strip(
        ) if validation_code_element else None

        print(f"Validation Code: {validation_code}")
        return {"success": True, "validation_code": validation_code}

    except Exception as e:
        print(str(e))
        return {"success": False, "error": str(e)}

    finally:
        driver.quit()
