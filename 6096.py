'''
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...
"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

입력
바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.십자 뒤집기 좌표가 횟수(n) 만큼 입력된다.
단, n은 10이하의 자연수이다.

출력

'''
import sys

board = []
for _ in range(19): # 19*19의 바둑판 배열을 받아들임
    board.append(list(map(int, sys.stdin.readline().split())))

T = map(int, sys.stdin.readline().split())

# 십자 뒤집기
for _ in range(T):
    for i in range(19):
        if board[i][y-1]:
            board[i][y-1] = 1
        else:
            board[i][y-1] = 0
    for j in range(19):
        if board[x-1][j]:
            board[x-1][j] = 1
        else:
            board[x-1][j] = 0

# 프린트
for i in board:
    for j in i:
        print(j, end=' ')
    print()

    