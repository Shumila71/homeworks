package prac2;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        List<Human> h_list = new ArrayList<>();
        h_list.add(new Human(25, "Mark", "H.", LocalDate.of(1990, 5, 15), 66));
        h_list.add(new Human(30, "Alex", "S.", LocalDate.of(1985, 8, 20), 69));
        h_list.add(new Human(22, "Lion", "E.", LocalDate.of(2001, 3, 10), 50));
        System.out.println("Люди до изменений:");
        h_list.forEach(System.out::println);
        System.out.println("Добавим по 3 к весу каждого");
        h_list = h_list.stream()
                .map(human -> {
                    human.setWeight(human.getWeight()+3);
                    return human;
            }).collect(Collectors.toList());
        h_list.forEach(System.out::println);


        System.out.println("Отсортируем по весу");
        h_list=h_list.stream().sorted((human1,human2) -> human2.getWeight() - human1.getWeight()).collect(Collectors.toList());
        h_list.forEach(System.out::println);


        System.out.println("Отфильтруем по дата рождения");
        h_list.stream().filter(human -> human.getBirthDate().isBefore(LocalDate.of(2000,1,1))).forEach(System.out::println);


        int sum = h_list.stream().mapToInt(Human::getWeight).sum();
        System.out.println("Сумма всех весов:" + sum);
    }
}
