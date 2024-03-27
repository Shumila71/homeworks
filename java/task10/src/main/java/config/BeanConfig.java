package config;

import component.Junior;
import component.Middle;
import component.Senior;
import interfaces.Programmer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan
public class BeanConfig {
    @Bean
    public Programmer GetJunior(){
        return new Junior();
    }
    @Bean
    public Programmer GetMiddle(){
        return new Middle();
    }
    @Bean
    public Programmer GetSenior(){
        return new Senior();
    }
}
