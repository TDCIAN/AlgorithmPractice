# Section09
# 파일 읽기, 쓰기
# 읽기 모드: r, 쓰기 모드(기존 파일 삭제): w, 추가 모드(파일 생성 또는 추가): a
# ..: 상대 경로, .: 절대 경로
# 기타: https://docs.python.org/3/library/functions.html#open

# 파일 읽기
# 예제1
f = open('/Users/apple/Desktop/FastCampus/python_basic/resource/review.txt', 'r')
content = f.read()
print(content)
# print(dir(f))
# 반드시 close 리소스 반환
f.close()

print("============================")
# 예제2
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/review.txt', 'r') as f:
    c = f.read()
    print(iter(c))

print("============================")
# 예제3
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) #strip는 양쪽 공백을 제거
print("============================")
# 예제4
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content) # 내용 없음

print("============================")
# 예제5
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line, end=' ')
        print("============================")
        line = f.readline()

print("========================================================")
print("========================================================")

# 예제7
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)

# 6.3 -> 여섯 자리이고, 소수는 셋째 자리까지 나올 수 있게
print('Average: {:6.3}'.format(sum(score)/len(score)))

# 파일 쓰기
# 예제1
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/text1.txt', 'w') as f:
    f.write('NiceMaaan!\n')

# 예제2
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/text1.txt', 'a') as f:
    f.write('GoodGoodMaaan!\n')

# 예제3
from random import randint

with open('/Users/apple/Desktop/FastCampus/python_basic/resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제4
# writelines: 리스트 -> 파일로 저장
with open('/Users/apple/Desktop/FastCampus/python_basic/resource/text3.txt', 'w') as f:
    list = ["Kim\n", "Park\n", "Cho\n"]
    f.writelines(list)
    

# class Median:
#     list_of_num = []

#     def __init__(self):
#         self.list_of_num = []
 
#     def get_item(self, item):
#         # Median.list_of_num.append(item)
#         self.list_of_num.append(item)
 
#     def clear(self):
#         # Median.list_of_num = []
#         self.list_of_num = []
 
#     def show_result(self):
#         # Median.list_of_num.sort()
#         self.list_of_num.sort()
#         # len_of_list = len(Median.list_of_num)
#         len_of_list = len(self.list_of_num)
#         center_of_list = int(len_of_list / 2)
#         if len_of_list % 2 == 1:
#             # print(Median.list_of_num[center_of_list])
#             print(self.list_of_num[center_of_list])
#         else:
#             # print((Median.list_of_num[center_of_list - 1] + Median.list_of_num[center_of_list]) / 2.0)
#             print((self.list_of_num[center_of_list - 1] + self.list_of_num[center_of_list]) / 2.0)
 
# median = Median()
# for x in range(10):
#     median.get_item(x)
# median.show_result()
 
# median.clear()
# for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
#     median.get_item(x)
# median.show_result()

# # 2020/03/29 changed
