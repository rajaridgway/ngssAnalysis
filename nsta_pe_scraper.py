#Raja Ridgway
#March 28, 2020
#nsta_pe_scraper.py
#Scrapes from the NGSS/NSTA website to create dataframe of all PEs, CCCs, and SEPs

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Create empty list to gather site links
urls = []
#Append all links to urls list
for i in [x for x in range(23,234) if x != 24 and x != 25 and x!=201]:
   urls.append('https://ngss.nsta.org/DisplayStandard.aspx?view=pe&id=' + str(i))

#Create empty lists
pe_num_list = []
sep_list = []
ccc_list = []

#Loop through all pages
for url in urls:
    try:
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')

        #Get the performance expectation
        pe_num = soup.select('.std > a')
        #Convert the soup element to a string and only get text
        pe_num = str(pe_num[0].getText())
        #Append PE_num to appropriate list
        pe_num_list.append(pe_num)

        #Get the SEP
        sep = soup.select('#MainContent_rptPractices_lblPractice_0')
        #Convert the soup element to a string and only get text
        sep = str(sep[0].getText())
        #Append SEP to appropriate list
        sep_list.append(sep)

        #Get the crosscutting concept using the CSS selector
        ccc = soup.select('#MainContent_rptConcepts_lblConcept_0')
        #Convert the soup element to a string and only get text
        ccc = str(ccc[0].getText())
        #Append ccc to appropriate list
        ccc_list.append(ccc)
    except IndexError:
        ccc_list.append("None")
        continue

#Create dataframe with NGSS dictionary
ngss_df = pd.DataFrame(
    {"PE_Number": pe_num_list,
    "SEP": sep_list,
    "CCC": ccc_list
    })

#Export to csv
ngss_df.to_csv(r'/Users/rajaridgway/ngss2.csv', index=False)
