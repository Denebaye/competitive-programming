class Solution {
public:
   long long numberOfWays(string s) {
       vector<vector<long long>> dp(2,vector<long long> (2,0));
       vector<vector<long long>> tp(2,vector<long long> (2,0));
       dp[0][0] = s[0]=='0'?1:0;
       dp[0][1] = s[0]=='1'?1:0;
       long long ans = 0;
       for(int i=1;i<s.size();i++){
           
           if(s[i]=='0'){
               tp[0][0] = dp[0][0]+1;
               tp[0][1] = dp[0][1];
               tp[1][0] = dp[0][1]+dp[1][0];
               tp[1][1] = dp[1][1];
               ans+=dp[1][1];
           }
           else{
               tp[0][0] = dp[0][0];
               tp[0][1] = dp[0][1]+1;
               tp[1][0] = dp[1][0];
               tp[1][1] = dp[1][1]+dp[0][0];
               ans+=dp[1][0];
           }
           
           dp = tp;
       }
       return ans;
       
       
   }
};
