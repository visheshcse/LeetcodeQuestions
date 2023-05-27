//https://leetcode.com/problems/pascals-triangle/

class Solution {
    public void ps(List<List<Integer>> list, List<Integer>rowList, int numRows, int start){
        if(numRows == 1){
            return;
        }
        List<Integer> newList = new ArrayList<>(start);
        newList.add(0, 1);
        newList.add(newList.size() - 1, 1);
        for(int i = 0; i < rowList.size() - 1; i++){
            newList.add(i+1, rowList.get(i) + rowList.get(i+1));
        }
        list.add(newList);
        ps(list, newList, numRows - 1, start++);
    }
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>(numRows);
        List<Integer> rowList = new ArrayList<>(1);
        rowList.add(0, 1);
        list.add(rowList);
        ps(list, rowList, numRows, 1);
        return list;

    }
}