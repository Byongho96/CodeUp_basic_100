'''
반복 횟수와 문장을 입력받아 여러 번 출력해보자.

예시
n = input()
s = input()
print(int(n)*s)

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

입력
반복 횟수와 문장이 줄을 바꿔 입력된다.

출력
입력된 횟수만큼 입력된 문장을 출력한다.
'''

num = int(input())
text = input()

print(text * num)