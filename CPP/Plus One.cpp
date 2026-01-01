class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        int i = 1;
        int carry = (digits[0]+1)/10;
        digits[0] = (digits[0]+1)%10;
        while(i < digits.size()){
            if(carry == 0)
                break;
            int c = (digits[i]+carry)/10;
            digits[i] = (digits[i]+carry)%10;
            carry = c;
            i++;
        }
        if(carry!= 0)
            digits.push_back(carry);
        reverse(digits.begin(), digits.end());
        return digits;
    }
};