from dotenv import dotenv_values
import time
import requests
from bs4 import BeautifulSoup

env = dotenv_values(".env")

start_time = time.time()

jobsIds = list()

keyword_search = 'software%20development'
geoId_Spain = '105646813'

link = 'https://www.linkedin.com/jobs/search/'
keywords = 'keywords=' + keyword_search + '&geoId=' + geoId_Spain

# Don't need auth in this case
# r = requests.get(link, auth=(user, pass))
res = requests.get(link, params=keywords, auth=(env['USER'], env['PASSWD']))

soup = BeautifulSoup(res.text, 'lxml')

#with open('index.html', "w", encoding=res.encoding) as fp:
#    fp.write(res.text)
    
    
jobs_container = soup.find('ul', {'class': 'jobs-search__results-list'})
jobs_lists = jobs_container.find_all('li')

for list in jobs_lists:
    jobsIds.append(list.find('div')['data-entity-urn'].split(':')[-1])
    
end_time = time.time()
print(jobsIds)
print("Total time: ", (end_time - start_time), "s")


    