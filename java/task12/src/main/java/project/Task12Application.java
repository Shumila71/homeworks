package project;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class Task12Application{
    public static void main(String[] args){
        ApplicationContext context = SpringApplication.run(Task12Application.class, args);
        new EditFiles();
        SpringApplication.exit(context);
    }
}
