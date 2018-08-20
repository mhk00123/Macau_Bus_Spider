import codecs
import json


class Bus_stop:

    def __init__(self):
        self.bus_stop_dict = {}
        self.keyS = []
        self.val = []

    def get_all_bus_stop(self):
        with open('..\Module\Bus_stop.txt', 'r', encoding='UTF-8') as file:
            content = file.read().split('\n')

            ct = 1
            for item in content:
                if(ct == 1):
                    self.keyS.append(item)
                    ct = 2
                elif(ct == 2):
                    self.val.append(item)
                    ct = 1

if __name__ == '__main__':
    obj = Bus_stop()
    obj.get_all_bus_stop()
    obj.bus_stop_dict = dict(zip(obj.keyS,obj.val))

    print(obj.bus_stop_dict)

    json.dumps(obj.bus_stop_dict)
    # 把爬回的巴士站數據存成Json已方便其他函式使用
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(obj.bus_stop_dict))
