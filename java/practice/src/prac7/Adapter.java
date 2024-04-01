package prac7;

public class Adapter{
    public Adapter(){
        Driver driver = new Driver();
        vehicle vehicle = new vehicle();
        driver.Travel(vehicle);

        Camel camel = new Camel();
        ITransport camelTransport = new CamelToTransportAdapter(camel);
        driver.Travel(camelTransport);
    }
}

class Driver{
    public void Travel(ITransport transport){
        transport.Drive();
    }
}

interface ITransport{
    void Drive();
}
class vehicle implements ITransport{
    public void Drive(){
        System.out.println("vehicle drived");
    }
}

interface IAnimal{
    void Move();
}
class Camel implements IAnimal{
    public void Move(){
        System.out.println("camel moved");
    }
}

class CamelToTransportAdapter implements ITransport{
    Camel camel;
    public CamelToTransportAdapter(Camel c){
        camel = c;
    }

    public void Drive(){
        camel.Move();
    }
}