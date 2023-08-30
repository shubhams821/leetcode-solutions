class Solution {
public:
    int findPeakElement(vector<int>& nums) {

        int low =0, n= nums.size(), high = n-1;
        while (low <= high){
            int mid = (low + high)/2;
            if ((mid ==0 or nums[mid-1]<= nums[mid]) && ( mid == n - 1 or nums[mid+1]<= nums[mid])) return mid;

            // left sorted
            if (mid > 0 && nums[mid] <= nums[mid-1]) high = mid-1;

            //  right sorted
            else low = mid+1;
        }        
        return -1;
    }
};