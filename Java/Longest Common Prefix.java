//https://leetcode.com/problems/longest-common-prefix/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null){
            return null;
        }
        else if (strs.length == 1){
            return strs[0];
        }
        String string1 = strs[0];
        String string2 = strs[1];
        String prefix = longestCommonPrefix(string1, string2);
        for(int i = 2; i < strs.length; i++){
            prefix = longestCommonPrefix(strs[i], prefix);
        }
        return prefix; 
    }


    public String  longestCommonPrefix(String string1, String string2){

        String prefix = "";
        if (string1.length() >= string2.length()) {
            prefix = string2;
            while(string1.indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() -1);
            }
        }
        else{
            prefix = string1;
            while(string2.indexOf(prefix) != 0){
                prefix = prefix.substring(0, prefix.length() -1);
            }
        }

        return prefix;

    }
}