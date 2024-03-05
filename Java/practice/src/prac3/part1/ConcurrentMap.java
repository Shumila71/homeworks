package prac3.part1;

import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class ConcurrentMap<K, V> {
    private final Map<K, V> map;
    private final Lock lock;

    public ConcurrentMap() {
        map = new HashMap<>();
        lock = new ReentrantLock();
    }

    public void put(K key, V value) {
        lock.lock();
        try {
            map.put(key, value);
        } finally {
            lock.unlock();
        }
    }
}