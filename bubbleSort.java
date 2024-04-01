class bubbleSort {
  public static void bubbleSort(int arr[]) {
    for (int turns = 0; turns < arr.length - 1; turns++) {
      int swaps = 0;
      for (int j = 0; j < arr.length - 1 - turns; j++) {
        if (arr[j] > arr[j + 1]) {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
          swaps++;
        }
      }
      System.out.println("loop ran");
      if (swaps == 0) {
        break;
      }
    }
  }

  public static void selectionSort(int arr[]) {
    for (int i = 0; i < arr.length - 1; i++) {
      int posmin = i;
      for (int j = i + 1; j < arr.length; j++) {
        if (arr[j] < arr[posmin]) {
          posmin = j;
        }
      }
      int temp = arr[posmin];
      arr[posmin] = arr[i];
      arr[i] = temp;
    }
  }

  public static void insertionSort(int arr[]) {
    for (int i = 1; i < arr.length; i++) {
      int curr = arr[i];
      int prev = i - 1;
      while (prev >= 0 && arr[prev] > curr) {
        arr[prev + 1] = arr[prev];
        prev--;
      }
      arr[prev + 1] = curr;
    }
  }

  public static void printArr(int arr[]) {
    for (int i = 0; i < arr.length; i++) {
      System.out.print(arr[i] + " ");
    }
    System.out.println();
  }

  public static void main(String[] args) {
    int arr[] = { 5, 2, 1, 4, 3 };
    insertionSort(arr);
    printArr(arr);
  }
}