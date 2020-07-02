# Ordenação

### Buscar Binariia a primeira ocorrencia numa lista de interios

```
from bisect import bisect_left 
  
def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i != len(a) and a[i] == x: 
        return i 
    else: 
        return -1

# calling:
BinarySearch(aList, query) # return the index of list with elemento
```

### Quick Sort

```
def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


# calling:
quickSort(aList,0, qtd - 1) # inplace, reordena a lista

```

### Inverter uma String/lista ( Mais eficiente)
link: https://www.journaldev.com/23647/python-reverse-string

````
s = "abc"
s_invertido = s[::-1]

````