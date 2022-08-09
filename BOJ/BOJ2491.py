N = int(input()) #수열의 길이 9
num_list = input().split()  # 1, 2, 2, 4, 4, 5, 7, 7, 2 

# 뒤집은 숫자 배열
num_flipped_list = num_list[::-1]
# 최종 수열 중 가장 긴 길이
max_len = 0
max_len_list = []

for i in range(N): # 0 ~ 8
    length = 1
    for j in range(i, N-1):  # 0, 1, 2, 3, 4, 5, 6, 7
        if num_list[j] <= num_list[j+1]: # 다음 숫자가 지금 숫자보다 크거나 같으면 
            length += 1 # length 에 1 추가
        else : # 아니면 for문 끝내! 
            break
    max_len_list.append(length)
    # if length >= max_len:
    #     max_len = length   

# for i in range(N):
#     length = 1
#     for j in range(i, N-1):
#         if num_flipped_list[j] <= num_flipped_list[j+1]:
#             length += 1
#         else : # 아니면 for문 끝내! 
#             break
#     # if length >= max_len:
#     #     max_len = length   
#     max_len_list.append(length)

# print(max(max_len_list))