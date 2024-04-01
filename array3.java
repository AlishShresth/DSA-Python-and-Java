public class array3 {
  public static void reverse(int arr[]) {
    int f = 0, l = arr.length - 1;
    while (f < l) {
      int temp = arr[f];
      arr[f] = arr[l];
      arr[l] = temp;
      f++;
      l--;
    }
  }

  public static void main(String[] args) {
    int arr[] = { 2, 4, 6, 8, 10, 12 };
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
    reverse(arr);
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

}
