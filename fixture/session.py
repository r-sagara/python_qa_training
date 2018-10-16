__author__ = 'Ruslan'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        driver = self.app.driver
        # print("###", len(driver.find_elements_by_link_text("LOGOUT")))
        return len(driver.find_elements_by_link_text("LOGOUT")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        # print(driver.find_element_by_css_selector("div#top form b").text)
        return "(" + username + ")" == driver.find_element_by_css_selector("div#top form b").text

    def logout(self, ensure=False):
        driver = self.app.driver
        if ensure:
            if self.is_logged_in():
                driver.find_element_by_link_text("LOGOUT").click()
                return
        driver.find_element_by_link_text("LOGOUT").click()

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
