with open("file1.txt", "r") as file1:
    list1 = file1.readlines()

list1_num = [int(num.strip()) for num in list1]
# print(list1_num)

with open("file2.txt", "r") as file2:
    list2 = file2.readlines()

list2_num = [int(num.strip()) for num in list2]
# print(list2_num)

