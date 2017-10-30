"""Script to scrape indeed.com and email me rlevant job openings"""


from collections import namedtuple
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys
import datetime
import bs4 as bs

NOW = datetime.datetime.now()

def main():
    """Main entry point for the script."""
    scraper = Scraper("data", "cork")
    responses = scraper.get_indeed_data()
    # print(responses[0])
    jobs = []
    for response in responses:
        job_group = scraper.get_job_details_on_page(response)
        jobs = jobs + job_group
    print(jobs)


class Scraper():
    """Indeed scraper with location  as first input and job keyword as second input"""
    def __init__(self, keyword, location):
        self.location = location
        self.keyword = keyword


    def get_indeed_data(self, days_ago_limit=2, starting_page=0, number_of_page_limit=10):
        "Returns list of responses of indeed.com for jobs in a a location and based on a keyword."
        responses = []
        for i in range(starting_page, number_of_page_limit):
            if i < number_of_page_limit:
                url_of_job_page = "https://ie.indeed.com/jobs?q={0}&l={1}&start={2}&fromage={3}".format(
                    self.keyword, self.location, i*10, days_ago_limit)
            else:
                break
            try:
                response = urlopen(url_of_job_page).read()
            except HTTPError as error:
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', error.code)
            except URLError as error:
                print('We failed to reach a server.')
                print('Reason: ', error.reason)
            responses.append(response)
        # print(now.day)
        return responses

    def get_job_details_on_page(self, response):
        """Returns a list of namedtuples for each jobs by keyword in a defined location"""
        soup = bs.BeautifulSoup(response, "lxml")
        job_html_blocks = soup.find_all('div', {'data-tn-component' : "organicJob"})
        companies = [x.span.text.replace("\n", "") for x in job_html_blocks]
        days_old = [x.text.split()[0] for x in soup.find_all('span', {'class' : "date"})]
        job_attributes = [x.h2.a.attrs for x in job_html_blocks]
        job_info = []
        Job = namedtuple("Job", "title company days_old link")
        for count, job_attribute in enumerate(job_attributes):
            title = job_attribute.get('title')
            link = job_attribute.get('href')
            job_info.append((title, companies[count], days_old[count], link))
        return [Job(*x) for x in job_info]

class JobSorter():
    def __init__(self):
        pass

    def experience_level(self):
        pass
    def desired_skills(self):
        pass
    def responsibilities(self):
        pass


if __name__ == '__main__':
    sys.exit(main())
