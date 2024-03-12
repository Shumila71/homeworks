package prac5;

public class Main {
    public static void main(String[] args) {
        System.out.println(Singleton1.getInstance());
        System.out.println(Singleton3.getInstance());
        for (int i = 1; i < 4; i++)        {
            var t = new Thread(() -> {
                System.out.println(Singleton2.getInstance() + " " + Thread.currentThread().getName());
            });
            t.setName("Поток " + i);
            t.start();
        }
    }
}

class Singleton1{//ленивая инициализация
    private static Singleton1 instance;
    private Singleton1(){}
    public static Singleton1 getInstance(){
        if (instance == null){
            instance = new Singleton1();
        }
        return instance;
    }
}
class Singleton2 {//потокобезопасный
    private static Singleton2 instance;
    private Singleton2(){}
    public static synchronized Singleton2 getInstance(){
        if (instance == null){
            instance = new Singleton2();
        }
        return instance;
    }
}
class Singleton3 {//холодная инициализация
    private static final Singleton3 instance = new Singleton3();
    private Singleton3() {}
    public static Singleton3 getInstance() {
        return instance;
    }
}
