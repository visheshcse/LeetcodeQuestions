class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman;
        roman['I'] = 1;
        roman['V'] = 5;
        roman['X'] = 10;
        roman['L'] = 50;
        roman['C'] = 100;
        roman['D'] = 500;
        roman['M'] = 1000;
        int i = 0, sum = 0;
        while(i < s.length()){
            if(i+1 < s.length() && roman[s[i]] < roman[s[i+1]])
                sum-= roman[s[i]];
            else
                sum+= roman[s[i]];
            i++;
        }
        return sum;
    }
};