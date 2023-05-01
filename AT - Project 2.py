from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class OrangeHRM:
    driver = webdriver.Firefox()
    def fill_form(self,url):
    # Get the Data
        username = "Admin"
        password = "admin123"
        
    # Get the XPATH / ID / Class
        username_xpath = '//[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
        password_xpath = '//[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
        login_button_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
        
        try:
            # open the webpage
            self.driver.get(url)

            #find the XPATH of the HTML element present on the webpage
            username_xpath=self.driver.find_element(by=By.XPATH, value=username_xpath)
            password_xpath=self.driver.find_element(by=By.XPATH, value=password_xpath)
            login_button_xpath=self.driver.find_element(by=By.XPATH, value=login_button_xpath)

    # fill the HTML form
            username_xpath.send_keys(username)
            password_xpath.send_keys(password)
            time.sleep(10)

            # click on the Submit button
            login_button_xpath.click()
            time.sleep(5)
        except: 
            print (" Error : XPATH not foun ! ")
            
    
     #Search TextBox TC-02:
    def Navigate_To_usermanagement(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(5)
            class_link.click()
        except:
            print("ERROR : Class not found !")
            
    def Click_users(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(3)
            class_link.click()
        except:
            print("ERROR : Class not found !")    
            
    def Select_dropdown (self,url,class_link) 
        try:
            self.driver.get(url)
            Select = Select(driver.find_element_by_class("oxd-select-text-input"))  
            time.sleep(3)
            class_link.click()  
        except:
            print("ERROR : Class not found !")    
              
    def Select_dropdown (self,url,class_link)
        try:
            self.driver.get(url)
            Select = Select(driver.find_element_by_class("oxd-select-text-input"))  
            time.sleep(3)
            class_link.click()  
        except:
            print("ERROR : Class not found !") 
            
#Creation of new Emp  TC-03: 
                     
    def Navigate_To_Pim(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(5)
            class_link.click()
        except:
            print("ERROR : Class not found !")
            
    def Add_Emp(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(5)
            class_link.click()
        except:
            print("ERROR : Class not found !")        
            
    def fill_Emp_Details (self,url):
        # Get the Data
        Firstname = "Jamuna"
        Middlename = "Mageshwari"
        Lastname = "V"
        
        
        # Get the XPATH / ID / Class
        Firstname_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
        Middlename_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
        Lastname_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
        Save_button_xpath = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        
        try:
            # open the webpage
            self.driver.get(url)

            #find the XPATH of the HTML element present on the webpage
            Firstname_xpath=self.driver.find_element(by=By.XPATH, value=Firstname_xpath)
            Middlename_xpath=self.driver.find_element(by=By.XPATH, value=Middlename_xpath)
            Lastname_xpath=self.driver.find_element(by=By.XPATH, value=Lastname_xpath)
            Save_button_xpat=self.driver.find_element(by=By.XPATH, value=Save_button_xpat)


       
            # fill the HTML form     
            Firstname_xpath.send_keys(Firstname)
            Middlename_xpath.send_keys(Middlename)
            Lastname_xpath.send_keys(Lastname)
            
            
            # click on the save button
            Save_button_xpath.click()
            time.sleep(2)
                       
        except:
            print("ERROR : XPATH not found !")
           
    #Emp persional Details TC-04: 
                     
    def Navigate_To_Pim(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(5)
            class_link.click()
        except:
            print("ERROR : Class not found !")
            
    def Emp_List(self, url, class_link):
         
        try:
            self.driver.get(url)
            class_link = self.driver.find_element(by=By.CLASS_NAME, value=class_link)
            time.sleep(5)
            class_link.click()
        except:
            print("ERROR : Class not found !")        
   
    def Select_by_Logout(Self,url,class_link):
            Self.driver.get(Self,url)
            Logout = Self.driver.find_element(by=By.CLASS_Name, Value="oxd-userdropdown-link")
            time.sleep(3)
            Logout.click()          
            
O = OrangeHRM()
url = 'https://opensource-demo.orangehrmlive.com/' 
    
Navigate_To_Admin= "oxd-main-menu-item toggle" 
Navigate_To_Usermanager ="oxd-topbar-body-nav-tab"
Click_users="oxd-topbar-body-nav-tab-link"
Navigate_To_PIM = "oxd-text oxd-text--span oxd-main-menu-item--name"
Add_emp = "oxd-button oxd-button--medium oxd-button--secondary"
Emp_List = "oxd-topbar-body-nav-tab-item"
    
      
        
O.fill_form(url)
O.Navigate_To_PIM_link(url, Navigate_To_PIM) 
O.Add_Emp(url,Add_emp)
O.fill_Emp_Details (url)   
O.Emp_Details(url,Emp_details)
        