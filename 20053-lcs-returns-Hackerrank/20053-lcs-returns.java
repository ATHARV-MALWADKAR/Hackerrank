import java.io.*;
import java.util.*;

public class LCSReturns {

    BufferedReader br;
    PrintWriter out;
    StringTokenizer st;
    boolean eof;

    void solve() throws IOException {
        String a = nextToken();
        String b = nextToken();

        int n = a.length();
        int m = b.length();

        int[][] pref = new int[n + 1][m + 1];
        int[][] suff = new int[n + 1][m + 1];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (a.charAt(i) == b.charAt(j)) {
                    pref[i + 1][j + 1] = pref[i][j] + 1;
                } else {
                    pref[i + 1][j + 1] = Math.max(pref[i + 1][j],
                            pref[i][j + 1]);
                }
            }

        for (int i = n - 1; i >= 0; i--)
            for (int j = m - 1; j >= 0; j--) {
                if (a.charAt(i) == b.charAt(j)) {
                    suff[i][j] = suff[i + 1][j + 1] + 1;
                } else {
                    suff[i][j] = Math.max(suff[i][j + 1], suff[i + 1][j]);
                }
            }
        
        int cur = pref[n][m];
        
        int ret = 0;

        for (int i = 0; i <= n; i++) {
            boolean[] used = new boolean[256];
            for (int j = 0; j < m; j++) {
                if (used[b.charAt(j)]) {
                    continue;
                }
                
                int now = pref[i][j] + suff[i][j + 1] + 1;
                if (now == cur + 1) {
                    used[b.charAt(j)] = true;
                    ret++;
                }
            }
        }
        
        out.println(ret);
    }

    LCSReturns() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        out = new PrintWriter(System.out);
        solve();
        out.close();
    }

    public static void main(String[] args) throws IOException {
        new LCSReturns();
    }

    String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                eof = true;
                return null;
            }
        }
        return st.nextToken();
    }

    String nextString() {
        try {
            return br.readLine();
        } catch (IOException e) {
            eof = true;
            return null;
        }
    }

    int nextInt() throws IOException {
        return Integer.parseInt(nextToken());
    }

    long nextLong() throws IOException {
        return Long.parseLong(nextToken());
    }

    double nextDouble() throws IOException {
        return Double.parseDouble(nextToken());
    }
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna