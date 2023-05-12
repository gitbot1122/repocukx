import os

filePath = "C:/Users/yakup/OneDrive/Belgeler/github_bot"

if os.path.exists(os.path.join(filePath, ".git")):
    print(".git klasörü var")
else:
    print(".git klasörü yok")