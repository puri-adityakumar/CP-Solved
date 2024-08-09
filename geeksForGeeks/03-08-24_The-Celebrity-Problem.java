// https://www.geeksforgeeks.org/problems/the-celebrity-problem/1

class Solution {
    public int celebrity(int mat[][]) {
       int arraySize = mat.length;
       
       int a = 0;
       int b = arraySize - 1;
       
       while (a < b) {
           if (mat[a][b] == 1) {
               a++;
           } else{
               b--;
           }
       }
       for( int i = 0; i < mat.length; i++){
            if((i!=a) && (mat[a][i] == 1 || mat[i][a] == 0)) {
                return -1;
            }
       }
       return a;
    }
}
