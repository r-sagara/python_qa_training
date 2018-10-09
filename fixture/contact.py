


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("HOME").click()

    def create(self, contact):
        driver = self.app.driver
        self.open_contacts_page()
        driver.find_element_by_link_text("ADD_NEW").click()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_name("submit").click()
        self.return_to_contacts_page()

    def return_to_contacts_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("home page").click()
