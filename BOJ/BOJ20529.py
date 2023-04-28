# BOJ 20529 가장 가까운 세 사람의 심리적 거리
# (BOJ 20529 가장 가까운 세 사람의 심리적 거리)[https://www.acmicpc.net/problem/20529]

# 문제
# 여러분은 요즘 유행하는 심리검사인 MBTI에 대해 들어보았는가?

# MBTI(Myers-Briggs Type Indicator)는 C.G.Jung의 심리유형론을 근거로 하여 Katharine Cook Briggs와 Isabel Briggs Myers가 보다 쉽고 일상생활에 유용하게 활용할 수 있도록 고안한 자기보고식 성격유형지표이다. (출처: 위키백과)

# MBTI는 아래와 같이 네 가지 척도로 사람들의 성격을 구분한다.

# 외향(E) / 내향(I)  
# 감각(S) / 직관(N)  
# 사고(T) / 감정(F)  
# 판단(J) / 인식(P)  
# 각 척도마다 두 가지 분류가 존재하므로, MBTI는 총 2^4 = 16가지 유형이 있음을 알 수 있다. 일반적으로 MBTI의 유형들은 각 분류를 나타내는 알파벳 한 글자씩을 따 네 글자로 표시하게 된다. 모든 유형의 목록은 다음과 같다.

# ISTJ, ISFJ, INFJ, INTJ, ISTP, ISFP, INFP, INTP, ESTP, ESFP, ENFP, ENTP, ESTJ, ESFJ, ENFJ, ENTJ
# MBTI 성격 유형을 이용하면 두 사람 사이의 심리적인 거리를 정의할 수 있다. 이는 두 사람의 MBTI 유형에서 서로 다른 분류에 속하는 척도의 수로 정의된다. 예를 들어, MBTI 유형이 ISTJ인 사람과 ISFJ인 사람 사이의 거리는 1이며, INTP인 사람과 ENTJ인 사람 사이의 거리는 2이다.  
# 이 정의를 확장해서 세 사람 사이의 심리적인 거리도 정의할 수 있다. 세 사람 A, B, C가 있을 때 이들의 심리적인 거리는

# (A와 B사이의 심리적인 거리) + (B와 C 사이의 심리적인 거리) + (A와 C사이의 심리적인 거리)
# 로 정의한다.

# 대학교에서 심리학 교수로 일하는 종서는 자신이 가르치는 학생들의 심리적인 특성을 분석하고 싶어한다.

# 오늘이 생일인 종서를 위해 N명의 학생들의 MBTI 유형이 주어질 때, 가장 가까운 세 학생 사이의 심리적인 거리를 구해보자.

# 입력
# 첫 줄에는 테스트 케이스의 수를 나타내는 정수 T가 주어진다.

# 각 테스트 케이스의 첫 줄에는 학생의 수를 나타내는 하나의 정수 N이 주어지며, 두 번째 줄에는 각 학생의 MBTI 성격 유형을 나타내는 문자열들이 사이에 공백을 두고 주어진다.

# 출력
# 각 테스트 케이스에 대한 답을 정수 형태로 한 줄에 하나씩 출력한다.

# 제한
# - 1 <= T <= 50
# - 3 <= N <= 100,000
# - 각 테스트 케이스의 N의 합은 100,000을 넘지 않는다. 
from itertools import combinations
import sys

sys.stdin = open('sample.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    arr = input().split()
    nums = [i for i in range(N)]
    combi = list(combinations(nums, 3))
    result = 16 * 3
    for a, b, c in combi:
        temp = 0
        for i in range(4):
            if temp > result:
                break
            if arr[a][i] != arr[b][i]:
                temp += 1
            if arr[b][i] != arr[c][i]:
                temp += 1
            if arr[c][i] != arr[a][i]:
                temp += 1
        if temp < result:
            result = temp
    print(result)