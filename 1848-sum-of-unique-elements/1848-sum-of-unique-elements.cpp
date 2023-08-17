class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        map<int,int> m;
        for(int i =0;i<nums.size();i++){
            m[nums[i]]++;

        }
        int res =0;
        for(auto x:m){
            if (x.second ==1) res+= x.first;
            cout<<x.second<<' ';
        }
        
       return res; 
    }
};