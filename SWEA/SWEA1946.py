#testcase
T = int(input())

for i in range (0, T) :
    arr = []
    #number of alphabet 
    num = int(input())

    for j in range (0, num) : 
        temp = input().split()
        arr.append(temp[0])
        arr.append(temp[1])
    temp = ""
    for j in range(len(arr)) : # 0, 1, 2, 3, 4, 5
        if j % 2 == 0 : 
            print(arr[j])
            print(int(arr[j+1]))
            temp = temp + arr[j]*int(arr[j+1])
        
    
    print(f'#{i+1}')
    for j in range(0, len(temp)//10+1) : 
        print(temp[j*10 : (j*10)+10])
