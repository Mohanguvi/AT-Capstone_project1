
from selenium.webdriver.common.by import By



class pageElement:

    def __init__(self):
        """
        The __init__() method initializes the class instance with the following attributes:
            - Username: Locator for the username input field.
            - Password: Locator for the password input field.
            - loginButton: Locator for the login button.
            - userMenu: Locator for the user menu.
            - logout: Locator for the logout button.
        """
        # login element
        self.Username = "username"
        self.Password = "password"
        self.loginButton = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'

        # Dashboard home
        self.dasboard = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'

        # PIM menu Xpath
        self.PIMMenu = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'

        # New Employee details
        self.addEmployee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
        self.FirstName = "firstName"
        self.MiddleName = "middleName"
        self.LastName = "lastName"
        self.empId = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
        self.Add_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        self.Message = '//*[@id="oxd-toaster_1"]'

        # Employee Edit details
        self.edit = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]'
        self.EmpID = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
        self.Other_ID = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
        self.Driving_license = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
        self.edit_save = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
        self.Edit_message = '//*[@id="oxd-toaster_1"]'

        # Delete a employee
        self.delete = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]'
        self.yes = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
        self.delete_message = '//*[@id="oxd-toaster_1"]'

        # logout elements
        self.userMenu = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li'
        self.logout = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    def enterText(self, driver, locator, text):
        """
        The enterText() method takes three arguments: driver, locator, and text.
        It finds the element based on the specified locator and enters the provided text into the input field.
        :param driver:
        :param locator:
        :param text:
        :return:
        """
        key = driver.find_element(by=By.NAME, value=locator)
        key.clear()
        key.send_keys(text)


    def clickpath(self, driver, locator):
        """
        The clickButton() method takes two arguments: driver and locator.
        It finds the element based on the specified locator and clicks on it.
        :param driver:
        :param locator:
        :return:
        """
        driver.find_element(by=By.XPATH, value=locator).click()
