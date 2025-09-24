import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        boolean state = false;
       HashSet<Integer> H = new HashSet<>();
       for (int i =0; i<nums.length; i++){
           if(!H.contains(nums[i])){
               H.add(nums[i]);
           }else{
               state = true ;
               break;
               
           }
       }
       return state;
    }
}