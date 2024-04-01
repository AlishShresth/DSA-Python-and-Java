package important;

public class sortedRotatedArray {
  public static int numsRotation(int[] nums, int target) {
    if (nums[0] == target) {
      return 0;
    }
    int count = 1;
    int ans = -1;
    for (int i = 0; i < nums.length - 1; i++) {
      if (nums[i] > nums[i + 1]) {
        ans = count;
      }
      if (nums[i] == target) {
        return ans;
      }
      if (nums[i] < nums[i + 1]) {
        count++;
      }

    }
    if (nums[nums.length - 1] == target) {
      return ans;
    }
    return -1;
  }

  public static void main(String[] args) {
    int nums[] = { 1 };
    System.out.println(numsRotation(nums, 10));
  }
}
