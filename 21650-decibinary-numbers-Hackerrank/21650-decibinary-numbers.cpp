#include <bits/stdc++.h>
#define pb push_back
#define sqr(x) (x)*(x)
#define sz(a) int(a.size())
#define reset(a,b) memset(a,b,sizeof(a))
#define oo 1000000007

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

int arr[111],cnt,n;
ll dp[30][20],sum[311111];

ll get(int i, int val){
    if(i==0) return arr[i]+val<=9;
    if(val>=20) return 0;
    if(dp[i][val]!=-1) return dp[i][val];
    ll &res = dp[i][val];
    res = 0;
    val += arr[i];
    for(int v=0; v<=val && v<=9; ++v)
        res += get(i-1, (val-v)*2);
    return res;
}

void convert(int v){
    cnt=0;
    while(v){
        arr[cnt++] = v&1;
        v>>=1;
    }
}

ll f(int v){
    if(v==0) return 1;
    convert(v);
    reset(dp,-1);
    return get(cnt-1, 0);
}

ll trackNum(int v, ll k){
    convert(v);
    reset(dp,-1);
    get(cnt-1, 0);
    int val = 0;
    for(int i=cnt-1; i>=0; --i){
        val += arr[i];
        if(i==0){
            arr[i] = val;
            break;
        }
        for(int v=0; v<=val && v<=9; ++v){
            ll x = get(i-1, (val-v)*2);
            if(x < k) k -= x;
            else{
                arr[i] = v;
                val = (val-v)*2;
                break;
            }
        }
    }
    ll res = 0;
    for(int i=cnt-1; i>=0; --i) res=res*10+arr[i];
    return res;
}

ll query(ll t){
    if(t==1) return 0;
    --t;
    int pos,l=1,r=n,mid;
    while(l<=r){
        mid=(l+r)/2;
        if(sum[mid]>=t){
            pos=mid;
            r=mid-1;
        }else
            l=mid+1;
    }
    t -= sum[pos-1];
    return trackNum(pos, t);
}

int main(){
//    freopen("input.txt","r",stdin);
    for(n=1; ; ++n){
        sum[n]=sum[n-1];
        sum[n]+=f(n);
        if(sum[n]>(ll)1e16) break;
    }
    int q;
    ll v;
    cin>>q;
    while(q--){
        cin>>v;
        cout<<query(v)<<endl;
    }
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna