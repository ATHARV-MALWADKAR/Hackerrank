#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int n; ll c;
vector<ll> P,Q,own;
struct R{ll s,t;ll o;int id;};
vector<R> allr, crr;
vector<ll> Tg;
vector<int> crRank;
vector<ll> S,suf,Sx,Tk; vector<int> kept;
int LOGW=1, WN=0, WW=1;
vector<unsigned long long> BV; vector<int> CU, NZ, cur_, nxt_;

void buildWM(const vector<int>&v,int m){
    WN=v.size(); LOGW=1; while((1<<LOGW)<=m) LOGW++;
    WW=(WN>>6)+1;
    BV.assign((size_t)LOGW*WW,0); CU.assign((size_t)LOGW*WW,0); NZ.assign(LOGW,0);
    cur_=v; nxt_.resize(WN);
    for(int lv=LOGW-1;lv>=0;lv--){
        unsigned long long* bv=&BV[(size_t)lv*WW]; int* cu=&CU[(size_t)lv*WW];
        int ones=0;
        for(int i=0;i<WN;i++) if((cur_[i]>>lv)&1) bv[i>>6]|=1ULL<<(i&63);
        for(int w=0;w<WW;w++){ cu[w]=ones; ones+=__builtin_popcountll(bv[w]); }
        NZ[lv]=WN-ones;
        int p0=0,p1=NZ[lv];
        for(int i=0;i<WN;i++){
            if((cur_[i]>>lv)&1) nxt_[p1++]=cur_[i]; else nxt_[p0++]=cur_[i];
        }
        swap(cur_,nxt_);
    }
}
// number of values in [x1,x2) among positions [l,r)
int cntRange(int l,int r,int x1,int x2){
    int la=l,ra=r,lb=l,rb=r,ca=0,cb=0;
    bool capA = x2>=(1<<LOGW), capB = x1>=(1<<LOGW);
    for(int lv=LOGW-1;lv>=0;lv--){
        const unsigned long long* bv=&BV[(size_t)lv*WW]; const int* cu=&CU[(size_t)lv*WW];
        int nz=NZ[lv];
        if(!capA){
            int l1=cu[la>>6]+__builtin_popcountll(bv[la>>6]&((1ULL<<(la&63))-1));
            int r1=cu[ra>>6]+__builtin_popcountll(bv[ra>>6]&((1ULL<<(ra&63))-1));
            int l0=la-l1, r0=ra-r1;
            if((x2>>lv)&1){ ca+=r0-l0; la=nz+l1; ra=nz+r1; } else { la=l0; ra=r0; }
        }
        if(!capB){
            int l1=cu[lb>>6]+__builtin_popcountll(bv[lb>>6]&((1ULL<<(lb&63))-1));
            int r1=cu[rb>>6]+__builtin_popcountll(bv[rb>>6]&((1ULL<<(rb&63))-1));
            int l0=lb-l1, r0=rb-r1;
            if((x1>>lv)&1){ cb+=r0-l0; lb=nz+l1; rb=nz+r1; } else { lb=l0; rb=r0; }
        }
    }
    if(capA) ca=r-l;
    if(capB) cb=r-l;
    return ca-cb;
}

