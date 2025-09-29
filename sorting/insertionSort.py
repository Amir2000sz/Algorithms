#input array = arr = [a1 , a2 ,...]
#output array = result (the increasing sorted version of arr)
#inplace
def sort(arr:list[int]):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
                print(arr)
    return arr
print("-----------------------------------------------")
print(sort([5,2,4,6,1,3]))

#Time complexity = the first loop execute n times and the insdie loop will be executed i times so we will have T = sigma_k=0 ^n (sigma_z=0 ^k 1) 
# = O(n^2) 

#so this the method i used CLRS and github repo are using a different method as i try to start from the 0 index and CLRS uses the index before the one we want to find its correct index it work like this that it compare the index that we want to find its correct spot with index - 1 if its smaller the element in index - 1 will be put in the index spot and then index-- 
