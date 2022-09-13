print(1, 2, 3) # 1 2 3

print('안녕', 'python') # 안녕 python

print(1, 2, 3, sep=', ') # 1, 2, 3

print('안녕', 'python', sep='') #안녕python

print(1, 2, 3, sep='\n') # 1\n 2\n 3\n

print('1\n2\n3') # 1\n 2\n 3\n #'\'을 문자로 출력하고 싶을 때는 \\
    
print(1, end='')
print(2, end='')
print(3) # 123

print(1, end=' ')
print(2, end=' ')
print(3) # 1 2 3


company = '네이버'
print(company)

ip = '223.130.200.107' #도메인으로 ip 확인(https://thisthatbase.com/domain-ip-check-online-command/)
url = 'naver.com'
print("네이버 url(IP): ", url + "(" + ip + ")") # 문자열을 합칠 때는 + / 네이버 url(IP):  naver.com(223.130.200.107)
print("네이버 url(IP):", url + "(" + ip + ")")  #                     / 네이버 url(IP): naver.com(223.130.200.107)
print("네이버 url(IP): " + url + "(" + ip + ")") # 위와 같은 결과 출력 / 네이버 url(IP): naver.com(223.130.200.107)


print('너 몇살이니?')
old = int(input()) # input으로 받은 값은 모두 문자열로 저장됨. 계산에 사용될 숫자를 입력하고 싶다면 int(input())
print('10년 뒤 너는', end=' ')
print(old + 10, end=' ')
print('살 입니다')