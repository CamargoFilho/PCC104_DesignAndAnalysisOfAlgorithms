ALGORITHM SequentialSearch2(A[0..n], K)
//Implements sequential search with a search key as a sentinel
//Input: An array A of n elements and a search key K
//Output: The index of the first element in A[0..n − 1] whose value is
// equal to K or −1 if no such element is found
A[n]← K
i ← 0
while A[i] = K do
i ← i + 1
if i<n return i
else return −1