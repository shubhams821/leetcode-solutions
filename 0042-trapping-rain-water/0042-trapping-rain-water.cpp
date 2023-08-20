class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int lmax[n];
        lmax[0] = height[0];
        for (int i =1; i<n; i++){
            lmax[i] = max( lmax[i-1],height[i]);
        }
        int rmax[n];
        rmax[n-1] = height[n-1];
        for(int j =n-2; j>=0;j--){
            rmax[j]=max(rmax[j+1],height[j]);
        }
        int res =0;
        for (int i=1;i<n-1;i++)
        res = res +(min(lmax[i],rmax[i])-height[i]);
        return res;
    }
    
};