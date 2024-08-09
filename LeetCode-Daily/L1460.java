// LeetCode problem : 1460. Make Two Arrays Equal by Reversing Subarrays

class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        Arrays.sort(target);
        Arrays.sort(arr);
        return Arrays.equals(target, arr);
    }
}