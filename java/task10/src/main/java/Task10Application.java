import config.BeanConfig;
import interfaces.Programmer;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Task10Application {
    public static void main(String[] args)
    {
        ApplicationContext context = new AnnotationConfigApplicationContext(BeanConfig.class);

        Programmer bean = context.getBean("GetJunior", Programmer.class);
        bean.doCoding();
        bean = context.getBean("GetMiddle", Programmer.class);
        bean.doCoding();
        bean = context.getBean("GetSenior", Programmer.class);
        bean.doCoding();
    }
}
