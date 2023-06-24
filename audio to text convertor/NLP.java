import java.io.*;
import java.util.*;

public class NLP extends Filehandler
{
    public static void main(String[] args) 
    {
        senteneMaker();
    }
}

class Filehandler
{
    static void senteneMaker()
    {
        try 
        {
            BufferedReader reader = new BufferedReader(new FileReader("audio.txt"));

            List<String> words = new ArrayList<>();

            String line;
            while ((line = reader.readLine()) != null) 
            {
                String[] lineWords = line.split("\\s+"); // Split the line into words using whitespace as the delimiter
                for (String word : lineWords) 
                {
                    words.add(word);
                }
            }
            reader.close();

            // Convert the list of words to an array
            String[] wordsArray = words.toArray(new String[0]);

            // Print the words in the array
            for (String word : wordsArray) 
            {
                System.out.println(word);
            }
        } catch (IOException e) 
        {
            e.printStackTrace();
        }
    }
}