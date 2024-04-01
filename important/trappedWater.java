package important;

public class trappedWater {
  public static void printArr(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

  public static int trap(int[] height) {
    int size = height.length;

    // calculate left max boundary array
    int leftMaxBoundary[] = new int[size];
    leftMaxBoundary[0] = height[0];
    for (int i = 1; i < size; i++) {
      leftMaxBoundary[i] = Math.max(height[i], leftMaxBoundary[i - 1]);
    }
    // printArr(leftMaxBoundary);

    // calculate right max boundary array
    int rightMaxBoundary[] = new int[size];
    rightMaxBoundary[size - 1] = height[size - 1];
    for (int i = size - 2; i >= 0; i--) {
      rightMaxBoundary[i] = Math.max(height[i], rightMaxBoundary[i + 1]);
    }
    // printArr(rightMaxBoundary);

    // calculate trapped water
    int trappedWater = 0;
    // System.out.println("Trapped water = " + trappedWater);
    for (int i = 0; i < size; i++) {
      // calculate water level for each bar
      // waterlevel = min(leftmax bound, rightmax bound)
      int waterLevel = Math.min(leftMaxBoundary[i], rightMaxBoundary[i]);

      // trappedwater = waterlevel - height[i]
      trappedWater += waterLevel - height[i];
    }
    return trappedWater;
  }

  public static void main(String[] args) {
    int height[] = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
    int ans = trap(height);
    System.out.println(ans);
  }
}