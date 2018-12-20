import random

phonbook = {
    "치킨집" : "02-000-0000",
    "피자집" : "02-111-1111"
}
# print(phonbook["치킨집"])

# 가수 그룹의 딕셔너리를 만들어주세요
# 변수명 : 그룹이름
# key : 이름
# value : 나이(가상)

winner = {
    "강승윤" : 24,
    "김진우" : 27,
    "이승훈" : 26,
    "송민호" : 25,
}
block_B = {
    "지코" : 26,
    "태일" : 28,
    "비범" : 28,
    "재효" : 27,
    "유권" : 26,
    "박경" : 26,
    "피오" : 25
}

idol = { "위너" : winner, "블락비" : block_B }

# print(idol)
# print(idol["위너"])
# print(idol["위너"]["어중이"])

# score ={
#     "수학" : 50,
#     "국어" : 70,
#     "영어" : 100
# }
# for key, value in score.items():
#     print("{0}점수는 {1}".format(key,value))
    
    
# sum = 0
# for key, value in score.items():
#     sum = sum + value
# print(sum/3)

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

# 1. ssafy를 진행하는 지역은 몇개 인가요?
print("- 문제 1 -")
ssafy_local = len(ssafy["location"])
print(ssafy_local)

# 2. python standard library 'requests'가 있나요?
print("- 문제 2 -")
flag = False
for value in ssafy["language"]["python"]["python standard library"]:
    if value == "requests":
        flag = True
if flag:
    print("있다")
else:
    print("없다")
    
# 3. gj1반의 반장의 이름을 출력하세요
print("- 문제 3 -")
print(ssafy["classes"]["gj1"]["class president"])

# 4. ssafy에서 배우는 언어들을 출력하세요 : dictionary.keys활용
print("- 문제 4 -")
for k in ssafy["language"].keys():
    print(k)
    
# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요 : dictionary.values활용
    # 예시) teacher2
    #       pro2
print("- 문제 5 -")
temp_list = ["lecturer", "manager"]
for li in temp_list:
    print(ssafy["classes"]["gj1"][li])

# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시) flask는 micro이다.
    #       django는 full-functioning이다.
print("- 문제 6 -")
for key, value in ssafy["language"]["python"]["frameworks"].items():
    print("{0}는 {1}이다.".format(key,value))

# 7. 오늘 당번을 뽑기 위해
    # 예시) 오늘 당번은 문동식입니다.
print("- 문제 7 -")
# student_list = ssafy["classes"]["gj1"]["groups"]
# print(random.sample(student_list,1))