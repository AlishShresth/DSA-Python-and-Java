package important;

import java.util.HashSet;

public class containsDuplicate {
  public static boolean containsDup(int[] arr) {
    HashSet<Integer> set = new HashSet<>();
    for (int i = 0; i < arr.length; i++) {
      if (set.contains(arr[i])) {
        return true;
      } else {
        set.add(arr[i]);
      }
    }
    return false;

  }

  public static void main(String[] args) {
    int arr[] = { 1, 2, 3, 4, 1, 1 };
    System.out.println(containsDup(arr));
  }

}
