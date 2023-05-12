import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GithubLogin():
    isUserActive =False
    from commands.user_info import User
    user =User("","")
    try:
        chrome_driver_path="webdriver/chromedriver.exe"
        browser = webdriver.Chrome(chrome_driver_path)
        browser.minimize_window()
        baseUrl = "https://github.com/"
    except Exception as e:
            print("An error occurred:", e)
    def __init__(self):
        pass

    def singIn(self):
        try:    
            
            
            self.username= self.user.userName="gitbotum55" #input("Kullanıcı Adı veya E-Posta: ")
            self.password= self.user.password="Gitbotum1" #input("Şifre: ") 

            GithubLogin.browser.get(self.baseUrl +"login")
            time.sleep(2)

            username=GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]")
            username.send_keys(self.username)

            passsword=GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]")
            passsword.send_keys(self.password)  
            GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[12]").click()

            time.sleep(2)
            isMailCode=GithubLogin.browser.find_elements(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[3]/div[2]/div[2]/form/input[2]")
            if len(isMailCode)>0:   
                if(isMailCode[0].is_enabled):
                    isFlase=True
                    while(isFlase):
                        code=input("Giriş için 6 haneli e-mail kodunu giriniz: ")
                        isMailCode[0].send_keys(code)
                        verifybutton=GithubLogin.browser.find_elements(By.XPATH,"/html/body/div[1]/div[3]/main/div/div[3]/div[2]/div[2]/form/button")
                        verifybutton[0].click()
                        time.sleep(2)
                        if(len(verifybutton[0]) == 0):
                            isFlase=False
                            self.isUserActive =True
            print("Giriş başarıyla yapıldı! ")          
            time.sleep(1)
            time.sleep(0)
        except Exception as e:
            print("An error occurred:", e)

    

    

    





