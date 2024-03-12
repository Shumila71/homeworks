package prac1;

import java.util.function.Consumer;

public class Main implements Consumer<int[]> {
    @Override
    public void accept(int[] num){
        for (int n : num){
            System.out.println(n + " ");
        }
    }
    public static void main(String[] args) {
        int[] num ={3,12,4,52};
        Main cons = new Main();
        cons.accept(num);
        Consumer<int[]> printer = arr -> {
            for (int n : arr) {
                System.out.println(n + " ");
            }
        };
        printer.accept(num);
    }
}
