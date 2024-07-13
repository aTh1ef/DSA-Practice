def linearSearch(arr,n,num):
    for i in range(0,n):
        if arr[i] == num:
          return i
    else:
          return -1

if __name__=="__main__":
    arr = [1,80,90,200,75]
    n = len(arr)
    num = 90
    result = linearSearch(arr,n,num)
    print("after serach we got the index as", result)
