import requests
import json
import os

class Mo_Bus:
    def __init__(self):

        self.bus_list = []
        self.all_bus_list =[]
        self.AoBa_list = []
        self.XinFuLi_list = []
        self.All_count = 0

        MYDIR = os.path.dirname(__file__)
        # 先由本地載入Bus Stop Data
        self.bus_stop_list = self.load_bus_stop()
        # 取得所有Bus數據
        self.get_bus_list()
        # 分類
        self.get_all_bus_list()



    def load_bus_stop(self):
        with open(os.getcwd() + '\Module\data.json') as bus_stop_data:
            load_dict = json.load(bus_stop_data)
            # print(load_dict)
            return load_dict

    def get_all_bus_list(self):
        for item in self.bus_list:
            self.all_bus_list.append(item['routeName'])

    def get_bus_list(self):
        url = "https://bis.dsat.gov.mo:37812/macauweb/getRouteAndCompanyList.html"

        rs = requests.post(url)
        # requests decode() 預設UTF-8
        data = rs.content.decode()
        data = json.loads(data)

        for item in data['data']['routeList']:
            # print(item)
            self.bus_list.append(item)

        # print(self.bus_list)
        return self.bus_list


    def get_bus_status(self, bus_num):
        print("{} 號巴士".format(bus_num))
        url = "https://bis.dsat.gov.mo:37812/macauweb/getRouteData.html"
        headerS = {
            'Host': 'bis.dsat.gov.mo:37812',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        playload = "action=dy&dir=0&lang=zh-tw&routeName=" + bus_num
        rs = requests.post(url, data=playload, headers=headerS)
        data = json.loads(rs.content.decode())
        # print(data)
        return data

    def get_AoBa(self):
        for item in self.bus_list:
            # print(item)
            if item['color'] == "Orange":
                self.AoBa_list.append(item['routeName'])
        # print(self.AoBa_list)
        return self.AoBa_list

    def get_XinFuLi(self):
        for item in self.bus_list:
            # print(item)
            if item['color'] == "Blue":
                self.XinFuLi_list.append(item['routeName'])
        print(self.XinFuLi_list)
        return self.XinFuLi_list

    def bus_count(self, data):
        # print(data)
        count = 0
        for item in data['data']['routeInfo']:
            # print(item)
            try:
                for bus in item['busInfo']:
                    count = count + 1;
                    print(bus['busPlate'] + "目前在 : " + self.bus_stop_list[item['staCode'].split('/',1)[0]])
            except IndexError:
                pass

        self.All_count += count
        print("共 {} 部".format(count))
        print("-----------------------------------")



# if __name__ == '__main__':
#     obj = Mo_Bus()
#     print(obj.homedir)
#     print(obj.all_bus_list)
#
#     for bus in obj.all_bus_list:
#         obj.bus_count(obj.get_bus_status(bus))
#
#     print("全澳目前共有 {} 部巴士正在行駛".format(obj.All_count))
