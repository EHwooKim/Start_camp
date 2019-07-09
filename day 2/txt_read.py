# window - cp949 (encoding)
# mac/web - utf-8 으로 작성(?)인식(?)되다보니 bash에서는 깨져보이긴하는데 제대로 된거야

with open('ssafy_with.txt','r') as f:
    # readlines : 라인을 각각 리스트의 원소로 하여 반환한다. 그렇기 때문에 반복문으로 출력
    lines = f.readlines()    

for line in lines:
    print(line.strip())

with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다. 그렇기 때문에 그냥 출력해도 모든 문장이 나온다.
    txt = f.read()

print(txt)
print(type(txt))