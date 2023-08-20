class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxsum = nums[0],cur =0;

        for (int x:nums){
            if (cur<0) cur =0;
            cur += x;
            maxsum =  max(cur,maxsum);
            
        }
        cout<<maxsum;
        return maxsum;
        
    }
};