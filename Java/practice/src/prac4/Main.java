package prac4;

public class Main {
    public static void main(String[] args) {
        CustomExecutorService executorService = new CustomExecutorService(5);

        for (int i = 0; i < 10; i++) {
            final int taskNumber = i;
            executorService.submit(() -> {
                System.out.println("Task " + taskNumber + " executed by thread " + Thread.currentThread().getName());
            });
        }

        executorService.shutdown();
    }
}
