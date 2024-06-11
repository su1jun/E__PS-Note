import sys
input = sys.stdin.readline

N = int(input()) # 채널 번호
M = int(input()) # 고장난 버튼 갯수
if M:
    err = list(map(int, input().split())) # 고장난 버튼
else:
    err = []

m_cnt = abs(100 - N) # +, -만 사용

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in err: # 고장난 버튼 제외
            break

        elif j == len(nums) - 1: # 채널 입력이 가능하다면 +, -로 채널조정
            m_cnt = min(m_cnt, abs(int(nums) - N) + len(nums))

print(m_cnt)