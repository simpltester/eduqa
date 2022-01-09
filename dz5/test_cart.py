import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def wait_element(browser):
    return WebDriverWait(browser, 3, poll_frequency=1)

def test_main(browser):
    browser.get(browser.url)
    wait = wait_element(browser)
    wait.until(EC.visibility_of_element_located((By.ID, "logo")))
    wait.until(EC.visibility_of_element_located((By.ID, "search")))
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))
    wait.until(EC.visibility_of_element_located((By.ID, "slideshow0")))
    wait.until(EC.visibility_of_element_located((By.ID, "carousel0")))

def test_cat_desktops(browser):
    browser.get(browser.url + "/desktops")
    wait = wait_element(browser)
    wait.until(EC.visibility_of_element_located((By.ID, "list-view")))
    wait.until(EC.visibility_of_element_located((By.ID, "grid-view")))
    wait.until(EC.visibility_of_element_located((By.ID, "compare-total")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-sort")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-limit")))
    desk_head = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert desk_head.find_element_by_xpath("//h2").text == "Desktops"
    active_desk = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "list-group-item")))
    assert "Desktops" in active_desk.text

def test_imac(browser):
    browser.get(browser.url + "/desktops/mac/imac")
    wait = wait_element(browser)
    wait.until(EC.visibility_of_element_located((By.ID, "content")))
    wait.until(EC.visibility_of_element_located((By.ID, "tab-description")))
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart"))) 
    mac_head = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "col-sm-4")))
    assert mac_head.find_element_by_xpath("//h1").text == "iMac"
    relate_prod = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert relate_prod.find_element_by_xpath("//h3").text == "Related Products"

def test_admin(browser):
    browser.get(browser.url + "/admin/")
    wait = wait_element(browser)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "panel-title"), "Please enter your login details."))
    wait.until(EC.visibility_of_element_located((By.ID, "input-username")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "help-block")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn")))

def test_register(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = wait_element(browser)
    header = wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert header.find_element_by_xpath("//h1").text == "Register Account"
    wait.until(EC.visibility_of_element_located((By.ID, "account")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-firstname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-lastname")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-email")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-telephone")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-password")))
    wait.until(EC.visibility_of_element_located((By.ID, "input-confirm")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "agree")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn")))
