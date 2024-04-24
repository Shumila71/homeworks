package org.task16.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Entity
@Table(name = "teams")
@Getter
@Setter
public class Team
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    @Column(name="name", nullable=false, length=25)
    private String name;
    @Column(name="creation_date", nullable=false, length=25)
    private String creationDate;
    @OneToMany
    private List <Footballer> footballers;
}