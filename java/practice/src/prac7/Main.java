package prac7;

public class Main {
    public static void main(String[] args) {
        System.out.println("Паттерн «Адаптер»:");
        new Adapter();
        System.out.println();
        System.out.println("Паттерн «Фасад»:");
        Facade facade = new Facade();
        facade.performComplexOperation();
    }
}
