"""Script to scrape indeed.com and email me rlevant job openings"""

import sys
import urllib.request
import bs4 as bs

def main():
    """Main entry point for the script."""
    pass


class Scraper():
    def __init__(self, keyword, location):
        self.location = location
        self.keyword = keyword
        pass

    def get_urls_of_jobs(self,n_jobs = 200 ):
        # """This returns a list of all possible Jobs by keyword in a defined location"""
        # url_of_job_page = "https://ie.indeed.com/{0}?q=data&l={1}".format(self.keyword, self.log) 
        # response = urllib.request.urlopen(url_of_job_pages).read()
        # soup = bs.BeautifulSoup(response)
        # jobs = soup.find_all('')
        pass
    
    def download_html_of_jobs(self):
        pass

    def convert_html_to_text(self):
        pass

class JobSorter():
    def __init__(self):
        pass

    def experience_level(self)
        pass
    def requirements(self)
        pass
    def responsibilities(self)
        pass





if __name__ == '__main__':
    sys.exit(main())