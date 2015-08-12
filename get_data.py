from bs4 import BeautifulSoup
import urllib2
import json
import re
import csv

#response = urllib2.urlopen('http://www.ntsb.gov/investigations/reports_aviation.html')
#html = response.read()
#soup = BeautifulSoup(html).prettify().encode('utf-8')
#output_file = open('aviation_report.html', 'w')
#output_file.write(soup)
#output_file.close()

states_dic = {}
soup = BeautifulSoup(open('aviation_report.html'))
for td in soup.find_all('td'):
    state = td.text.strip()
    if len(state) == 2:
        states_dic[state] = states_dic.get(state,0)+1

result = sorted(states_dic.iteritems(),key=lambda d:d[1],reverse=True)
print result
    

writer = csv.writer(open('summary_location.csv','wb',buffering=0))
writer.writerows(result)                    
