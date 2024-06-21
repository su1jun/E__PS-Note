import java.util.Scanner;

public class S2_1699 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.close();

        int[] dp = new int[N + 1];
        dp[0] = 0;

        for (int i = 1; i <= N; i++) {
            dp[i] = i;
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i-j * j] + 1);
            }
        }

        System.out.println(dp[N]);
    }
}
