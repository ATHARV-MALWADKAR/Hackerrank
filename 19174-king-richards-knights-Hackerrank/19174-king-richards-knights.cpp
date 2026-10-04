#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    ll n; int m;
    scanf("%lld %d", &n, &m);
    vector<ll> A(m + 1), B(m + 1), D(m + 1);
    for (int i = 1; i <= m; i++) scanf("%lld %lld %lld", &A[i], &B[i], &D[i]);

    // T_k(r,c) = (m00*r + m01*c + tr, m10*r + m11*c + tc)
    vector<ll> m00(m + 1), m01(m + 1), m10(m + 1), m11(m + 1), tr(m + 1), tc(m + 1);
    m00[0] = 1; m01[0] = 0; m10[0] = 0; m11[0] = 1; tr[0] = 0; tc[0] = 0;
    for (int k = 1; k <= m; k++) {
        ll a = A[k], b = B[k], d = D[k];
        // r' = a - b + c1,  c' = a + b + d - r1
        m00[k] = m10[k - 1]; m01[k] = m11[k - 1]; tr[k] = tc[k - 1] + a - b;
        m10[k] = -m00[k - 1]; m11[k] = -m01[k - 1]; tc[k] = -tr[k - 1] + a + b + d;
    }

    int q;
    scanf("%d", &q);
    while (q--) {
        ll L;
        scanf("%lld", &L);
        ll r = L / n + 1, c = L % n + 1;

        auto apply = [&](int k, ll &rr, ll &cc) {
            rr = m00[k] * r + m01[k] * c + tr[k];
            cc = m10[k] * r + m11[k] * c + tc[k];
        };
        auto inside = [&](int k) {           // is T_{k-1}(p) inside square k ?
            ll rr, cc;
            apply(k - 1, rr, cc);
            return rr >= A[k] && rr <= A[k] + D[k] && cc >= B[k] && cc <= B[k] + D[k];
        };

        int lo = 0, hi = m;                  // largest k with inside(k) true, else 0
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (inside(mid)) lo = mid; else hi = mid - 1;
        }
        ll rr, cc;
        apply(lo, rr, cc);
        printf("%lld %lld\n", rr, cc);
    }
    return 0;
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna