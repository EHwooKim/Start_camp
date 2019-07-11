"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
# 1. 기본 풀이
print('==== Q1 ====')
sum = 0
for value in score.values():
    sum += value
print(f'평균: {sum/len(score)}')

# 2. 함수 활용하기
print('평균: {0}'.format(sum(score.values())/len(score)))



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
# 방법 1.
for key in scores:
    sum = 0
    for value in scores[key].values():
        sum += value
    print('{0}반 평균 : {1}'.format(key, sum/len(scores[key])))
# 방법 2.
for key in scores:
    average = sum(scores[key].values())/len(scores[key])
    print('{0}반 평균 : {1}'.format(key, average))

# 전체 평균
total = 0
count = 0
for person_scores in scores.values():
    for score in person_scores.values():
        total += score
        count +=1
print(total/count)
    
    



# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 내가한거..
print('==== Q3-1 ====')
for key in city:
    sum = 0
    for value in city[key]:
        sum += value
    print('{0} : {1:.2f}'.format(key,sum/len(city[key])))

# 선생님 풀이
for name, temp in city.items():
    avg = sum(temp)/len(temp)
    print(f'{name}: {avg:.2f}')   # f-string : 3.6+


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
# 선생님 풀이
min_temp = 0
max_temp = 0
min_city = ''
max_city = ''
count = 0
# 지역별로 온도를 모두 확인하면서,
for name, temp in city.items():
    # 첫번째 반복때는 모두 다 저장해! 처음에 어떤 값을 최대, 최소로 할지 모르거든, 그래서 처음 값을 저장하는거야
    if count == 0:
        min_city = name
        max_city = name
        min_temp = min(temp)
        max_temp = max(temp)
        count += 1  # 이제 초기화 끝.
# 가장 추우면, 해당 도시와 기온을 기록
    if min(temp) < min_temp:
        min_city = name
        min_temp = temp
# 더울 때도, 해당 도시와 기온을 기록
    if max(temp) > max_temp:
        max_city = name
        max_temp = temp
print(f'추운 곳은 {min_city}, 더운 곳은{max_city}')

#--------------------------
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

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
# 선생님 풀이
if 2 in city['서울'] :
    print('네')
else:
    print('아니요')
