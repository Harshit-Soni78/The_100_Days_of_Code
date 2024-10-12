from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pytrends.request import TrendReq
from selenium import webdriver
from tqdm import tqdm
import random
import time
# Use this Command to install all requirements: - pip install selenium pytrends tqdm time random
# You also need to install Selenium Edge Driver if you are using Edge Browser.


def loop_searches(url, search_element_xpath, list_of_topics, sleep_time=2, break_in_between=5, time_to_sign_in=15):
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=edge_options)
    time.sleep(time_to_sign_in)
    # for topic in list_of_topics:
    for topic in tqdm(list_of_topics, desc="Searching Topics"):
        driver.get(url)
        search_element = driver.find_element(By.XPATH, value=search_element_xpath)
        search_element.send_keys(topic)
        time.sleep(sleep_time)
        search_element.send_keys(Keys.ENTER)
        time.sleep(break_in_between)
    time.sleep(sleep_time)
    driver.close()


def list_of_trending_searches(length: int):
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
    if length <= len(unique_list):
        return unique_list[:length]
    else:
        return unique_list


print("""Hello !!
This is the script to complete the microsoft search reward task.
After running this script, please sign in the id. It will give time of 15 sec to do so.""")

N = int(input("Please Enter the number of searches you want to do:- "))

URL = "https://www.bing.com/?scope=web&cc=IN&FORM=ANNTH1&pc=PCMWSB"
Element_XPATH = '/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea'

try:
    LIST_OF_TOPICS = list_of_trending_searches(N)
    print(f"LIST_OF_TOPICS = {LIST_OF_TOPICS}")
    loop_searches(URL, Element_XPATH, LIST_OF_TOPICS)
except:
    LIST_OF_TOPICS = ['Types of fossil fuel power plants', 'How coal-fired power plants work',
                      'Natural gas power plants explained', 'Oil-fired power plants',
                      'Combined heat and power (CHP) plants',
                      'Comparison of fossil fuel power plants', 'Environmental impact of fossil fuel power plants',
                      'Air pollution from power plants', 'Effects of coal power plants on the environment',
                      'Water pollution from fossil fuel power plants',
                      'Impact of power plants on wildlife and livestock',
                      'Climate change and fossil fuels', 'Health effects of fossil fuel emissions',
                      'Introduction to renewable energy sources', 'What are non-conventional energy sources?',
                      'Overview of solar energy', 'Wind energy basics', 'Biomass energy explained',
                      'Geothermal energy overview',
                      'Ocean energy: wave, tidal, and OTEC', 'Hydrogen energy and fuel cells',
                      'Assessing renewable energy potential',
                      'Technical feasibility of renewable energy', 'Economic viability of renewable energy',
                      'Environmental impact of renewable energy', 'Social acceptance of renewable energy projects',
                      'Energy storage and grid integration', 'Cost-benefit analysis of renewable energy',
                      'Renewable energy resource assessment', 'Limitations of renewable energy',
                      'Challenges of solar energy',
                      'Wind energy limitations', 'Biomass energy drawbacks', 'Geothermal energy challenges',
                      'Environmental impact of renewable energy', 'Intermittency in renewable energy',
                      'Economic challenges of renewable energy', 'Technological hurdles in renewable energy',
                      'YouTube', 'Amazon', 'Facebook', 'Weather', 'Google', 'Gmail', 'Barbie', 'The Last of Us',
                      'Caterpillar', 'Bones', 'Park Güell', 'Louvre Museum', 'Subhuman Gill', 'Gambling',
                      'Cricket World Cup',
                      'Netflix', 'iPhone 13', 'Tesla', 'Bitcoin', 'Omicron', 'Spider-Man: No Way Home', 'Taylor Swift',
                      'Adele', 'Squid Game', 'Metaverse', 'NFT', 'Web3', 'Christmas', 'New Year', 'Hanukkah', 'Kwanzaa',
                      'Diwali', 'Halloween', 'Thanksgiving', 'Black Friday', 'Cyber Monday', 'Olympics', 'Paralympics',
                      'FIFA World Cup', 'UEFA Champions League', 'NBA', 'NFL', 'MLB', 'NHL', 'Formula 1', 'MotoGP',
                      'Tennis',
                      'Golf', 'Chess', 'Sudoku', 'Crossword', 'Scrabble', 'Minecraft', 'Fortnite', 'Roblox', 'Among Us',
                      'NHL', 'Formula 1', 'MotoGP', 'Tennis', 'Golf', 'Chess', 'Sudoku', 'Crossword', 'Scrabble',
                      'Minecraft',
                      'Fortnite', 'Roblox', 'Among Us']
    (random.shuffle(LIST_OF_TOPICS))
    (random.shuffle(LIST_OF_TOPICS))
    print(f"LIST_OF_TOPICS = {LIST_OF_TOPICS[:N]}")
    loop_searches(URL, Element_XPATH, LIST_OF_TOPICS[:N])

print("Done Searches")
