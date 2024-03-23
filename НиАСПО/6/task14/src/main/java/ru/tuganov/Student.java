package ru.tuganov;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
//@Table(name = "student")
public class Student {
    @Id
    @GeneratedValue(strategy= GenerationType.AUTO)
    //@Column(name = "id")
    private Integer id;

    //@Column(name = "name")
    private String name;

    //@Column(name = "sir_name")
    private String sir_name;
}
