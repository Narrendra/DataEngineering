import json
import parquet
import spark
import pyspark

# data\pems_sorted\station=402265\part-r-00272-ddaee723-f3f6-4f25-a34b-3312172aa6d7.snappy.parquet
# df = parquet.read_data_page()
# with open('data\pems_sorted\station=402265\part-r-00272-ddaee723-f3f6-4f25-a34b-3312172aa6d7.snappy.parquet') as pq:
#     for row in parquet.DictReader(pq):
#         print(row)
# df = spark.read.load("data\pems_sorted\station=402265\part-r-00272-ddaee723-f3f6-4f25-a34b-3312172aa6d7.snappy.parquet")
# print(df)
# import pandas as pd
# import pdfkit
# import os
# cols = ['A','B']
# df = pd.DataFrame(columns=cols)
# i = 0
# for i in range(5):
#     df = df.append({'A': i,"B": i +1 }, ignore_index=True)

# f = open('exp.html','w')
# a = df.to_html()
# f.write(a)
# f.close()

# f = open('..\\..\\..\\DataEngineering\\exp.html')
# print(f)
# pdfkit.from_file('exp.html', 'example.pdf')
# df.iloc[1,1] = "Hey"
# print(df)
# print(os.path.basename("exp.html"))


# import requests
# from testrail_api import TestRailAPI
# https://jobvite.testrail.net/index.php?/milestones/view/271
# GET index.php?/api/v2/get_runs/:project_id

# re = requests.get('https://jobvite.testrail.net/index.php?/api/v2/get_runs/:5350')
# print(re)

# client = 'http://s://jobvite.testrail.net/testrail/'
# # client = 
# client.user = 'anil.perikala@jobvite-inc.com'
# client.password = 'Jobvite2021'
# case = client.send_get('get_case/1')
# print(case)
# api = TestRailAPI("https://jobvite.testrail.net/", "anil.perikala@jobvite-inc.com", "Jobvite2021")
# tc = api.tests.get_test("1")
# print(tc)
# pth = "../DataEngineering/exp.html"
# f = open(pth)

# from testrail import *

# client = APIClient('http://jobvite.testrail.net/testrail/') #https://jobvite.testrail.net/index.php?/suites/overview/10
# client.user = 'anil.perikala@jobvite-inc.com'
# client.password = 'Jobvite2021'

# result = client.send_post(
# 	'add_result_for_case/1/1',
# 	{ 'status_id': 1, 'comment': 'This test worked fine!' }
# )


# case = client.send_get('get_case/2543660')
# print(case)
# caseIds = []
# for i in range(4):
#     caseIds.append(i) 

 

# runName = "ETL_Daily_Automation_" 
# strSuiteID = "2470"
# incFlag = True
# # caseIds = [1,2]
# runData = {"suite_id": strSuiteID, "name": runName,"include_all": incFlag, "case_ids" : caseIds} 
# # runIDNew = addRun(runData)
# print(runData)
# import json
# dList = []
# for i in range(2):
#     dList.append({"case_id": i,	"status_id": 5})

# dList = json.dumps(dList)

# # {"results": [ { "case_id": 786085, "status_id": 5,"comment": "Test Comment" } ] }

# # caseData = {"case_id": 1,	"status_id": 5}, {"case_id": 2,	"status_id": 5}
# data = "{	\"results\": "  + str(dList) + "  } " 
# print(data)
payload = []
strCaseID = 0
for strCaseID in range(3):
    print(strCaseID)
    cdata = "{ \"case_id\": "+ str(strCaseID) + ", \"status_id\": 5} "
    payload.append(cdata)
cCat = "Naren " + str(payload)
cCat = cCat.replace("'","")

print(cCat)