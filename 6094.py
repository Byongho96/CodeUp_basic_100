'''
정보 선생님은 오늘도 이상한 출석을 부른다.

영일이는 오늘도 다른 생각을 해보았다.
출석 번호를 다 부르지는 않은 것 같은데... 가장 빠른 번호가 뭐였지?

출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

단, 
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.

참고
리스트에 출석 번호를 기록해 두었다가, 그 중에서 가장 작은 값을 찾아내면 된다.
그런데, 가장 작은 값은 어떻게 어떤 것과 비교하고, 어떻게 찾아야 할까?

입력
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출력
출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

'''

n = int(input())

call_list = list(map(int, input().split()))

print(min(call_list))