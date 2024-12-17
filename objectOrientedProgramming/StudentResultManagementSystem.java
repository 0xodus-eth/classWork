import javax.swing.*;
import javax.swing.border.TitledBorder;
import javax.swing.table.DefaultTableModel;
import java.awt.*;

public class StudentResultManagementSystem {
    public static void main(String[] args) {
        // Frame setup
        JFrame mainFrame = new JFrame("Student Result System");
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.setSize(1000, 600);
        mainFrame.setLayout(null);

        // Panel for student records
        JPanel studentPanel = new JPanel();
        studentPanel.setBounds(10, 10, 600, 350);
        studentPanel.setLayout(null);
        studentPanel.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(Color.BLACK, 1), "Student Records",
                TitledBorder.LEFT, TitledBorder.TOP, new Font("Arial", Font.BOLD, 14), Color.BLACK
        ));

        // Personal Info Fields
        JTextField idField = new JTextField();
        JTextField firstNameField = new JTextField();
        JTextField lastNameField = new JTextField();
        JComboBox<String> courseComboBox = new JComboBox<>(new String[]{"CS", "BIT", "BBIT"});
        JTextField totalScoreField = new JTextField();
        JTextField avgField = new JTextField();
        JTextField rankField = new JTextField();

        String[] labels = {"Student_ID:", "Firstname:", "Surname:", "Course Code:", "Total Score:", "Average:", "Ranking:"};
        JTextField[] textFields = {idField, firstNameField, lastNameField, totalScoreField, avgField, rankField};
        int verticalPos = 30;

        // Adding personal info fields dynamically
        for (int i = 0; i < labels.length; i++) {
            JLabel label = new JLabel(labels[i]);
            label.setBounds(20, verticalPos, 100, 25);
            studentPanel.add(label);

            if (i == 3) { // Course combo box
                courseComboBox.setBounds(130, verticalPos, 120, 25);
                studentPanel.add(courseComboBox);
                JSeparator separator = new JSeparator();
                separator.setBounds(20, verticalPos + 30, 230, 1);
                studentPanel.add(separator);
            } else {
                textFields[i < 3 ? i : i - 1].setBounds(130, verticalPos, 120, 25);
                studentPanel.add(textFields[i < 3 ? i : i - 1]);
            }

            verticalPos += 40;
        }

        // Subject Info Fields
        JTextField maths = new JTextField();
        JTextField english = new JTextField();
        JTextField biology = new JTextField();
        JTextField computing = new JTextField();
        JTextField chemistry = new JTextField();
        JTextField physics = new JTextField();
        JTextField addMaths = new JTextField();
        JTextField business = new JTextField();

        String[] subjectLabels = {"Maths:", "English:", "Biology:", "Computing:", "Chemistry:", "Physics:", "Add Maths:", "Business:"};
        JTextField[] subjectFields = {maths, english, biology, computing, chemistry, physics, addMaths, business};

        verticalPos = 30;

        // Adding subject fields
        for (int i = 0; i < subjectLabels.length; i++) {
            JLabel label = new JLabel(subjectLabels[i]);
            label.setBounds(270, verticalPos, 100, 25);
            studentPanel.add(label);

            subjectFields[i].setBounds(380, verticalPos, 120, 25);
            studentPanel.add(subjectFields[i]);

            verticalPos += 40;
        }

        mainFrame.add(studentPanel);

        // Panel for grades
        JPanel gradePanel = new JPanel();
        gradePanel.setBounds(620, 10, 350, 350);
        gradePanel.setLayout(null);
        gradePanel.setBorder(BorderFactory.createTitledBorder(
                BorderFactory.createLineBorder(Color.BLACK, 1), "Grades",
                TitledBorder.LEFT, TitledBorder.TOP, new Font("Arial", Font.BOLD, 14), Color.BLACK
        ));

        JTextArea gradeSummary = new JTextArea();
        JScrollPane gradeScroll = new JScrollPane(gradeSummary);
        gradeScroll.setBounds(20, 30, 300, 290);
        gradePanel.add(gradeScroll);

        mainFrame.add(gradePanel);

        // Table for displaying student results
        JTable studentTable = new JTable(new DefaultTableModel(new Object[][]{}, new Object[]{
                "Student_ID", "Course_Code", "Maths", "English", "Biology", "Computing", "Chemistry", "Physics", "Add Maths", "Business",
                "Total_Score", "Average", "Ranking"
        }));
        JScrollPane tableScroll = new JScrollPane(studentTable);
        tableScroll.setBounds(10, 370, 970, 100);
        mainFrame.add(tableScroll);

        // Buttons
        JButton rankButton = new JButton("Ranking");
        JButton transcriptButton = new JButton("Transcript");
        JButton deleteButton = new JButton("Delete");
        JButton resetButton = new JButton("Reset");
        JButton exitButton = new JButton("Exit");

        rankButton.setBounds(150, 480, 100, 30);
        transcriptButton.setBounds(270, 480, 100, 30);
        deleteButton.setBounds(390, 480, 100, 30);
        resetButton.setBounds(510, 480, 100, 30);
        exitButton.setBounds(630, 480, 100, 30);

        mainFrame.add(rankButton);
        mainFrame.add(transcriptButton);
        mainFrame.add(deleteButton);
        mainFrame.add(resetButton);
        mainFrame.add(exitButton);

        // Action Listeners
        rankButton.addActionListener(e -> {
            try {
                int mathsScore = Integer.parseInt(maths.getText());
                int englishScore = Integer.parseInt(english.getText());
                int biologyScore = Integer.parseInt(biology.getText());
                int computingScore = Integer.parseInt(computing.getText());
                int chemistryScore = Integer.parseInt(chemistry.getText());
                int physicsScore = Integer.parseInt(physics.getText());
                int addMathsScore = Integer.parseInt(addMaths.getText());
                int businessScore = Integer.parseInt(business.getText());

                int total = mathsScore + englishScore + biologyScore + computingScore + chemistryScore + physicsScore + addMathsScore + businessScore;
                double avg = total / 8.0;
                String grade;

                if (avg >= 70) grade = "A";
                else if (avg >= 60) grade = "B";
                else if (avg >= 50) grade = "C";
                else if (avg >= 40) grade = "D";
                else grade = "F";

                totalScoreField.setText(String.valueOf(total));
                avgField.setText(String.format("%.2f", avg));
                rankField.setText(grade);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(mainFrame, "Please enter valid numeric values for all subjects.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        transcriptButton.addActionListener(e -> {
            try {
                String studentID = idField.getText();
                String firstName = firstNameField.getText();
                String surname = lastNameField.getText();
                String courseCode = (String) courseComboBox.getSelectedItem();
                int totalScore = Integer.parseInt(totalScoreField.getText());
                double avg = Double.parseDouble(avgField.getText());
                String rank = rankField.getText();

                int mathsScore = Integer.parseInt(maths.getText());
                int englishScore = Integer.parseInt(english.getText());
                int biologyScore = Integer.parseInt(biology.getText());
                int computingScore = Integer.parseInt(computing.getText());
                int chemistryScore = Integer.parseInt(chemistry.getText());
                int physicsScore = Integer.parseInt(physics.getText());
                int addMathsScore = Integer.parseInt(addMaths.getText());
                int businessScore = Integer.parseInt(business.getText());

                Object[] rowData = {studentID, courseCode, mathsScore, englishScore, biologyScore, computingScore,
                        chemistryScore, physicsScore, addMathsScore, businessScore, totalScore, avg, rank};

                DefaultTableModel model = (DefaultTableModel) studentTable.getModel();
                model.addRow(rowData);
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(mainFrame, "Please fill all fields correctly.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        });

        resetButton.addActionListener(e -> {
            idField.setText("");
            firstNameField.setText("");
            lastNameField.setText("");
            totalScoreField.setText("");
            avgField.setText("");
            rankField.setText("");
            for (JTextField field : new JTextField[]{maths, english, biology, computing, chemistry, physics, addMaths, business}) {
                field.setText("");
            }
            gradeSummary.setText("");
        });

        exitButton.addActionListener(e -> System.exit(0));

        mainFrame.setVisible(true);
    }
}