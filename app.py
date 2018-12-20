from flask import Flask, render_template, request
import random
import requests
import json
from faker import Faker

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")
    
@app.route('/lottery')
def lottery():
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'
    res = requests.get(url).text # 여기에서 json형식으로 받는다. type(res) = str
    # print(type(res))
    lotto_dict = json.loads(res) #json 내부 함수 활용 json->dict 변환
    date = lotto_dict["drwNoDate"] # 추첨일
    turn = lotto_dict["drwNo"] # 추첨회차
    week = [] # 추첨번호
    for i in range(1,7):
        temp_str = "drwtNo{0}".format(i)
        week.append(lotto_dict[temp_str])
    lotto_bonus = lotto_dict["bnusNo"] # 보너스번호
    
    pick = random.sample(list(range(1,46)), 6) # 번호 자동 추출
    pick.sort()
    
    match = len(set(week) & set(pick)) # 공통 번호 개수
    
    # 등수 찾기
    rank = -1
    if match == 6:
        rank = 1
    elif match == 5:
        if lotto_bonus in pick:
            rank = 2
        else:
            rank = 3
    elif match == 4:
        rank = 4
    elif match == 3:
        rank = 5
    
    # 멘트 출력
    if 1 <= rank <= 5:
        ment = "축하합니다. {0}등 입니다!!".format(rank)
    else:
        ment = "꽝입니다. 아쉽네요."
        
    return render_template('lotto.html', lotto=pick, lotto_date=date, lotto_turn=turn, lotto_week=week, lotto_bonus=lotto_bonus, lotto_rank=rank, lotto_ment=ment)
    

@app.route('/ping')
def ping():
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_job = fake.job()
    return render_template("pong.html", html_name=input_name, fake_job=fake_job)
    
@app.route('/soulmate_in')
def soulmate_in():
    return render_template("soulmate_in.html")
    
@app.route('/soulmate_out')
def soulmate_out():
    input_name = request.args.get('name')
    fake = Faker('ko_KR')
    fake_soul = fake.name()
    return render_template("soulmate_out.html", html_name=input_name, soulmate=fake_soul)