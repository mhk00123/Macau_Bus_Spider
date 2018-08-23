from Module import Mo_Bus


class Spider:

    def __init__(self):
        self.mb = Mo_Bus.Mo_Bus()

        #記錄每台巴士的2個總站
        self.bus = {}


if __name__ == '__main__':
    obj = Spider()
    # Get這台巴士的所有巴士站
    all_bus_list = obj.mb.get_all_bus_list()
    list_b = []
    count = 0
    All_count = 0

    for bus_num in all_bus_list:
        # Get這台巴士的所有巴士站
        rs = obj.mb.get_bus_status(bus_num)
        # 取得總站

        rs_stop = obj.mb.get_bus_stop_list(rs)
        obj.bus[bus_num] = list()
        obj.bus[bus_num].append(rs[0]['staCode'].split('/', 1)[0])
        obj.bus[bus_num].append(rs[-1]['staCode'].split('/', 1)[0])

        #統計正在運行的巴士數
        for item in rs:
            for it in item['busInfo']:
                bus_plate = it['busPlate']
                now_bus_stop = item['staCode'].split('/', 1)[0]

                if (now_bus_stop == obj.bus[bus_num][0]) or (now_bus_stop == obj.bus[bus_num][1]):
                    continue
                else:
                    count = count + 1
                    All_count = All_count + 1
                    print("{} 目前在 {}".format(bus_plate, obj.mb.bus_stop_list[now_bus_stop]))
        print("共有 {} 架".format(count))
        count = 0
        list_b.clear()
        print("----------------------------")

    print("總共有 {} 架巴士正在運行".format(All_count))