package prac3.part1;

public class Main {
    public static void main(String[] args) {
        ConcurrentMap<String, Integer> concurrentMap = new ConcurrentMap<>();

        Thread thread1 = new Thread(() -> {
            try {
                for (int i = 0; i < 5; i++) {
                    concurrentMap.put("Key" + i, i);
                    System.out.println("Thread 1 added: Key" + i + " -> " + i);
                    Thread.sleep(1000);
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });

        Thread thread2 = new Thread(() -> {
            try {
                for (int i = 5; i < 10; i++) {
                    concurrentMap.put("Key" + i, i);
                    System.out.println("Thread 2 added: Key" + i + " -> " + i);
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

