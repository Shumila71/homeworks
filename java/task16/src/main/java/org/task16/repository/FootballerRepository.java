package org.task16.repository;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Repository;
import org.task16.entity.Team;
import org.task16.entity.Footballer;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class FootballerRepository
{
    private final SessionFactory sessionFactory;
    private Session session;

    @PostConstruct
    void init()
    {
        session = sessionFactory.openSession();
    }

    public void AddFootballer(Footballer footballer, Long gameId)
    {
        var t = session.beginTransaction();
        var team = session.get(Team.class, gameId);
        footballer.setTeam(team);
        session.persist(footballer);
        t.commit();
    }

    public void DeleteFootballer(Long id)
    {
        var t = session.beginTransaction();
        session.remove(session.find(Footballer.class, id));
        t.commit();
    }

    public List<Footballer> GetAllFootballer()
    {
        var t = session.beginTransaction();
        var footballers = session.createQuery("select g from Footballer g", Footballer.class).getResultList();
        t.commit();
        return footballers;
    }

    public Footballer GetFootballerById(Long id)
    {
        var t = session.beginTransaction();
        var team = session.find(Footballer.class, id);
        t.commit();
        return team;
    }
}
