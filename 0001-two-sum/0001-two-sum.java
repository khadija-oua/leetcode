class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] L = new int[2];
        int t = target;
        for(int i=0; i<nums.length ;i++ ){
             for(int j = i+1; j<nums.length ;j++ ){
                if ( nums[i]+nums[j] == t ){
                    L[0]=i;
                    L[1]=j;
                }

             }
        }
        return L;
    }
}