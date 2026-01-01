class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m-1, j = n-1, temp = m+n-1;
        if(m == 0)
            nums1 = nums2;
        while(i >= 0 && j >= 0){
            if(nums1[i] > nums2[j]){
                nums1[temp] = nums1[i];
                i--;
            }
            else{
                nums1[temp] = nums2[j];
                j--;
            }
            temp--;
        }
        while(j >= 0){
            nums1[temp] = nums2[j];
            j--;
            temp--;
        }
    }
};