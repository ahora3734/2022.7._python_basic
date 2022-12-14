# ==== 숫자처리함수(random, randrange, randint) ====
from random import *

print(random()) # 0.49884507875627426 / 0.0 ~ 1.0 미만의 임의의 값 생성(소수점 17번째 자리까지 보여짐)
print(random() * 10)
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값(정수) 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값(정수) 생성

#로또 번호(1~45숫자를 임의로 출력)
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값(정수) 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값(정수) 생성, randrange(start, stop, step)
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값(정수) 생성


# 문제) 
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 한다.

# 조건1) 랜덤으로 날짜를 뽑아야 한다.

# 조건2) 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정한다.

# 조건3) 매월 1~3일은 스터디 준비해야 하므로 제외

# (결과 예) 오프라인 스터디 모임 날짜는 매월 X 일 입니다.

from random import *
day = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + "일 입니다.")