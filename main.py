import os
import time
from commands.github_login import GithubLogin 
from commands.terminal_command import TerminalCommand
from commands.new_repo import SendCode
os.system("cls")
os.system("color 9")
git=GithubLogin()
tc = TerminalCommand()


def main():
    os.system("cls")
    os.system("color 9")
    print(f'''
->1-) Kod paylaşım  

    ''')
    profchoice = input("Seçmek istediğiniz komutun karşılığına denk gelen rakamı yazınız: ") 
    if profchoice == "1":
        SendCode()
        main()
    else:
        main()




if(GithubLogin.isUserActive==False):
    git.singIn()
    main()
#  C:\Users\yakup\OneDrive\Belgeler\github_bot


