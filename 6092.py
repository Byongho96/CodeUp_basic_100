'''
정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.

선생님은 출석부를 보고 번호를 부르는데,
학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부른다.

그리고 얼굴과 이름이 잘 기억되지 않는 학생들은 번호를 여러 번 불러
이름과 얼굴을 빨리 익히려고 하는 것이다.

출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

예시
n = int(input())      #개수를 입력받아 n에 정수로 저장
a = input().split()  #공백을 기준으로 잘라 a에 순서대로 저장

for i in range(n) :  #0부터 n-1까지...
  a[i] = int(a[i])       #a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장

d = []                     #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
for i in range(24) :  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
  d.append(0)        #각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.

for i in range(n) :    #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
  d[a[i]] += 1

for i in range(1, 24) :  #카운트한 값을 공백을 두고 출력
  print(d[i], end=' ')

참고
- d = []              #어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
- d.append(값)  #d 리스트의 마지막에 원하는 값을 추가(append)해 넣음 
- d[a[i]] += 1     #2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..

어떤 값을 기록했다가 다시 사용할 필요가 있을 때, 필요한 변수(variable)를 만들어 사용하는 것처럼,
여러 개의 값을 하나로 묶어 목록으로 기록했다가 다시 사용할 필요가 있을 때, 리스트(list)를 만들어 사용할 수 있다.
리스트는 변수들을 모아 놓은 변수라고 생각할 수도 있고, 참조번호를 이용해 간단하고 편리하게 사용할 수 있다.

입력
첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.

출력
1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력한다.

'''

n = int(input())
call = list(map(int, input().split()))

stu_list = []
for _ in range(24):
    stu_list.append(0)

for num in call:
    stu_list[num] += 1

for i in range(1, 24):
    print(stu_list[i], end = ' ')
