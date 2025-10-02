#Merge sort code written based on CLRS project
def merge(A, p, q, r):
    # Left half: A[p..q], Right half: A[q+1..r]
    L = A[p:q+1]
    R = A[q+1:r+1]

    # Add sentinel values
    L.append(float('inf'))
    R.append(float('inf'))

    i = j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
            if i == len(L): # this part added for implenting this algorithm without using the sentinel values
                A[k+1:r+1] = R[j:]
                break
        else:
            A[k] = R[j]
            j += 1
            if j == len(R):
                A[k+1:r+1] = L[i:]
                break

def mergeSort(arr):
    if len(arr) <= 1:   # base case
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

#using the T(n) = 2T(n_2) + O(n) so the Time complexisty is equal to nlogn