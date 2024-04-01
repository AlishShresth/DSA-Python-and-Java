import java.util.Scanner;

public class array1 {
  public static void main(String[] args) {
    int marks[] = new int[50];
    int numbers[] = { 1, 2, 3 };
    int moreNumbers[] = { 4, 5, 6 };
    String fruits[] = { "Apple", "Banana", "Orange" };
    Scanner sc = new Scanner(System.in);
    for (int i = 0; i < 3; i++) {
      marks[i] = sc.nextInt();
    }
    for (int i = 0; i < 3; i++) {
      System.out.println("marks of " + (i + 1) + " = " + marks[i]);
    }
  }
}
