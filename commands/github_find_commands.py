from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from commands.github_login import GithubLogin


class FindCommand(GithubLogin):
    
    def __init__(self):
        super().__init__(self)

    def findRepo(self,keyword):
        self.keyWord=keyword
        # search button clicked
        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div[3]/qbsearch-input/div[1]/button/span").click()
        self.timer.shortTimer()
        # input entered
        inputSearch=self.browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div[3]/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input")
        inputSearch.send_keys(keyword)
        inputSearch.send_keys(Keys.ENTER)
    
    def findUsername(self,keyword):
            self.keyWord=keyword
            self.browser.get(self.baseUrl +keyword)