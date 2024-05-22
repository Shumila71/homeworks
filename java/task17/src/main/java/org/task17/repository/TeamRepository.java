package org.task17.repository;

import jakarta.annotation.PostConstruct;
import jakarta.persistence.criteria.CriteriaBuilder;
import jakarta.persistence.criteria.CriteriaQuery;
import jakarta.persistence.criteria.Root;
import lombok.RequiredArgsConstructor;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.stereotype.Repository;
import org.task17.entity.Team;

import java.util.List;

@Repository
@RequiredArgsConstructor
public class TeamRepository
{
    private final SessionFactory sessionFactory;
    private Session session;

    @PostConstruct
    void init()
    {
        session = sessionFactory.openSession();
    }

    public void AddTeam(Team team)
    {
        var t = session.beginTransaction();
        session.persist(team);
        t.commit();
    }

    public void DeleteTeam(Long id)
    {
        var t = session.beginTransaction();
        session.remove(session.find(Team.class, id));
        t.commit();
    }

    public List<Team> GetAllTeam()
    {
        var t = session.beginTransaction();
        var teams = session.createQuery("select g from Team g", Team.class).getResultList();
        t.commit();
        return teams;
    }

    public Team GetTeamById(Long id)
    {
        var t = session.beginTransaction();
        var team = session.find(Team.class, id);
        t.commit();
        return team;
    }
    // Filter
    public List<Team> FilterTeamsByName(String pattern)
    {
        CriteriaBuilder builder = session.getCriteriaBuilder();
        CriteriaQuery<Team> criteriaQuery = builder.createQuery(Team.class);
        Root<Team> root = criteriaQuery.from(Team.class);

        var pred = builder.like(root.get("name"), "%"+pattern+"%");
        var query = criteriaQuery.select(root).where(pred);
        return session.createQuery(query).getResultList();
    }

    public List<Team> FilterTeamsByDate(String pattern)
    {
        CriteriaBuilder builder = session.getCriteriaBuilder();
        CriteriaQuery<Team> criteriaQuery = builder.createQuery(Team.class);
        Root<Team> root = criteriaQuery.from(Team.class);

        var pred = builder.like(root.get("creationDate"), "%"+pattern+"%");
        var query = criteriaQuery.select(root).where(pred);
        return session.createQuery(query).getResultList();
    }
}
