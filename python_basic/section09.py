class Median:
    list_of_num = []

    def __init__(self):
        self.list_of_num = []
 
    def get_item(self, item):
        # Median.list_of_num.append(item)
        self.list_of_num.append(item)
 
    def clear(self):
        # Median.list_of_num = []
        self.list_of_num = []
 
    def show_result(self):
        # Median.list_of_num.sort()
        self.list_of_num.sort()
        # len_of_list = len(Median.list_of_num)
        len_of_list = len(self.list_of_num)
        center_of_list = int(len_of_list / 2)
        if len_of_list % 2 == 1:
            # print(Median.list_of_num[center_of_list])
            print(self.list_of_num[center_of_list])
        else:
            # print((Median.list_of_num[center_of_list - 1] + Median.list_of_num[center_of_list]) / 2.0)
            print((self.list_of_num[center_of_list - 1] + self.list_of_num[center_of_list]) / 2.0)
 
median = Median()
for x in range(10):
    median.get_item(x)
median.show_result()
 
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()

# 2020/03/29 changed
