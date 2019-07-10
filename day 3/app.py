from flask import Flask, render_template
import random

#flask run으로 서버 켜고 Ctrl+c로 서버 끄기
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route('/hi')
def hi():
    return render_template('hi.html')

# variable routing : 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higye(name):
    return render_template('hi2.html',namee=name)

# /cube/<숫자>
# 세제곱한 결과를 반환
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}'

# /lunch/사람이름
@app.route('/lunch/<string:name>')
def lunch(name):
    lunch_box = ['한식', '중식', '일식']
    return render_template('lunch.html', name=name, menu=random.choice(lunch_box))
    


# 로또!
# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route('/lotto')
def lotto():
    jackpot = random.sample(range(1,46),6)
    # jackpot.sort()
    # jackpot = ','.join(list(map(str,jackpot)))
    return f'이번주 당첨번호는{jackpot}!!!! 1등기원'

if __name__ == "__main__":
    #python app.py 를 하면 아래의 코드 블록을 실행시킨다. 
    #지금부터는 python app.py로 서버 켜고 서버 껐다 켜지 않아도 수정내용 반영 가능.
    app.run(debug=True)






