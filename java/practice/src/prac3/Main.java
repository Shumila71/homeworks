package prac3;

public class Main {
    public static void main(String[] args) {
        ConcurrentSet<Integer> concurrentSet = new ConcurrentSet<>();

        Thread thread1 = new Thread(() -> {
            try {
                for (int i = 0; i < 5; i++) {
                    concurrentSet.add(i);
                    System.out.println("Thread 1 added: " + i);
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread thread2 = new Thread(() -> {
            try {
                for (int i = 5; i < 10; i++) {
                    concurrentSet.add(i);
                    System.out.println("Thread 2 added: " + i);
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        thread1.start();
        thread2.start();
    }
}

