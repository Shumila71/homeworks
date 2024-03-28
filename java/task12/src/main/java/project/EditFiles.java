package project;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.springframework.stereotype.Service;

import java.io.*;

@Service
public class EditFiles
{
    String file1 = "D:\\code\\_4\\java\\task12\\f1.txt";
    String file2 = "D:\\code\\_4\\java\\task12\\f2.txt";

    @PostConstruct
    public void PostConstruct() throws IOException{
        var bufferedWriter = new BufferedWriter(new FileWriter(file2));

        if (new File(file1).exists()){
            var bufferedReader = new BufferedReader(new FileReader(file1));
            var strBuilder = new StringBuilder();
            String line;

            while ((line = bufferedReader.readLine()) != null){
                strBuilder.append(line);
            }
            bufferedWriter.write(String.valueOf(strBuilder.hashCode()));
            System.out.println("Текст из 1 файла был передан в виде хеша во 2");
            bufferedReader.close();
        }
        else        {
            System.out.println("Первого файла нет");
            bufferedWriter.write("null");
        }
        bufferedWriter.close();
    }

    @PreDestroy
    public void PreDestroy(){
        if(new File(file1).delete()){
            System.out.println("Первый файл удален");
        }
    }
}