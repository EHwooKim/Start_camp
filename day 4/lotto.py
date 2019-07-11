# 요청보내는거 
# pprint : 이쁘게 보여주는거
import random
import pprint
import requests
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'
# 1.요청
# json -> 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# json을 쓰면 bs4로 했던거처럼 할 필요가 없다.!
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
# pprint.pprint(response)
# print(type(response))


# drwtNo_list = []
# drwtNo_list.append(response['drwtNo1'])
# drwtNo_list.append(response['drwtNo2'])
# drwtNo_list.append(response['drwtNo3'])
# drwtNo_list.append(response['drwtNo4'])
# drwtNo_list.append(response['drwtNo5'])
# drwtNo_list.append(response['drwtNo6'])
# bonus=response['bnusNo']

drwtNo_list = []
for i in range(1,7):
    drwtNo_list.append(response[f'drwtNo{i}'])
bonus=response['bnusNo']



count_jackpot = [0, 0, 0, 0, 0]
for i in range(10000000):
    my_lotto = random.sample(range(1,46),6)

    # count = 0
    # for i in my_lotto:
    #     if i in drwtNo_list:
    #         count += 1

    count = len(set(drwtNo_list) & set(my_lotto))


    if count == 3:
        # print('5등!')
        count_jackpot[4] += 1    
    elif count == 4:
        # print('4등!')   
        count_jackpot[3] += 1     
    elif count == 5 and bonus not in my_lotto:
        # print('3등!')
        count_jackpot[2] += 1    
    elif count == 5 :
        # print('2등!')
        count_jackpot[1] += 1    
    elif count == 6:
        # print('1등!')
        count_jackpot[0] += 1    
    else:
        pass
        # print('당연히 꽝입니다.')
        # count_jackpot[0] += 1    

    print(count_jackpot, end='\r')

# print('끝')

# for i in range(6):
#     print('{0}등을 총 {1}번 했습니다'.format(i, count_jackpot[i]))
# print('당신은 {0}원을 썼습니다.'.format(sum(count_jackpot)*1000))

