city = {
    '서울': [-6, -10, 10],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 1],
    '부산': [2, -2, 9],
}

total_temp=[]
for value in city.values():
    total_temp.extend(value)

min_temp = min(total_temp)
max_temp = max(total_temp)

for key in city:
    if min_temp in city[key]:
        print('최근 3일간 가장 추웠던 곳은 {0}입니다.'.format(key))
    elif max_temp in city[key]:
        print('최근 3일간 가장 더웠던 곳은 {0}입니다.'.format(key))
