package ch01_1;

import edu.princeton.cs.algs4.StdIn;

/* File Name: ex21
 * Author: @bGZo
 * Created Time: 4/17/2022 22:01
 * License: MIT
 * Description:
 */
public class ex21 {
    public static void main(String[] args) {
        System.out.print("Please input count:");
        int n = StdIn.readInt();
        String[] nameArray = new String[n];
        int[] integerArray1 = new int[n];
        int[] integerArray2 = new int[n];
        for (int i = 0; i < n; i++) {
            nameArray[i] = StdIn.readString();
            integerArray1[i] = StdIn.readInt();
            integerArray2[i] = StdIn.readInt();
        }
        System.out.println("----------------------------");
        for (int i = 0; i < n; i++) {
            System.out.printf("|%4s|%4d|%4d|%6.3f|\n", nameArray[i], integerArray1[i], integerArray2[i],
                    (float) integerArray1[i] / integerArray2[i]);
            if (i != n - 1) {
                System.out.println("----------------------------");
            }
        }
        System.out.println("弩----拂----拂----拂------彼");

    }
}
