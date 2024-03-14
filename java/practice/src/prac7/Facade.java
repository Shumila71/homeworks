package prac7;

class SubsystemA {
    public void operationA() {
        System.out.println("SubsystemA: Performing operation A");
    }
}

class SubsystemB {
    public void operationB() {
        System.out.println("SubsystemB: Performing operation B");
    }
}

class SubsystemC {
    public void operationC() {
        System.out.println("SubsystemC: Performing operation C");
    }
}
public class Facade {
    private SubsystemA subsystemA;
    private SubsystemB subsystemB;
    private SubsystemC subsystemC;

    public Facade() {
        this.subsystemA = new SubsystemA();
        this.subsystemB = new SubsystemB();
        this.subsystemC = new SubsystemC();
    }

    public void performComplexOperation() {
        System.out.println("Facade: Performing complex operation by delegating to subsystems");
        subsystemA.operationA();
        subsystemB.operationB();
        subsystemC.operationC();
    }
}
