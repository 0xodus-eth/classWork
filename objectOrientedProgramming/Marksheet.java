
import java.util.Scanner;

public class Marksheet {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input details
        System.out.println("Department of Computer Science");
        System.out.println("End Semester Results");

        System.out.print("Enter your Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your Roll Number: ");
        String rollNumber = scanner.nextLine();

        System.out.print("Enter your Semester: ");
        String semester = scanner.nextLine();

        // Input marks
        System.out.println("Enter marks for each unit:");

        System.out.print("Database: ");
        int database = scanner.nextInt();

        System.out.print("Systems: ");
        int systems = scanner.nextInt();

        System.out.print("Algorithm: ");
        int algorithm = scanner.nextInt();

        System.out.print("Statistics: ");
        int statistics = scanner.nextInt();

        // Compute total and average
        int total = database + systems + algorithm + statistics;
        double average = total / 4.0;

        // Display results
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("                            Department of Computer Science                       ");
        System.out.println("                               End Semester Results                              ");
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("Name: " + name + "                     |Roll_No: " + rollNumber + "\t              |Semester: " + semester);
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("| Unit Code                  | Unit Name:                Score ");
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("| CCS2101                    | Database                  | " + database);
        System.out.println("| CCS2102                    | Systems                   | " + systems);
        System.out.println("| CCS2103                    | Algorithm                 | " + algorithm);
        System.out.println("| CCS2104                    | Statistics                | " + statistics);
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("|Total:                                                  | " + total);
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("|Average:                                                | " + String.format("%.2f", average));
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("|Grade:                                                  | " + "A");
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("                                         Recommendation  |       ");
        System.out.println("---------------------------------------------------------------------------------");

        System.out.println("Grading Criteria                   Overall Grade(A-D)              Recommend Pass");
        System.out.println("70-100\t\t\tA");
        System.out.println("60-69\t\t\tB");
        System.out.println("50-59\t\t\tC");
        System.out.println("40-49\t\t\tD");
        System.out.println("Below 40\t\tF");
        System.out.println("---------------------------------------------------------------------------------");

        scanner.close();
    }
}
