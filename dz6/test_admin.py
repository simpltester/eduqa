from page import AdminPage

def test_add_item(browser):
    admin_page = AdminPage(browser)
    admin_page.login_with("user", "bitnami")
    admin_page.add_product()

def test_delete_item(browser):
    admin_page = AdminPage(browser)
    admin_page.login_with("user", "bitnami")
    admin_page.delete_prosuct()
    