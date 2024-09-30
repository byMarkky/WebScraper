from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

def dump_file(response, encoding):
    with open('index.html', 'w', encoding=encoding) as file:
        file.write(response)
        file.close()

def get_jobs_ids(res):
    content = res.text
    soup = BeautifulSoup(content, 'lxml')
    jobs_ids = list()

    # If we exceed the max request, we jump of the program
    if res.status_code == int(os.getenv('TOO_MANY_REQUEST_CODE')):
        print(res.headers)
        print(os.getenv('TOO_MANY_REQUEST_MSG'))
        exit(1)
        

    dump_file(content, res.encoding)
        
    jobs_container = soup.find('ul', {'class': 'jobs-search__results-list'})
    jobs_lists = jobs_container.find_all('li')

    for job in jobs_lists:
        jobs_ids.append(job.find('div')['data-entity-urn'].split(':')[-1])
        
    return jobs_ids
    

def main():
    load_dotenv()

    keyword_search = 'software%20development'
    geoId_Spain = '105646813'

    link = 'https://www.linkedin.com/jobs/search/'
    keywords = 'geoId=' + geoId_Spain + '&keywords=' + keyword_search

    # Don't need auth in this case
    # r = requests.get(link, auth=(user, pass))
    res = requests.get(link,
                       headers={'User-agent': 'your bot 0.1'},
                       params=keywords,
                       auth=(os.getenv('USER'), os.getenv('PASSWD')))

    jobs_ids = get_jobs_ids(res)
    print(jobs_ids)


if __name__ == '__main__':
    main()    