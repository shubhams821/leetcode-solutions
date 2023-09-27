class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long res = INT_MIN;
        long long count =0;
        for(int i =0;i<nums.size();i++){
            if (count<0) {count =0;}
            count +=nums[i];
            cout<<count<<' ';
            res = max(res,count);
            
        }
        return res;
    }
};