def AcceptFreeVersion():
    btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/div/div/div[2]/div/span/div/button[2]")
    btn.click()

def login(username, password):
    btn = driver.find_element(by=By.CLASS_NAME, value="icon-account")
    btn.click()
    
    username_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[1]/input")
    password_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[2]/input")
    connect_btn = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/div/div[2]/form/div[4]/button")
    
    
    username_box.send_keys(username)
    password_box.send_keys(password)
    connect_btn.click()
    #faire le capchat !
    #do the capchat !
    while driver.current_url != "https://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm":
        time.sleep(0.1)
