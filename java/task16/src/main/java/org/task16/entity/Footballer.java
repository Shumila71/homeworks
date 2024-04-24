package org.task16.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.Setter;

@Entity
@Getter
@Setter
@Table(name="footballers")
public class Footballer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(name="firstName", nullable=false, length=25)
    private String firstName;
    @Column(name="lastName", nullable=false, length=25)
    private String lastName;
//    @Column(name="game_id")
//    public Long gameId;

    @ManyToOne
    private Team team;
}
