import java.util.Scanner;

public class Marksheet2 {
    private static final String[] UNIT_CODES = {"CCS2211", "CCS2212", "CCS2213", "CCS2214", "CCS2215"};
    private static final int NUM_STUDENTS = 5;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String[] regNos = new String[NUM_STUDENTS];
        String[] names = new String[NUM_STUDENTS];
        int[][] marks = new int[NUM_STUDENTS][UNIT_CODES.length];

        // Input student details and marks
        for (int student = 0; student < NUM_STUDENTS; student++) {
            System.out.println("Enter Student Registration Number for Student " + (student + 1) + ": ");
            regNos[student] = scanner.nextLine();

            System.out.println("Enter the Student Name for Student " + (student + 1) + ": ");
            names[student] = scanner.nextLine();

            for (int i = 0; i < UNIT_CODES.length; i++) {
                System.out.println("Enter marks for " + UNIT_CODES[i] + " for Student " + (student + 1) + ":");
                marks[student][i] = scanner.nextInt();
            }
            scanner.nextLine();
        }

        scanner.close();

        printHeader();

        // Output student data
        for (int student = 0; student < NUM_STUDENTS; student++) {
            int total = calculateTotal(marks[student]);
            double average = (double) total / UNIT_CODES.length;
            char grade = determineGrade(average);
            String status = average >= 70 ? "PASS" : "FAIL";

            printStudentRow(regNos[student], names[student], marks[student], total, average, status, grade);
        }
    }

    private static void printHeader() {
        System.out.println("Student Score Sheet");
        System.out.println("------------------------------------------------------------------------------------------------------------------");
        System.out.printf("%-15s %-20s %-10s %-10s %-10s %-10s %-10s %-6s %-8s %-7s %-5s%n",
                "Reg no.", "Full Name", "CCS2211", "CCS2212", "CCS2213", "CCS2214", "CCS2215", "TOTAL", "AVERAGE", "STATUS", "GRADE");
        System.out.println("------------------------------------------------------------------------------------------------------------------");
    }

    private static void printStudentRow(String regNo, String name, int[] marks, int total, double average, String status, char grade) {
        System.out.printf("%-15s %-20s %-10d %-10d %-10d %-10d %-10d %-6d %-8.1f %-7s %-5s%n",
                regNo, name, marks[0], marks[1], marks[2], marks[3], marks[4], total, average, status, grade);
    }

    private static int calculateTotal(int[] marks) {
        int total = 0;
        for (int mark : marks) {
            total += mark;
        }
        return total;
    }

    private static char determineGrade(double average) {
        if (average >= 70) return 'A';
        else if (average >= 60) return 'B';
        else if (average >= 50) return 'C';
        else if (average >= 40) return 'D';
        else return 'F';
    }
}


