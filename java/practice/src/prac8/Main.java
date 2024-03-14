package prac8;

import java.util.ArrayList;
import java.util.List;

//ПОСЕТИТЕЛЬ
interface Visitor {
    void visit(ElementA element);
    void visit(ElementB element);
}

class ConcreteVisitor implements Visitor {
    @Override
    public void visit(ElementA element) {
        System.out.println("Visitor is visiting ElementA");
    }

    @Override
    public void visit(ElementB element) {
        System.out.println("Visitor is visiting ElementB");
    }
}

interface Element {
    void accept(Visitor visitor);
}

class ElementA implements Element {
    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}

class ElementB implements Element {
    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }
}


//ПОСРЕДНИК
interface Mediator {
    void mediate(Colleague colleague);
}

class ConcreteMediator implements Mediator {
    @Override
    public void mediate(Colleague colleague) {
        System.out.println("Mediator is mediating the colleague");
        // Perform mediation logic here
    }
}

interface Colleague {
    void action();
}

class ConcreteColleague implements Colleague {
    private Mediator mediator;

    public ConcreteColleague(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public void action() {
        System.out.println("Colleague is performing action");
        // Perform some action
        mediator.mediate(this);
    }
}

// Main class
public class Main {
    public static void main(String[] args) {
        System.out.println("Паттерн Посетитель");
        List<Element> elements = new ArrayList<>();
        elements.add(new ElementA());
        elements.add(new ElementB());

        Visitor visitor = new ConcreteVisitor();
        for (Element element : elements) {
            element.accept(visitor);
        }

        System.out.println("Паттерн Посроедник");
        Mediator mediator = new ConcreteMediator();
        Colleague colleague = new ConcreteColleague(mediator);
        colleague.action();
    }
}

