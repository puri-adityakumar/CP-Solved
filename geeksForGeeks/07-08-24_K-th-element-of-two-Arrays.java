// https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1

class Solution {
    public long kthElement(int k, int arr1[], int arr2[]) {
        int n = 0;
        int length = arr1.length + arr2.length;
        
        int[] arr3 = new int[length];
        int pos = 0;
        for (int i = 0; i < arr1.length; i++) {
            arr3[pos] = arr1[i];
            pos++;
        }
        for (int i = 0; i < arr2.length; i++){
            arr3[pos] = arr2[i];
            pos++;
        }
        
        Arrays.sort(arr3);
        
        for (int i = 0; i < arr3.length; i++){
            n = arr3[ k - 1];
        }
        return n;
    }
}