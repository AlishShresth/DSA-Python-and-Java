package important;

public class maxSubarraySum {
  public static void subArray(int arr[]) {
    int minSum = Integer.MAX_VALUE;
    int maxSum = Integer.MIN_VALUE;
    for (int i = 0; i < arr.length; i++) {
      for (int j = i; j < arr.length; j++) {
        System.out.print("( ");
        int sum = 0;
        for (int k = i; k <= j; k++) {
          System.out.print(arr[k] + " ");
          sum += arr[k];
        }
        if (minSum > sum) {
          minSum = sum;
        }
        if (maxSum < sum) {
          maxSum = sum;
        }
        System.out.print(")");
      }
      System.out.println();
    }
    System.out.println("Max Sum = " + maxSum);
    System.out.println("Min Sum = " + minSum);
  }

  public static void prefixSum(int arr[]) {
    int prefix[] = new int[arr.length];
    prefix[0] = arr[0];
    int maxSum = prefix[0];
    for (int i = 1; i < arr.length; i++) {
      prefix[i] = prefix[i - 1] + arr[i];
      if (prefix[i] > maxSum) {
        maxSum = prefix[i];
      }
    }
    for (int i = 1; i < arr.length; i++) {
      int sum = 0;
      for (int j = i; j < arr.length; j++) {
        sum = prefix[j] - prefix[i - 1];
        if (sum > maxSum) {
          maxSum = sum;
        }
      }
    }
    System.out.println("MaxSum = " + maxSum);

  }

  public static void kadanesAlgo(int arr[]) {
    int sum = 0;
    int maxSum = sum;
    for (int i = 0; i < arr.length; i++) {
      if ((sum + arr[i]) < 0) {
        sum = 0;
      } else {
        sum += arr[i];
      }
      if (maxSum < sum) {
        maxSum = sum;
      }
    }
    System.out.println("MAx Sum = " + maxSum);
  }

  public static void main(String[] args) {
    // int arr[] = { 1, -2, 6, -1, 3 };
    int arr[] = { -2, -3, 4, -1, -2, 1, 5, -3 };
    // subArray(arr);
    // prefixSum(arr);
    kadanesAlgo(arr);
  }

}
