import os

# listdir == $ ls
# 현재 디렉토리에 있는 파일 및 폴더들
ls = os.listdir('.')
print(ls)
# getcwd(get current working directory) == $ pwd
# 현재 파일이 실행된 디렉토리(작업하고 있는 디렉토리)
pwd = os.getcwd()
print(pwd)
os.chdir(r'c:\Users\student\Desktop\Start_camp\day 2\dummy')
pwd = os.getcwd()
print(pwd)