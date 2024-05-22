package org.task21;

import lombok.AllArgsConstructor;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.task21.entity.Team;

@Service
@AllArgsConstructor
public class EmailSender
{
    private final JavaMailSender javaMailSender;

    @Async
    public void sendEmail(Team team) {
        SimpleMailMessage message = new SimpleMailMessage();

        message.setFrom("vezuncik03@mail.ru");
        message.setTo("vezuncik03@mail.ru");
        message.setSubject("Info message");
        message.setText(team.toString());

        javaMailSender.send(message);
    }
}
