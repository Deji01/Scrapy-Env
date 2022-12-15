
import re
import json
import requests
from urllib.parse import urlencode
import pandas as pd

SCRAPEOPS_API_KEY = 'SCRAPEOPS_API_KEY'

def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


indeed_search_url = 'https%3A%2F%2Fwww.indeed.com%2Fjobs%3Fq%3Dsoftware%20engineer%26l%3DSan%20Francisco%26start%3D0%26filter%3D0'

## Send URL To ScrapeOps Instead of Indeed 
response = requests.get(scrapeops_url(indeed_search_url))

job_id_list = [
    'f6288f8af00406b1',
     '56ab4e4fe59ae782',
     '29bd7638828fab65',
     '697a7a3f18590465',
     '08e92505e27442d3',
     '105529f69e3fdae2'
]

full_job_data_list = []

for job_id in job_id_list:
    try:
        indeed_job_url = 'https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk=' + job_id
        response = requests.get(scrapeops_url(indeed_job_url))

        if response.status_code == 200:
            script_tag  = re.findall(r"_initialData=(\{.+?\});", response.text)
            if script_tag is not None:
                json_blob = json.loads(script_tag[0])
                job = json_blob["jobInfoWrapperModel"]["jobInfoModel"]
                full_job_data_list.append({
                    'company': job.get('jobInfoHeaderModel').get('companyName') if job.get('jobInfoHeaderModel') is not None else '',
                    'jobkey': job_id,
                    'jobTitle': job.get('jobInfoHeaderModel').get('jobTitle') if job.get('jobInfoHeaderModel') is not None else '',
                    'jobDescription': job.get('sanitizedJobDescription').get('content') if job.get('sanitizedJobDescription') is not None else '',
                })
            
            
    except Exception as e:
        print('Error', e)

df = pd.json_normalize(full_job_data_list)
df.to_csv("indeed-jobs.csv", index=False)