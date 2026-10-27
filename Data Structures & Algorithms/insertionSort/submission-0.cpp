class Solution {
public:
    vector<vector<Pair>> insertionSort(vector<Pair>& pairs) {
        vector<vector<Pair>> states;
        int n = pairs.size();
        
        for (int i = 0; i < n; i++) {
            int j = i - 1;
            Pair key = pairs[i];
            
            while (j >= 0 && pairs[j].key > key.key) {
                pairs[j + 1] = pairs[j];
                j--;
            }
            pairs[j + 1] = key;
            
            states.push_back(pairs);
        }
        
        return states;
    }
};