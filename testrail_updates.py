import json
import requests
import base64
from requests.api import post
from testrail import * 
from datetime import date
   
client = APIClient('https://jobvite.testrail.net/')
client.user = 'anil.perikala@jobvite-inc.com'
client.password = 'Jobvite2021'

def addRun(data):
    res = client.send_post('add_run/10',data)
    runID = res['id']    
    return runID

def addResultsForCases(run_id, data):
    inp_string = "add_results_for_cases/" + run_id

#Prepare run data 
runName = "ETL_Daily_Automation_" + str(date.today()) 
strSuiteID = "2470"
incFlag = True
runData = {"suite_id": strSuiteID, "name": runName,"include_all": incFlag} 
runIDNew = addRun(runData)

#Prepare for adding results 
data = ""
addResultsForCases(runIDNew,data)


# casesList = []
# # i = 0 

# tests = client.send_get('get_tests/5566')
# for rs in tests: 
#     casesList.append(rs["case_id"])

  
# print(casesList)
# def getTestsFromRuns(run_id):
#     inp_string = "get_tests/" + run_id
#     tests = client.send_get(inp_string)


     