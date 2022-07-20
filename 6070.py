'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall

예시
...
if n//3==1 :
print("spring")
...

참고
때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.

입력
월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

출력
계절 이름을 출력한다.
'''
month = int(input())
quo_month = month //3

if quo_month == 1:
    print('spring')
elif quo_month == 2:
    print('summer')
elif quo_month == 3:
    print('fall')
else:
    print('winter')