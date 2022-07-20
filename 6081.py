'''
16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

예시
...
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
...

참고
print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
작은 따옴표 2개 '' 또는 큰 따옴표 2개 "" 는 아무 문자도 없는 빈문자열(empty string)을 의미한다.


입력
16진수로 한 자리 수가 입력된다.
단, A ~ F 까지만 입력된다.

출력
입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
계산 결과도 16진수로 출력해야 한다.
'''

num = int(input(), 16)

for i in range(1, 16):
    mul = num * i
    print(f'{num:X}*{i:X}={mul:X}')