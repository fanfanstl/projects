
import csv


def get_str(num):
    if num < 10:
        num = '0' + str(num)
    return str(num)


# 城市代码创建
def create_city_code():
    city_code = []
    file = open('china-city-list.csv','r',encoding='utf-8')
    reader = csv.reader(file)
    for item in reader:
        data = {}
        data[item[0][2:]] = item[2]
        city_code.append(data)
    file.close()
    return city_code




if __name__ == '__main__':
    # print(get_str(9))
    print(create_city_code())
