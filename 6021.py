'''
알파벳과 숫자로 이루어진 단어 1개가 입력된다.
입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

예시
s = input()
print(s[0])
print(s[1])
...

참고
s[0] 은 첫 번째 문자를 의미한다.

입력
5개의 문자로 이루어진 단어 1개가 입력된다.

출력
각 문자를 한 줄에 한 문자씩 줄을 바꿔 출력한다.
'''
## 이 아래부터 코드 시작
text = input()
text_len = len(text)

for i in range(text_len):
    print(text[i])