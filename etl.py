# Json data format { "results": [ {"case_id": 1,"status_id": 5,},{  "case_id": 2,"status_id": 1} ] }
                #  { "results": [ {"case_id": 4,"status_id": 4,} ] }

dataList = []

for i in range(5):
    data = "{\"case_id\": " + str(i) + ",\"status_id\": " + str(i) + ",}"
    dataList.append(data)

# for itm in dataList:
ls = ("[{0}]".format(', '.join(map(str, dataList))))
finalDataSet = "{ \"results\": [ " + ls +  " ] }"

print(finalDataSet)


