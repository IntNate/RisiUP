from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome(executable_path="chromedriver.exe")

class Script():
    def __init__(self, driver, topic:str, username:str, password:str, message:str='up', delay=10) -> None:
        self.username = username
        self.password = password
        self.topic = topic
        self.message = message
        self.delay = delay
        self.driver = driver
        self.running = True
    
    def AcceptFreeVersion(self):
        self.pop_pup = False
        while self.pop_pup == False:
            try :
                self.btn = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[2]/div/span/div/button[2]")
                self.btn.click()
                self.pop_pup = True
            except:
                pass
                
    
    
    def login(self):
        
        # self.driver.get(self.link)
        self.link = f'https://www.jeuxvideo.com/login?url=https%3A%2F%2Fwww.jeuxvideo.com%2F&hash=f6d2d7b2ed5de512489d34aba1cda581'
        self.driver.get(self.link)
        self.username_box = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[1]/input")
        self.password_box = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[2]/input")
        self.connect_btn = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[4]/button")
        
        
        self.username_box.send_keys(self.username)
        self.password_box.send_keys(self.password)
        self.connect_btn.click()
        #faire le capchat !
        #do the capchat !
        
        
        # while str(self.driver.current_url) != 'https://www.jeuxvideo.com':
        #     time.sleep(0.1)
        #     print(self.driver.current_url)
        
        
        # self.boucle = True
        # while self.boucle:
        #     if self.driver.current_url.endswith('jeuxvideo.com'):
        #         print('oui')
        #         print(self.driver.current_url)
        #         self.boucle = False
        #     else:
        #         print('non')
        #         print(self.driver.current_url)
            
        

    
       
    def send_post(self):
        self.driver.get(self.topic)  
        
        
        self.pop = False
        while self.pop == False:
            try:       
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.ID, "message_topic")))
                WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-poster-msg')))
                
            except:
                
                pass


            self.text_form = self.driver.find_element(by=By.ID, value='message_topic')
            self.text_btn = self.driver.find_element(by=By.CLASS_NAME, value='btn-poster-msg')
            
            self.text_form.send_keys(self.message)
            self.text_btn.click()
            time.sleep(self.delay)
            self.pop = False
            
            

            
        
            
            
    def start(self):
        
        
        self.login()
        self.AcceptFreeVersion()
        self.send_post()

        
        
        
        
instance = Script(driver, 'https://www.jeuxvideo.com/forums/42-51-69544642-1-0-1-0-test.htm','BOT-GENTIL', '1234Abcd')

instance.start()     
        
        

