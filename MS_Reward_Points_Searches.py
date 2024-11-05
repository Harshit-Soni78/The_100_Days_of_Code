# Use this Command to install all requirements: - pip install selenium pytrends tqdm time random
# You also need to install Selenium Edge Driver if you are using Edge Browser.
# Use this Command on cmd to Run { python -u "PATH\MS_Reward_Points_Searches.py" }

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pytrends.request import TrendReq
from selenium import webdriver
import random
import time


def list_of_trending_topics():
    retries = 3
    while retries > 0:
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
            print("\n---- Done Searching Topics ----\n")
            return unique_list
        except Exception as exception:
            print(f"Previous Attempt to search topics Failed! Retrying !!..... Please Check the Internet......")
            print(f"Error: {exception}. \nRetrying in 2 seconds...")
            time.sleep(2)
            retries -= 1
    print("Failed to retrieve trending searches after multiple attempts.")
    return ['NFT', 'Hanukkah', 'Crossword', 'Minecraft', 'Park Gelled', 'Christmas', 'NHL', 'iPhone 13', 'Barbie',
            'Fortnite', 'Gambling', 'The Last of Us', 'Cyber+Monday', 'Among+Us', 'Golf', 'Web3', 'New+Year',
            'Cricket World Cup', 'Louvre Museum', 'Omicron', 'Diwali', 'Black+Friday', 'Scrabble', 'Kwanzaa', 'Chess',
            'Taylor Swift', 'Olympics', 'Adele', 'MLB', 'Thanksgiving', 'Squid Game', 'Roblox', 'Metaverse', 'Amazon',
            'Facebook', 'Tennis', 'Tesla', 'Gmail', 'Google', 'Paralympics', 'MotoGP', 'Sudoku',
            'Spider-Man: No Way Home', 'NBA', 'UEFA+Champions+League', 'YouTube', 'Weather', 'FIFA+World+Cup',
            'Formula+1', 'Subhuman Gill', 'Halloween', 'Netflix', 'Caterpillar', 'Bones', 'Bitcoin', 'NFL']


class MS_Account:
    def __init__(self):
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=self.edge_options)
        self.URL = "https://www.bing.com/?scope=web&cc=IN&FORM=ANNTH1&pc=PCMWSB"
        self.Element_XPATH = '/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea'
        self.MS_REWARD_URL = "https://rewards.bing.com/"
        self.sleep_time: int = 2
        self.tab_close_time: int = 4
        self.browser_close_time: int = 5

    def start_searches(self, topics_list):
        print(f"Search Topics are :- {topics_list}\n")
        print(f"---- Starting Searches ----")
        for topic in topics_list:
            self.search_topic(topic)

    def close_browser(self):
        print("Closing Edge in 5 Seconds...")
        time.sleep(5)
        self.driver.close()

    def open_rewards(self):
        print("Opening MS Reward Page")
        self.driver.get(self.MS_REWARD_URL)

    def search_topic(self, topic):
        try:
            self.driver.get(self.URL)
            search_element = self.driver.find_element(By.XPATH, value=self.Element_XPATH)
            search_element.send_keys(topic)
            time.sleep(self.sleep_time)
            search_element.send_keys(Keys.ENTER)
            time.sleep(self.tab_close_time)
            # print(f"Done Search:- {topic}")
        except Exception as search_error:
            retries = 3
            while retries > 0:
                print(f"Error: {search_error}\n... Retrying in 2 seconds ...")
                self.driver.close()
                self.search_topic(topic)
                time.sleep(2)
                retries -= 1


if __name__ == '__main__':
    print("""
    Hello !!
    This is the script to complete the microsoft search reward task.
    After running this script, please sign in the id. It will give time of 15 seconds to do so.
    """)

    accounts = int(input("How many accounts do you want to do Task:- "))
    close_browser = bool(input("Do you want to close the browsers after all searches (1: True, 0: False):- "))
    no_of_search_topics = int(input("How many Searches do you want to do in each account ( < 100 topics):- "))

    browsers = []
    if no_of_search_topics > 1:
        TRENDING_SEARCHES = list_of_trending_topics()
    else:
        TRENDING_SEARCHES = []

    # Opening Browsers
    try:
        for account in range(accounts):
            print(f"\n-- Opening Browser {account + 1} --\n")
            browsers.append(MS_Account())
            print("You have 10 seconds to choose Account\n")
            time.sleep(5)
    except Exception as e:
        print(f"\nError in opening the Browser. {e}\n")

    for account in range(accounts):
        try:
            print(f"\n\n-- Doing Searches for Account number {account + 1} --\n")
            random.shuffle(TRENDING_SEARCHES)
            search_list = TRENDING_SEARCHES[:no_of_search_topics]
            print(search_list)
            browsers[account].start_searches(search_list)
            if not close_browser:
                browsers[account].close_browser()
            else:
                browsers[account].open_rewards()
            print(f"\n____ Done for Account number {account + 1} ____\n")
        except Exception as e:
            print(f"Error in searching in Account number {account + 1}")
            print(f"Error is {e}")
            browsers[account].close_browser()

    print("\n\n************ Thank you for Using ************\n\n")
