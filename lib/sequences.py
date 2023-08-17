#!/usr/bin/env python3

def print_fibonacci(length):
    arr = [0,1]
    if length==0:
        print('[]')

    elif length==1:
        print('[0]')

    elif length==2:
        print('[0,','1]')
    else:
        while(len(arr)<length):
            arr.append(0)
        if(length==0 or length==1):
            return 1
        else:
            arr[0]=0
            arr[1]=1
            for i in range(2,length):
                arr[i]=arr[i-1]+arr[i-2]
            print(arr)    
            return arr[length-2]
print_fibonacci(9)    