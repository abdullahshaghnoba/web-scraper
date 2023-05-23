import requests
from bs4 import BeautifulSoup
import json

History_of_Maxico_URL = "https://en.wikipedia.org/wiki/History_of_Mexico"


# print(all_citation_needed_signs)

def get_citations_needed_count(History_of_Maxico_URL):
    Data = requests.get(History_of_Maxico_URL)

    soup = BeautifulSoup(Data.content, 'html.parser')
    # print(soup)

    all_citation_needed_signs = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    count = 0
    for _ in all_citation_needed_signs:
        count+=1

    return count

# print(get_citations_needed_count(History_of_Maxico_URL))

def get_citations_needed_report(History_of_Maxico_URL):
    Data = requests.get(History_of_Maxico_URL)

    soup = BeautifulSoup(Data.content, 'html.parser')
    all_pars_with_citation_signs = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    all_pars = ""
    # print(all_pars)
    for p in all_pars_with_citation_signs:
        par = p.find_previous('p')
        # print(par.text)
        all_pars+=par.text
    return all_pars

print(get_citations_needed_report(History_of_Maxico_URL))