

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
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("GROUPS").click()

    def delete_first_group(self):
        driver = self.app.driver
        self.open_groups_page()
        # select first group
        driver.find_element_by_name("selected[]").click()
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()