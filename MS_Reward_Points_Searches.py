# Use this Command to install all requirements: - pip install selenium pytrends tqdm time random
# You also need to install Selenium Edge Driver if you are using Edge Browser.
# Use this Command on cmd to Run { python -u "PATH\MS_Reward_Points_Searches.py" }

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pytrends.request import TrendReq
from selenium import webdriver
from tqdm import tqdm
import random
import time


class MS_Account:
    def __init__(self, close_edge: bool = False, no_of_searches: int = 33):
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=self.edge_options)
        self.URL = "https://www.bing.com/?scope=web&cc=IN&FORM=ANNTH1&pc=PCMWSB"
        self.Element_XPATH = '/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea'
        self.MS_REWARD_URL = "https://rewards.bing.com/"
        self.no_of_searches = no_of_searches
        self.list_of_topics = self.list_of_searches()
        self.sleep_time: int = 2
        self.tab_close_time: int = 5
        self.browser_close_time: int = 5
        self.open_reward_page: bool = not close_edge
        self.close_edge: bool = close_edge

    def start_searches(self):
        print(f"Starting Searches")
        time.sleep(5)
        self.loop_searches()
        if self.open_reward_page:
            print("Opening MS Reward Page")
            self.driver.get(self.MS_REWARD_URL)
        if self.close_edge:
            print("Closing Edge in 15 Seconds...")
            time.sleep(15)
            self.driver.close()

    def loop_searches(self):
        try:
            for topic in tqdm(self.list_of_topics, desc="Searching Topics"):
                self.driver.get(self.URL)
                search_element = self.driver.find_element(By.XPATH, value=self.Element_XPATH)
                search_element.send_keys(topic)
                time.sleep(self.sleep_time)
                search_element.send_keys(Keys.ENTER)
                time.sleep(self.tab_close_time)
            time.sleep(self.sleep_time)
        except:
            self.driver.close()
            print("Previous Attempt Failed! Retrying !!......")
            self.loop_searches()
        print("Done Searches")

    def list_of_searches(self):
        try:
            pytrends = TrendReq(hl='en-US', tz=360)
            trending_searches_df_top50 = pytrends.realtime_trending_searches(pn='IN')
            dict_trand = trending_searches_df_top50.to_dict()
            entity_name_dict = dict_trand["entityNames"]
            entity_list = []
            for i in range(len(entity_name_dict)):
                value_list = entity_name_dict[i]
                for value in value_list[:-1]:
                    entity_list.append(value)
            seen = set()
            unique_list = [x for x in entity_list if x not in seen and not seen.add(x)]
            random.shuffle(unique_list)
            if self.no_of_searches <= len(unique_list):
                return unique_list[:self.no_of_searches]
            else:
                return unique_list
        except:
            print(
                f"Previous Attempt to search {self.no_of_searches} topics Failed! Retrying !!..... Please Check the Internet......")
            self.list_of_searches()


if __name__ == '__main__':
    print("""
    Hello !!
    This is the script to complete the microsoft search reward task.
    After running this script, please sign in the id. It will give time of 15 seconds to do so.
    """)

    accounts = int(input("How many accounts do you want to do Task:- "))
    close_browser = bool(input("Do you want to close the browsers after all searches (1: True, 0: False):- "))
    no_of_search_topics = int(input("How many Searches do you want to do in each account:- "))
    browsers = []

    for account in range(accounts):
        print(f"Opening Browser {account}")
        browsers.append(MS_Account(close_browser, no_of_search_topics))

    for account in range(accounts):
        print(f"Doing Searches for Account number {account}")
        browsers[account].start_searches()
        print(f"Done for Account number {account}")

    print("************ Thank you for Using ************")
