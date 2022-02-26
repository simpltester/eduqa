from selenium.webdriver.common.by import By
from page import WebPage

def test_main(browser):
    mainpage = WebPage(browser)
    mainpage.check_element((By.ID, "logo"))
    mainpage.check_element((By.ID, "search"))
    mainpage.check_element((By.ID, "cart"))
    mainpage.check_element((By.ID, "slideshow0"))
    mainpage.check_element((By.ID, "carousel0"))

def test_cat_desktops(browser):
    catpage = WebPage(browser, "desktops")
    catpage.check_element((By.ID, "list-view"))
    catpage.check_element((By.ID, "grid-view"))
    catpage.check_element((By.ID, "compare-total"))
    catpage.check_element((By.ID, "input-sort"))
    catpage.check_element((By.ID, "input-limit"))
    desk_head =  catpage.check_element((By.ID, "content"))
    assert desk_head.find_element(By.XPATH, "//h2").text == "Desktops"
    active_desk = catpage.check_element((By.CLASS_NAME, "list-group-item"))
    assert "Desktops" in active_desk.text

def test_imac(browser):
    macpage = WebPage(browser, "desktops/mac/imac")
    relate_prod = macpage.check_element((By.ID, "content"))
    assert relate_prod.find_element(By.XPATH, "//h3").text == "Related Products"
    macpage.check_element((By.ID, "tab-description"))
    macpage.check_element((By.ID, "button-cart"))
    mac_head = macpage.check_element((By.CLASS_NAME, "col-sm-4"))
    assert mac_head.find_element(By.XPATH, "//h1").text == "iMac"
    
def test_admin(browser):
    admin_page = WebPage(browser, "admin/")
    admin_page.check_element((By.CLASS_NAME, "panel-title"))
    admin_page.check_element((By.ID, "input-username"))
    admin_page.check_element((By.ID, "input-password"))
    admin_page.check_element((By.CLASS_NAME, "help-block"))
    admin_page.check_element((By.CLASS_NAME, "btn"))

def test_register(browser):
    reg_page = WebPage(browser, "index.php?route=account/register")
    header = reg_page.check_element((By.ID, "content"))
    assert header.find_element(By.XPATH, "//h1").text == "Register Account"
    reg_page.check_element((By.ID, "account"))
    reg_page.check_element((By.ID, "input-firstname"))
    reg_page.check_element((By.ID, "input-lastname"))
    reg_page.check_element((By.ID, "input-email"))
    reg_page.check_element((By.ID, "input-telephone"))
    reg_page.check_element((By.ID, "input-password"))
    reg_page.check_element((By.ID, "input-confirm"))
    reg_page.check_element((By.CLASS_NAME, "agree"))
    reg_page.check_element((By.CLASS_NAME, "btn"))

def test_change_currency(browser):
    mainpage = WebPage(browser)
    cart = mainpage.check_element((By.ID, "cart-total"))
    assert "$" in cart.text
    mainpage.click_by_locator((By.CLASS_NAME, "btn-link"))
    btn = mainpage.check_element((By.CLASS_NAME, "btn-group"))
    mainpage.click_by_elem(btn.find_element(By.XPATH, "//button[@name='EUR']"))
    mainpage.wait_page(1)
    cart = mainpage.check_element((By.ID, "cart-total"))
    assert "€" in cart.text

def test_reg_user(browser):
    mainpage = WebPage(browser)
    mainpage.click_by_locator((By.CLASS_NAME, "dropdown"))
    mainpage.click_link("Register")
    mainpage.input_item("ftest", (By.ID, "input-firstname"))
    mainpage.input_item("ltest", (By.ID, "input-lastname"))
    mainpage.input_item("test@test.com", (By.ID, "input-email"))
    mainpage.input_item("89123456789", (By.ID, "input-telephone"))
    mainpage.input_item("12345678", (By.ID, "input-password"))
    mainpage.input_item("12345678", (By.ID, "input-confirm"))
    confirm = mainpage.check_element((By.CLASS_NAME, "buttons"))
    mainpage.click_by_elem(confirm.find_element(By.XPATH, "//input[@type='checkbox']"))
    mainpage.click_by_elem(confirm.find_element(By.XPATH, "//input[@type='submit']"))
    mainpage.wait_page(1)
    success = mainpage.check_element((By.ID, "content"))
    assert success.find_element(By.XPATH, "//h1").text == "Your Account Has Been Created!"
