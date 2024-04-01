from dataPage import Data
from Element import element

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_Case:

    def __init__(self):
        """
        Initializes the Test_Case class with WebDriver and WebDriverWait instances.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        """
        Navigates to the URL specified in Data.PageSource and waits until the URL is fully loaded.
        """
        self.driver.get(Data.PageSource().url)
        self.driver.maximize_window()
        self.wait.until(EC.url_to_be(Data.PageSource().url))

    def close(self):
        """
        Quits the WebDriver instance.
        """
        self.driver.quit()

    def login(self, username, password):
        """
        Attempts to log in using the provided username and password.
        """
        try:
            self.start()
            self.wait.until(EC.visibility_of_element_located((By.NAME, element.pageElement().Username))).send_keys(
                username)
            self.wait.until(EC.visibility_of_element_located((By.NAME, element.pageElement().Password))).send_keys(
                password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().loginButton))).click()
            self.wait.until(EC.url_to_be(Data.PageSource().LoginUrl))
            print("The user is logged in successful")
        except TimeoutException:
            print("Invalid Credentials")

    def logout(self):
        """
        Logs out from the application by clicking on the user menu and then the logout button.
        """
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().userMenu))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().logout))).click()
        except NoSuchElementException as e:
            print("Error during logout:", e)

    def write_test_result(self, row, result):
        """
        Writes the test result (Passed or Failed) to the Excel file at a specific row and column.
        """
        Data.PageSource().writeExcel(row, 10, result)

    def Test_Case_Login(self):
        """
        Executes a test case ID 01 and 02 to log in using credentials from Excel file.
        """
        try:
            for row in range(2, Data.PageSource().Totaldata()-2):  # Corrected range
                username = Data.PageSource().readExcel(row, 2)
                password = Data.PageSource().readExcel(row, 3)
                try:
                    self.login(username, password)
                    self.write_test_result(row, "Test Passed")
                    self.wait.until(EC.url_changes(Data.PageSource().url))
                except:
                    self.write_test_result(row, "Test Failed")
        except NoSuchElementException as e:
            print("Error in logging in:", e)
        finally:
            self.logout()

    def TestCase_PIM01(self):
        """
        Executes a test case to add a new employee by entering their details.
        """
        try:
            for row in range(4, Data.PageSource().Totaldata()-1):
                username = Data.PageSource().readExcel(row, 2)
                password = Data.PageSource().readExcel(row, 3)
                firstname = Data.PageSource().readExcel(row, 4)
                middlename = Data.PageSource().readExcel(row, 5)
                lastname = Data.PageSource().readExcel(row, 6)
                Emp_ID = Data.PageSource().readExcel(row, 7)
                try:
                    self.login(username, password)
                    # Go to PIM menu
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().PIMMenu))).click()
                    # Add new employee
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().addEmployee))).click()

                    # Enter the First Name
                    self.wait.until(EC.element_to_be_clickable((By.NAME, element.pageElement().FirstName))).send_keys(
                        firstname)
                    # Enter the Middle Name
                    self.wait.until(EC.element_to_be_clickable((By.NAME, element.pageElement().MiddleName))).send_keys(
                        middlename)
                    # Enter the Last Name
                    self.wait.until(EC.element_to_be_clickable((By.NAME, element.pageElement().LastName))).send_keys(
                        lastname)
                    # Enter the employee ID
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().empId))).send_keys(Emp_ID)
                    # Save the employee details
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().Add_save))).click()
                    # Get the success message
                    success_message = self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().Message)))
                    print({success_message.text})

                    # Wait for the success message or any other indicator of employee addition
                    self.wait.until(EC.url_changes(Data.PageSource().AddEmployee_Url))

                    # Go to dashboard Home
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().dasboard))).click()

                    self.write_test_result(row, "Test Passed")
                    print("Successfully employee addition")
                except:
                    self.write_test_result(row, "Test Failed")
        except NoSuchElementException as e:
            print("Error in employee addition!")
        finally:
            self.logout()

    def TestCase_PIM02(self):
        """
        Executes a test case to edit an existing employee's details.
        """
        try:
            for row in range(5, Data.PageSource().Totaldata()):
                username = Data.PageSource().readExcel(row, 2)
                password = Data.PageSource().readExcel(row, 3)
                Emp_ID = Data.PageSource().readExcel(row, 7)
                DL_Number = Data.PageSource().readExcel(row, 8)
                other_ID = Data.PageSource().readExcel(row, 9)
                try:
                    self.login(username, password)
                    # Go to PIM menu
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().PIMMenu))).click()
                    # Click an existing employee to edit the details
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().edit))).click()
                    # Enter the Employee ID
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().EmpID))).send_keys(Emp_ID)
                    # Enter the Other ID
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().Other_ID))).send_keys(other_ID)
                    # Enter the Driver's license number
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().Driving_license))).send_keys(DL_Number)
                    # Save the Employee
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().edit_save))).click()
                    # Wait to load the page
                    self.wait.until(EC.url_changes(Data.PageSource().editEmployee_Url))
                    # Get the success message
                    success_message = self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().Edit_message)))
                    print({success_message.text})
                    # Wait for the success message or any other indicator of employee addition
                    self.wait.until(EC.url_changes(Data.PageSource().url))
                    # Go to dashboard Home
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().dasboard))).click()
                    self.write_test_result(row, "Test Passed")
                    print("Successfully employee details addition")
                except:
                    self.write_test_result(row, "Test Failed")
        except NoSuchElementException as e:
            print("Error in employee detail addition:", e)
        finally:
            self.logout()

    def TestCase_PIM03(self):
        """
        Executes a test case to delete an existing employee's details.
        """
        try:
            for row in range(6, Data.PageSource().Totaldata()+1):
                username = Data.PageSource().readExcel(row, 2)
                password = Data.PageSource().readExcel(row, 3)
                try:
                    self.login(username, password)
                    # Go to PIM menu
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().PIMMenu))).click()
                    # Delete an existing employee in the list
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().delete))).click()
                    # Accept yes to delete the employee
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().yes))).click()

                    # Get the success message
                    success_message = self.wait.until(EC.element_to_be_clickable((By.XPATH, element.pageElement().delete_message)))
                    print({success_message.text})

                    # Wait for the success message or any other indicator of employee addition
                    self.wait.until(EC.url_changes(Data.PageSource().url))
                    print("Successful deletion")

                    self.write_test_result(row, "Test Passed")
                except NoSuchElementException:
                    print("Error in deletion!")
                    self.write_test_result(row, "Test Failed")
        finally:
            self.logout()
            self.close()

obj = Test_Case()
obj.Test_Case_Login()
obj.TestCase_PIM01()
obj.TestCase_PIM02()
obj.TestCase_PIM03()
