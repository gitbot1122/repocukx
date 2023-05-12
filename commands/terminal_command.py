import os
import time
# https://github.com/settings/tokens  => token linki
#curl -H "Authorization: token {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}" -d '{"name":"Repo Name"}' https://api.github.com/user/repos
class TerminalCommand:
    try:
        path = 'C:\\Users\\yakup\\OneDrive\\Belgeler\\docmclone'
        url = 'https://github.com/omersayak/BruteForceWepApp.git'
        def __init__(self):
            pass
        def fetchRepo(self):
            os.system("color a")
            os.system("cls")
            path=input('''
C:\\Users\\user\\OneDrive\\Belgeler\\docmclone
Kaydetmek istediğiniz dosyanın yolunu yukarıdaki kurala uygun veriniz: ''')
            os.chdir(path)
            time.sleep(1)
            os.system("cls")
            url=input('''
"https://github.com/omersayak/Pro_FirstHelper_Script.git"
Github Linkini Yukarıdaki kurala uygun veriniz: ''')
            os.system("git clone "+url)
            time.sleep(2)

    except Exception as e:
        print("An error occurred:", e)
    
