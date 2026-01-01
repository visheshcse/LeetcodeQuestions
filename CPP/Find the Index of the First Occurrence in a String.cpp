class Solution {
public:
    int strStr(string haystack, string needle) {
        int i = 0, j = 0, n;
        n = needle.length();
        while(i < haystack.length()){
            if((i + n) <= haystack.length() && haystack.substr(i, n) == needle)
                return i;
            else if((i+n) > haystack.length())
                return -1;
            else
                i++;
        }
        return -1;
    }
};