import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    static int intervalSelection(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparing(interval -> interval[1]));

        int lastSingle = -1;
        int lastDouble = -1;

        int skipped = 0;
        
        for (int[] interval : intervals) {
            int start = interval[0];
            if (start <= lastDouble) {
                skipped++;
            } else if (start <= lastSingle) {
                lastDouble = lastSingle;
                lastSingle = interval[1];
            } else {
                lastSingle = interval[1];
            }
        }

        return intervals.length - skipped;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int s = Integer.parseInt(scanner.nextLine().trim());

        for (int sItr = 0; sItr < s; sItr++) {
            int n = Integer.parseInt(scanner.nextLine().trim());

            int[][] intervals = new int[n][2];

            for (int intervalsRowItr = 0; intervalsRowItr < n; intervalsRowItr++) {
                String[] intervalsRowItems = scanner.nextLine().split(" ");

                for (int intervalsColumnItr = 0; intervalsColumnItr < 2; intervalsColumnItr++) {
                    int intervalsItem = Integer.parseInt(intervalsRowItems[intervalsColumnItr].trim());
                    intervals[intervalsRowItr][intervalsColumnItr] = intervalsItem;
                }
            }

            int result = intervalSelection(intervals);

            bufferedWriter.write(String.valueOf(result));
            bufferedWriter.newLine();
        }

        bufferedWriter.close();
    }
}


// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna