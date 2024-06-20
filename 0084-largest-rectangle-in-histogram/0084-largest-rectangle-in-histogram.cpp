class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
     stack<int> s;
     int res =0;
     int n = heights.size();
     for(int i=0; i<n;i++){
        while(!s.empty() and heights[s.top()]>= heights[i]){
            int tp = s.top();
            s.pop();
            int curr = heights[tp]*(s.empty()?i:(i-s.top()-1));
            res = max(res,curr);
        }
        s.push(i);
     }   
     while(!s.empty()){
        int tp = s.top();
        s.pop();
        int curr = heights[tp]*(s.empty()?n:(n-s.top()-1));
        res = max(res, curr);
     }
     return res;
    }
};