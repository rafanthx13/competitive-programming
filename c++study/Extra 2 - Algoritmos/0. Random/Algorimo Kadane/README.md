# Algotimo de Kadadane

Tambem conhecido como maxSubArray Problem

## Links

+ https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
+ https://pt.wikipedia.org/wiki/Sublista_cont%C3%ADgua_de_soma_m%C3%A1xima

Problema: sublista contígua de maior soma a partir de uma lista de números é um problema bastante conhecido.

Time Complexity: O(n)
Algorithmic Paradigm: Dynamic Programming

```
Initialize:
    max_so_far = 0
    max_ending_here = 0

Loop for each element of the array
  (a) max_ending_here = max_ending_here + a[i]
  (b) if(max_ending_here < 0)
            max_ending_here = 0
  (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
return max_so_far
```

Exemplo Geek

```
int maxSubArraySum(int a[], int size) 
{ 
   int max_so_far = 0, max_ending_here = 0; 
   for (int i = 0; i < size; i++) 
   { 
       max_ending_here = max_ending_here + a[i]; 
       if (max_ending_here < 0) 
           max_ending_here = 0; 
  
       /* Do not compare for all elements. Compare only    
          when  max_ending_here > 0 */
       else if (max_so_far < max_ending_here) 
           max_so_far = max_ending_here; 
   } 
   return max_so_far; 
} 
```