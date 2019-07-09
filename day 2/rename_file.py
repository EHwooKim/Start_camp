import os
# 1. dummy 폴더로 들어간다.
os.chdir('./dummy')
print(os.getcwd())
# 2. 하나씩 파일명을 변경한다. => 반복문
files = os.listdir('.')
print(type(files))
#for file in files:
#    os.rename(file, f'SAMSUNG_{file}')
# 3. SAMSUNG이 아니라 SSAFY를 붙였어야지!
for file in files:
    os.rename(file, file.replace('SAMSUNG_SAMSUNG','SSAFY'))
