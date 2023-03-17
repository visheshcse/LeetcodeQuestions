class Solution {
public:
    string longestcp(string a, string b){
        string s = "";
        for(int i = 0; i < min(a.size(), b.size()); i++){
            if(a[i] == b[i]){
                s+= a[i];
            }
            else{
                break;
            }
        }
        return s;
    }
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0){
            return "";
        }
        if(strs.size() == 1){
            return strs[0];
        }
        string comp = strs[0];
        for(int i = 1; i < strs.size(); i++){
            comp = longestcp(comp, strs[i]);
        }
        return comp;
    }
};