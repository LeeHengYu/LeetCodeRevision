#include <vector>

class Solution
{
public:
    int maxArea(vector<int> &height)
    {
        double max_area = 0;
        int i = 0, j = height.size() - 1;
        int high = min(height[i], height[j]);

        max_area = high * (j - i);

        while (i < j)
        {
            if (height[i] <= high)
                i++;
            if (height[j] <= high)
                j--;
            high = min(height[i], height[j]);
            if (high * (j - i) > max_area)
            {
                max_area = high * (j - i);
            }
        }

        return int(max_area);
    }
};