//https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution {
    public int removeDuplicates(int[] nums) {
        int insertionIndex = 1;
        int iterationIndex = 0;
        while(iterationIndex != nums.length -1){
            if(nums[iterationIndex] == nums[iterationIndex+1]){
                iterationIndex = iterationIndex + 1;
            }
            else{
                iterationIndex = iterationIndex + 1;
                nums[insertionIndex] = nums[iterationIndex];
                insertionIndex = insertionIndex +1;
            }
        }
        return insertionIndex;
        
    }
}