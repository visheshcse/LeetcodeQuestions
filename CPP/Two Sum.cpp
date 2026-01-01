class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        for(int i = 0; i < nums.size(); i++)
            m[nums[i]] = i;
        int i = 0, j  = nums.size()-1;
        sort(nums.begin(), nums.end());
        vector<int> res;
        while(i < j){
            if(nums[i]+nums[j] == target){
                res.push_back(m[nums[i]]);
                res.push_back(m[nums[j]]);
                break;
            }
            else if(nums[i]+nums[j] > target)
                j--;
            else
                i++;
        }
        return res;
    }
};