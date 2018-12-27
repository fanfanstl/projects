import csv


# ************************************读取******************************
# 以列表形式读出
csvFile = open("china-city-list.csv", "r",encoding='utf-8')
reader = csv.reader(csvFile)
for item in reader:
    print(item)
csvFile.close()



