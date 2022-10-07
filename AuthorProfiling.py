from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading
from difflib import SequenceMatcher

driver1 = webdriver.Chrome(ChromeDriverManager().install())
# driver2 = webdriver.Chrome(ChromeDriverManager().install())

author_profiles=[] 

def profiling1(link1,keywords):
    authorScore = 0
    
    driver1.get(link1)
    driver1.implicitly_wait(5)
    try:
        l = driver1.find_element("link text", "Show More")
        driver1.execute_script('arguments[0].click()', l)
    except:
        pass
    name = (driver1.find_elements(By.XPATH,"//h1[contains(@class,'hide-mobile')]"))
    publication_topics_list = driver1.find_elements(By.XPATH,"//div[contains(@class,'research-areas')]")
    publication_count = (driver1.find_elements(By.XPATH,"//div[contains(@class,'publications col-6 text-base-md-lh')]"))
    citations = (driver1.find_elements(By.XPATH,"//div[contains(@class,'citations col-6')]"))
    startYear = (driver1.find_elements(By.XPATH,"//span[contains(@class,'start-year col-6')]"))
    endYear = (driver1.find_elements(By.XPATH,"//span[contains(@class,'end-year col-6')]"))
    
    timePeriod = int((int(endYear[1].text))-(int(startYear[1].text)))+1
    
    citationsPerPaper = int(int((int(citations[1].text.split("\n")[1]))) / (int((publication_count[0].text).split("\n")[1])))
    publicationsPerYear = int((int((publication_count[0].text).split("\n")[1])) / (timePeriod))
    
    print(name[0].text)
    print(publication_topics_list[0].text)
    print(citationsPerPaper)
    print(publicationsPerYear)
    print(SequenceMatcher(None,publication_topics_list[0].text , keywords).ratio())
    
    try:
        l = driver1.find_element("link text", "Show More")
        driver1.execute_script('arguments[0].click()', biography)
        biography = ((driver1.find_elements(By.XPATH,"//div[contains(@class,'biography')]"))[0]).text 
        print(biography)
    except:
        pass
    
    return author_profiles;

# def profiling2(link2):
#     driver2.get(link2)
#     driver2.implicitly_wait(5)
#     try:
#         l = driver2.find_element("link text", "Show More")
#         driver2.execute_script('arguments[0].click()', l)
#     except:
#         pass
#     areas2 = driver2.find_elements(By.XPATH,"//div[contains(@class,'research-areas')]")
#     for area2 in areas2:
#         print(area2.text)

def authorProfiling(list):
    number_of_authors = len(list)-1
    keywords = list[0]
    authors=[]
    for itr in range(1,number_of_authors+1,1):
        authors.append(list[itr])
    if(number_of_authors==1):
        profiling1(str(authors[0]),keywords,)
        
    else:
        author1 = str(authors[0])
        author2 = str(authors[1])
        
        t1 = threading.Thread(target=profiling1,args=(author1,keywords,))
        t2 = threading.Thread(target=profiling2,args=(author2,keywords,))
       
        t1.start()
        t2.start()
        
        t1.join()
        t2.join()
        
        
        
