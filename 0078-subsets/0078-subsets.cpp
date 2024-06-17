class Solution {
public:
    vector<vector<int>> ans;
    void recur(vector<int> nums, vector<int> temp, int idx){
        if (idx== nums.size()){
            ans.push_back(temp);
            return;
        }
        recur(nums,temp,idx+1);
        temp.push_back(nums[idx]);
        recur(nums,temp,idx+1);
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<int> temp;
        ans.clear();
        recur(nums,temp,0);
        return ans;
    }
};