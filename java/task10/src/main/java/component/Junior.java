package component;

import interfaces.Programmer;
import org.springframework.stereotype.Component;

@Component
public class Junior implements Programmer {
    @Override
    public void doCoding() {
        System.out.println("Junior coding");
    }
}
