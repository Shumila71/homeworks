package prac3;

import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.Semaphore;

public class ConcurrentSet<T> {
    private Set<T> set;
    private Semaphore semaphore;

    public ConcurrentSet() {
        set = new HashSet<>();
        semaphore = new Semaphore(1); // Одна разрешающая семафор
    }

    public boolean add(T element) throws InterruptedException {
        semaphore.acquire(); // Захватываем разрешение
        boolean added = set.add(element);
        semaphore.release(); // Освобождаем разрешение
        return added;
    }
}