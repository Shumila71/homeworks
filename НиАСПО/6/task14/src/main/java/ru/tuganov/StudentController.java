package ru.tuganov;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
@RequiredArgsConstructor
public class StudentController {

    private final StudentRepository repository;

    @GetMapping("/result")
    public String getStudent(Model model) {
        populateModel(model);

        return "result";
    }

    private void populateModel(Model model) {
        final Iterable<Student> studentList = repository.findAll();
        model.addAttribute("studentList", studentList);
    }

    @GetMapping("/student")
    public String addStudentForm(Model model) {
        model.addAttribute("student", new Student());

        return "student";
    }

    @PostMapping("/add-student")
    public String addStudentSubmit(@ModelAttribute Student student, Model model) {
        repository.save(student);
        populateModel(model);

        return "result";
    }
}