vector<int> ordP, ordQ, iAL, iBL, K1, K2, TL, TR;
bool check(ll D){
    if(D==0) return true;
    S.clear(); vector<ll> tt; tt.reserve(allr.size());
    for(auto&r:allr) if(r.o>=D){S.push_back(r.s);tt.push_back(r.t);}
    suf.assign(S.size(),0);
    for(int i=(int)S.size()-1;i>=0;i--)
        suf[i]=min(tt[i], i+1<(int)S.size()?suf[i+1]:LLONG_MAX);
    Sx.clear(); kept.clear(); Tk.clear();
    for(int k=0;k<(int)crr.size();k++)
        if(crr[k].o>=D){Sx.push_back(crr[k].s);kept.push_back(k);Tk.push_back(crr[k].t);}
    int m=Tg.size(), ns=S.size(), nx=Sx.size();
    {
        int a1=0,a2=0,a3=0;
        for(int i:ordP){ if(own[i]<D) continue;
            ll al=P[i]+D, bh=P[i]+c-D;
            while(a1<ns && S[a1]<al) a1++;
            while(a2<nx && Sx[a2]<al) a2++;
            while(a3<m && Tg[a3]<=bh) a3++;
            iAL[i]=a1; K1[i]=a2; TR[i]=a3-1;
        }
    }
    {
        int b1=0,b2=0,b3=0;
        for(int i:ordQ){ if(own[i]<D) continue;
            ll bl=Q[i]+D, ah=Q[i]-D;
            while(b1<ns && S[b1]<bl) b1++;
            while(b2<nx && Sx[b2]<=ah) b2++;
            while(b3<m && Tg[b3]<bl) b3++;
            iBL[i]=b1; K2[i]=b2; TL[i]=b3;
        }
    }
    bool built=false;
    for(int i=0;i<n;i++){
        if(own[i]<D) continue;
        ll al=P[i]+D, ah=Q[i]-D, bl=Q[i]+D, bh=P[i]+c-D;
        bool hA=al<=ah, hB=bl<=bh;
        if(hA){int j=iAL[i]; if(j<ns && suf[j]<=ah) return true;}
        if(hB){int j=iBL[i]; if(j<ns && suf[j]<=bh) return true;}
        if(hA&&hB){
            int k1=K1[i],k2=K2[i],tl=TL[i],tr=TR[i];
            if(k1>=k2||tl>tr) continue;
            if(k2-k1<=40){
                for(int j=k1;j<k2;j++) if(Tk[j]>=bl&&Tk[j]<=bh) return true;
                continue;
            }
            if(!built){
                built=true; vector<int> v(kept.size());
                for(size_t j=0;j<kept.size();j++) v[j]=crRank[kept[j]];
                buildWM(v,m);
            }
            if(cntRange(k1,k2,tl,tr+1)>0) return true;
        }
    }
    return false;
}
int main(){
    scanf("%d %lld",&n,&c);
    P.resize(n);Q.resize(n);own.resize(n);
    ll mx=0;
    for(int i=0;i<n;i++){
        scanf("%lld %lld",&P[i],&Q[i]); if(P[i]>Q[i]) swap(P[i],Q[i]);
        ll d=Q[i]-P[i]; own[i]=min(d,c-d); mx=max(mx,own[i]);
    }
    for(int i=0;i<n;i++){
        ll p=P[i],q=Q[i],o=own[i];
        allr.push_back({p,q,o,i});allr.push_back({q,p+c,o,i});
        allr.push_back({p+c,q+c,o,i});allr.push_back({q+c,p+2*c,o,i});
        crr.push_back({p,q,o,i});
    }
    auto cmp=[](const R&a,const R&b){return a.s<b.s;};
    sort(allr.begin(),allr.end(),cmp); sort(crr.begin(),crr.end(),cmp);
    for(auto&r:crr) Tg.push_back(r.t);
    sort(Tg.begin(),Tg.end());Tg.erase(unique(Tg.begin(),Tg.end()),Tg.end());
    crRank.resize(crr.size());
    for(size_t k=0;k<crr.size();k++)
        crRank[k]=lower_bound(Tg.begin(),Tg.end(),crr[k].t)-Tg.begin();
    ordP.resize(n);ordQ.resize(n);
    iota(ordP.begin(),ordP.end(),0);iota(ordQ.begin(),ordQ.end(),0);
    sort(ordP.begin(),ordP.end(),[&](int x,int y){return P[x]<P[y];});
    sort(ordQ.begin(),ordQ.end(),[&](int x,int y){return Q[x]<Q[y];});
    iAL.assign(n,0);iBL.assign(n,0);K1.assign(n,0);K2.assign(n,0);TL.assign(n,0);TR.assign(n,0);
    ll lo=0,hi=min(c/2,mx);
    while(lo<hi){ll mid=(lo+hi+1)/2; if(check(mid)) lo=mid; else hi=mid-1;}
    printf("%lld\n",lo);
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna