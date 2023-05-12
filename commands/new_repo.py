import os
import time
import requests
from commands.github_login import GithubLogin
from selenium.webdriver.common.by import By

class SendCode(GithubLogin):

    def __init__(self):
        self._selectionScreen()

    def _selectionScreen(self):
        try:
            chooseToken = int(input(r'''
    ->1-) Yeni token anahtarı oluştur
    ->2-) Zaten token anahtarım var 
    ->3-) Ana menüye dön '''))
            
            if(chooseToken == 1):
                self.createToken()
                chooseRepo = int(input('''
    ->1-) Yeni repo  oluştur
    ->2-) Zaten repom var 
    ->3-) Ana menüye dön '''))
                if(chooseRepo == 1):
                    self.createRepo()
                    self.gitPush()
                if(chooseRepo == 2):
                    self.gitPush()  
                if(chooseRepo ==3):
                    pass

            if(chooseToken ==2 ):
                chooseRepo = int(input(r'''
    ->1-) Yeni repo  oluştur
    ->2-) Zaten repom var 
    ->3-) Ana menüye dön '''))
                if(chooseRepo == 1):
                    self.createRepo()
                    self.gitPush()
                if(chooseRepo == 2):
                    self.gitPush()  
                if(chooseRepo ==3):
                    pass
            if(chooseToken == 3):
                pass
        except Exception as e:
            print("Bir hata oluştu: ", e)           
    def createToken(self):
        try:
            GithubLogin.browser.get("https://github.com/settings/tokens/new")
            time.sleep(2)
            tokenDescription=GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div[2]/div/div[2]/div/div/form/dl/dd/input")
            tokenDescription.send_keys(input("Token açıklamasını giriniz: "))
            repoCheckbox=GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div[2]/div/div[2]/div/div/form/div/dl[2]/dd/div/ul/li[1]/div/label/div[1]/input")
            repoCheckbox.click()
            time.sleep(2)
            generateButton=GithubLogin.browser.find_element(By.XPATH,"/html/body/div[1]/div[6]/main/div[2]/div/div[2]/div/div/form/p/button")
            generateButton.click()
            time.sleep(2)
            tokenValue=GithubLogin.browser.find_element(By.CSS_SELECTOR,"#new-oauth-token").text
            print(f'''
Token anahtarınızı bir yere not ediniz. Bazı işlemler için ihtiyaç duyulacaktır!
Token anahatarınız :" {tokenValue} "
''')
        except Exception as e:
            print("Bir hata meydana geldi:", e)

    def createRepo(self):
        try:
            url = 'https://api.github.com/user/repos'
            tokenValue=input(r'''
Örnek anahtar: ghp_F3h8U1xJRckSQAvvKSyqaap2cl766j3rgrkH                          
Token anahtarınızı yazınız: ''')
            headers = {'Authorization': f'token {tokenValue}'}
            time.sleep(3)
            repoName=input('''
Repo isimlendime örnegi: IlkRepom
Lütfen repo adı giriniz: ''')
            data = {'name':f'{repoName}'}

            response = requests.post(url, headers=headers, json=data)

            if response.ok:
                print(f"Repo '{data['name']}' {repoName} reposu başarıyla oluştu!")
            else:
             print(f"Repo oluşturuluken bir hata oluştu: {response.text}")

        except Exception as e:
            print("Bir hata meydana geldi: ",e)
            input()

    def gitPush(self):
        try:
            filePath =input(r'''
    C:\Users\user\OneDrive\documents\github_bot
    Repo'ya yüklemek istediğiniz dosyanın yolunu yukarıdaki örnege uygun veriniz: ''')
            isfile= os.path.exists(os.path.join(filePath, ".git"))
            if(isfile == True):
                self.githubcomand(filePath=filePath)
            else:
                os.system("git init")
                time.sleep(1)
                self.githubcomand()
        except Exception as e:
            print("bir hata meydana geldi: ",e)
            time.sleep(5)
    def githubcomand(self,filePath):
        os.chdir(filePath)
        time.sleep(2)
        os.system("git add .")
        time.sleep(2)
        commitmessage=input("commit mesajınızı giriniz: ")
        os.system(f'git commit -m "{commitmessage}')
        time.sleep(2)
        repoName = input(r"repo adını yazınız: ")
        os.system(f"git remote add origin https://github.com/{GithubLogin.user.username}/{repoName}.git")
        time.sleep(2)
        branchName=input(r'''
örnek: main         
Branch adını giriniz
            ''')
        os.system(f"git push -u origin {branchName} ")
        print("Dosya içeriği github'a yüklendi! ")
        time.sleep(3)


