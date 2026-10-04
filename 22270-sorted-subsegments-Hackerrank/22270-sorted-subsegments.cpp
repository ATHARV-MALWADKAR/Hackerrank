#include <bits/stdc++.h>
using namespace std;

int n, q, k;
vector<int> a;
vector<pair<int,int>> qs;

vector<int> sm, lz;

void build(int node, int l, int r, int x) {
    lz[node] = -1;
    if (l == r) { sm[node] = (a[l] >= x); return; }
    int m = (l + r) / 2;
    build(2*node, l, m, x);
    build(2*node+1, m+1, r, x);
    sm[node] = sm[2*node] + sm[2*node+1];
}

void apply(int node, int l, int r, int v) {
    sm[node] = v * (r - l + 1);
    lz[node] = v;
}

void push(int node, int l, int r) {
    if (lz[node] != -1) {
        int m = (l + r) / 2;
        apply(2*node, l, m, lz[node]);
        apply(2*node+1, m+1, r, lz[node]);
        lz[node] = -1;
    }
}

void update(int node, int l, int r, int ql, int qr, int v) {
    if (ql > qr || qr < l || r < ql) return;
    if (ql <= l && r <= qr) { apply(node, l, r, v); return; }
    push(node, l, r);
    int m = (l + r) / 2;
    update(2*node, l, m, ql, qr, v);
    update(2*node+1, m+1, r, ql, qr, v);
    sm[node] = sm[2*node] + sm[2*node+1];
}

int query(int node, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return sm[node];
    push(node, l, r);
    int m = (l + r) / 2;
    return query(2*node, l, m, ql, qr) + query(2*node+1, m+1, r, ql, qr);
}

bool check(int x) {
    build(1, 0, n-1, x);
    for (auto &[l, r] : qs) {
        int ones = query(1, 0, n-1, l, r);
        int zeros = (r - l + 1) - ones;
        update(1, 0, n-1, l, l + zeros - 1, 0);
        update(1, 0, n-1, l + zeros, r, 1);
    }
    return query(1, 0, n-1, k, k) == 1;
}

int main() {
    scanf("%d %d %d", &n, &q, &k);
    a.resize(n);
    for (auto &x : a) scanf("%d", &x);
    qs.resize(q);
    for (auto &p : qs) scanf("%d %d", &p.first, &p.second);

    sm.assign(4*n, 0);
    lz.assign(4*n, -1);

    vector<int> vals = a;
    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int lo = 0, hi = vals.size() - 1;
    while (lo < hi) {
        int mid = (lo + hi + 1) / 2;
        if (check(vals[mid])) lo = mid;
        else hi = mid - 1;
    }
    printf("%d\n", vals[lo]);
    return 0;
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna