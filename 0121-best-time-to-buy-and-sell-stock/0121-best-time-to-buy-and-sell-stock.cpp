class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = prices[0];
        int res =0;
        for (int i =1;i< prices.size();i++){
            int sell = prices[i];
            if (buy < sell) res = max(res,sell-buy);
            else buy = sell;
        }
      return res;  
    }
};