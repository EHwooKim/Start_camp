# dictionary
# key - value
# key : string, integer, float, boolean 
# list, dictionary는 key가 될 수 없다.
# value : 모든 값을 가질 수 있다.
lunch = {'중국집' : '02-220-4123'}
print(lunch)
dinner = dict(한식='02-123-412')
print(dinner)
bf = {}
bf['분식'] = '123-412-5512'
print(bf)

menu = {'bf' : bf, 'lunch' : lunch, 'dinner': dinner}
print(menu)
print(menu['bf']['분식'])

ssafy = {'김은정': '학생', '김인성': '학생', '연용흠': '반장'}
for key in ssafy:
    print(key)
    print(ssafy[key])

for key, value in ssafy.items():
    print(key, value)

# print(ssafy.items()) # key와 value를 가지는 tuple들.

for value in ssafy.values():
    print(value)

for key in ssafy.keys():    # for key in ssafy: 랑 같은 결과
    print(key)