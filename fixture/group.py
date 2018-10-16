

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_name("new").click()
        # fill the form
        self.fill_group_form(group)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("GROUPS").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        self.select_first_group(driver)
        # submit deletion
        self.delete_groups(driver)
        self.return_to_groups_page()

    def delete_groups(self, driver=None):
        if driver is None:
            driver = self.app.driver
        driver.find_element_by_name("delete").click()

    def select_first_group(self, driver):
        driver.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group(driver)
        # open modification form
        driver.find_element_by_name("edit").click()
        # fill the form
        self.fill_group_form(new_group_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    def check_all_groups(self):
        driver = self.app.driver
        self.open_groups_page()
        for item in driver.find_elements_by_name("selected[]"):
            item.click()
