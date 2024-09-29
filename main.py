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
keywords = 'geoId=' + geoId_Spain + '&keywords=' + keyword_search

# Don't need auth in this case
# r = requests.get(link, auth=(user, pass))
res = requests.get(link, params=keywords, auth=(env['USER'], env['PASSWD']))

# If we exceed the max request, we jump of the program
if res.status_code == int(env['TOO_MANY_REQUEST_CODE']):
    print(env['TOO_MANY_REQUEST_MSG'])
    exit(1)
    

soup = BeautifulSoup(res.text, 'lxml')

#with open('index.html', "w", encoding=res.encoding) as fp:
#    fp.write(res.text)
#    fp.close()
    
    
jobs_container = soup.find('ul', {'class': 'jobs-search__results-list'})
#print(jobs_container)
jobs_lists = jobs_container.find_all('li')

for list in jobs_lists:
    jobsIds.append(list.find('div')['data-entity-urn'].split(':')[-1])
    
end_time = time.time()
print(jobsIds)
print("Total time: ", (end_time - start_time), "s")


    