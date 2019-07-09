# option 1.
# 파일을 연다.
# open(파일명, 옵션)
# w : write (덮어쓰기)
# a : append (이어쓰기)

f = open('ssafy.txt','a')
# 글을 작성한다.
for i in range(10):
    # \n : 개행문자 (엔터 : newline)
    f.write(f'안녕하세요. {i}\n')
# 파일을 닫는다.
f.close()
#그런데 이 option 1. 은 close를 해줘야해서 불편해. 그래서 나온게! option 2.


#option 2. 컨택스트 매니저(context manager) with 구문
with open('ssafy_with.txt','w') as f:
    for i in range(5):
        f.writelines('안녕?\n써지나?\n써지네\n')
        f.writelines(['은정\n','인성\n'])
# close()가 필요없다!

