# with open('number.txt','r') as f:
#     # readlines : 라인을 각각 리스트의 원소로 하여 반환한다. 그렇기 때문에 반복문으로 출력
#     lines = f.readlines()
#     lines.reverse()

# for line in lines:
#     print(line.strip())

# with open('reverse_number.txt','w') as f:
#     for line in lines:
#         f.write(line)

# #-------

# with open('number.txt','r') as file:
#     numbers = file.readlines()
# print(numbers)

# numbers.reverse()

# with open('number_revers.txt','w') as file:
#     for number in numbers:
#         file.write(number)
#????????????????????????????????????????????????????????

# number.txt를 읽어서
# 리스트 (readlines)
with open('number.txt', 'r') as file:
    numbers = file.readlines()
print(numbers)

# 리스트를 뒤집는다.
numbers.reverse()
print(numbers)
# number_reverse.txt로 저장!
# 4
# 3
# 2
# 1
# 0
with open('number_reverse.txt', 'w') as file:
    for number in numbers:
        file.write(number)