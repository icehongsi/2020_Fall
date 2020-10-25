'''
[DP] 왼쪽 맞춤제출완료
70점
아래한글이나 MS 워드에서는 문단을 왼쪽맞춤, 오른쪽맞춤, 양쪽맞춤 중 하나로 편집가능하다. 그 중에서 왼쪽맞춤을 생각해보자
각 줄의 처음은 단어로 시작하고, 두 단어 사이에는 정확히 하나의 공백(space)을 넣는다고 가정한다
단어 하나는 반드시 한 줄에 포함되어야 한다. 즉, 두 줄에 걸쳐 나뉘어 나타나지 않아야 한다
문장을 페이지 폭이 W인 쪽(page)에서 왼쪽 맞춤을 예쁘게 하기 위해, 각 줄마다 penalty 점수를 (W - 해당 줄의 글자 수 - 단어 사이의 공백 수)**3 으로 정의한다
예: Ape ate apple.   에서 W = 16이고, 글자수 = 12 (마침표 포함), 세 단어 사이의 공백 수 = 2이므로 (16 - 14)**3 = 2**3 = 8 점이 penalty 값이다 (여기서 가장 뒤 초록색과 보라색은 오른쪽 끝에 남은 공백이다!)
최종 왼쪽 맞춤의 penalty 값은 각 줄의 penalty 값의 합으로 정의된다
입력:  W값을 첫 번째 줄에서 먼저 입력받고 두 번째 줄에서 여러 문장을 한 줄로 입력받는다.
입력 받은 문장을 공백을 기준으로 split으로 분할하여, 폭이 W인 페이지에 왼쪽맞춤을 하는데, penalty 값이 최소가 되도록 한다. (DP로 해결 가능)
단, W 값은 가장 긴 단어(구둣점 포함)의 길이보다 같거나 크다고 가정해도 된다
출력: 최소 penalty 값이다
분석: 코드 마지막에 주석으로 DP 점화식을 쓰고 알고리즘의 수행시간을 간단하게 분석한 후 Big-O 기호로 표기할 것
[주의] 유사도 검사를 실시할 예정이니 꼭 혼자 힘으로 짜보길 바랍니다!
입력 예: W = 8인 경우
8
ape eats apple cider a lot.
최소 penalty는 62가 되고 그 때의 왼쪽 맞춤한 결과는 아래와 같다
마지막 문자 |은 줄의 마지막임을 나타내기 위해 일부러 삽입한 것임
ape eats|
apple   |
cider   |
a lot.  |
첫 줄의 penalty = 0, 둘째 줄의 penalty = 3^3 = 27, 세째 줄의 penalty = 3^3 = 27, 네째 줄의 penalty = 2^3 = 8 이 되어 62가 되고, 이 값이 입력에 대한  최소 penalty의 왼쪽 맞춤이 된다
만약 아래처럼 왼쪽 맞춤을 하면, 총 penalty = 0 + 3^3 + 1^3 + 4^3 = 27 + 1 + 64 = 92가 되어 최소 penalty를 갖는 왼쪽 맞춤이 아니다
ape eats|
apple   |
cider a |
lot.    |

최소 penalty가 되는 왼쪽 맞춤은 여러 개가 존재할 수도 있다. (즉, 최소 penalty 값은 유일하지만, 그 penalty 값을 주는 왼쪽 맞춤은 여러 개일 수 있다)

입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
12
ape eats apple cider alot.
출력
281
예시 2
입력
8
ape eats apple cider alot.
출력
62
예시 3
입력
5
abcde
출력
28
예시 4
입력
30
입/출력 예시
:
공백
:
줄바꿈
:
탭
예시 1
입력
12
apeeatsapplecideralot.
출력
281
예시 2
입력
8
apeeatsapplecideralot.
출력
62
예시 3
입력
5
abcde
출력
28
예시 4
입력
30
The word 'algorithm' has its roots in Latinizing the name of Persian mathematician Muhammad ibnMusaal-Khwarizmi in the first steps to algorismus.
출력
2234

출력
2234
'''


import sys


def solution(chars, n):
    dp = [[sys.maxsize for char in chars] for char in chars] #make a dp matrix that is filled with zero
    for char in range(len(chars)):
        dp[char][char] = (n - len(chars[char]))**3
    for i in range(1, len(chars)): # n of iteration
        row = 0
        for col in range(i, len(chars)): #column
            if len("".join(chars[row:col+1])) + (col - row) <= n: # 단어의 합이 n보다 작을 경
                 min_val = (n - (len("".join(chars[row:col+1])) + (col - row))) ** 3
            else:
                min_val = sys.maxsize
            for l in range(col):
                if min_val > dp[0][col-l-1] + dp[col-l][col]:
                    min_val = dp[0][col-l-1] + dp[col-l][col]
            dp[row][col] = min_val
            row += 1

    return dp[0][len(chars)-1]


#print(solution("ab c de".split(), 5))
#30


result =solution("The word 'algorithm' has its roots in Latinizing the name of Persian mathematician Muhammad ibn Musa al-Khwarizmi in the first steps to algorismus.".split(), 30)
print(result)