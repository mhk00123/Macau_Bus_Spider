import requests
from Module import Mo_Bus
import json


class MainF:
    def __init__(self):
        self.mb = Mo_Bus.Mo_Bus()

if __name__ == '__main__':
    obj = MainF()

    for bus in obj.mb.all_bus_list:
        obj.mb.bus_count(obj.mb.get_bus_status(bus))

    print("全澳目前共有 {} 架巴士正在運行".format(obj.mb.All_count))





