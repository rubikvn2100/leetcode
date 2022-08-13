class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int N = s.length();
        int *next = new int[N];
        
        for(int i = 0; i < N; i++) {
            next[i] = -1;
        }
        
        int p;
        for(int i = 0; i < N; i++) {
            if(next[i] == -1) {
                p = i;
                for(int j = i + 1; j < N; j++) {
                    if(s[p] == s[j]) {
                        next[p] = j;
                        p = j;
                    }
                }
                next[p] = N;
            }
        }
        
        int i, j, upper_bound, max = 0;
        for(i = 0; i < N; i++) {
            upper_bound = next[i];
            for(j = i + 1; j < upper_bound; j++) {
                if(next[j] < upper_bound) {
                    upper_bound = next[j];
                }
            }
            
            if(j - i > max) {
                max = j - i;
            }
        }
        
        return max;
    }
};