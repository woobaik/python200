import os
import csv
import requests
from bs4 import BeautifulSoup

os.system("clear")
alba_url = "http://www.alba.co.kr"

html_docs = requests.get(alba_url).text

soup = BeautifulSoup(html_docs, "html.parser")

company_list = soup.find('div', id='MainSuperBrand')
lis = company_list.find_all('li', "impact")

result = []
for company_raw_info in lis:

    company_info = {}
    company_name = company_raw_info.img['alt']
    company_page = company_raw_info.a['href']
    company_info[company_name] = company_name

    company_page_text = requests.get(company_page).text
    company_page_soup = BeautifulSoup(company_page_text, "html.parser")
    company_title = company_page_soup.title
    company_info[company_title] = company_title
    company_page_table = company_page_soup.find(
        'table', {"summary": "일반 채용정보에 등록한 회사의 근무지, 업무내용, 회사명, 성별, 근무시간, 급여, 등록일 정보입니다."})
    company_job_rows = company_page_table.find_all('tr')

    # file open

    file = open(company_name, mode="w")
    writer = csv.writer(file)

    for tr in company_job_rows[1:]:
        if len(tr) < 2:
            continue

        if 'summaryView' in tr['class'] or 'divide' in tr['class']:
            continue

        company_detail_location = tr.find(
            'td', {'class': 'local first'}).get_text()
        company_detail_title = tr.find('span', {'class': 'company'}).get_text()
        company_detail_payIcon = tr.find(
            'span', {'class': 'payIcon'}).get_text()
        company_detail_payAmount = tr.find(
            'span', {'class': 'number'}).get_text()
        company_detail_posted_ago = tr.find(
            'td', {'class': 'regDate last'}).get_text()

        try:
            company_detail_time = tr.find('span', {'class': 'time'}).get_text()
        except AttributeError as err:
            print(f"{err} has found in time error, will replace it with 'consult'")
            company_detail_time = tr.find(
                'span', {'class': 'consult'}).get_text()

        print(company_detail_location, company_name, company_detail_title, company_detail_time,
              company_detail_payIcon, company_detail_payAmount, company_detail_posted_ago)
        writer.writerow([company_detail_location, company_name, company_detail_title, company_detail_time,
                         company_detail_payIcon + company_detail_payAmount, company_detail_posted_ago])
