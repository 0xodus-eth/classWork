import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class addingMarksGUI extends JFrame {

    private JTextField TextFieldName;
    private JTextField TextFieldRegNo;
    private JTextField textFieldCCS2211;
    private JTextField textFieldCCS2212;
    private JTextField textFieldCCS2213;
    private JTextField textFieldGrade;
    private JTextField textFieldTotal;
    private JTextField textFieldAverage;
    private JButton calculateButton;
    private JPanel addingMarksGUI;

    public addingMarksGUI(){
        setTitle("Adding Marks GUI");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(500,500);
        setLocationRelativeTo(null);
        setVisible(true);
        setContentPane(addingMarksGUI);

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

               try {
                   int score2211, score2212, score2213, tot;
                   double avg;
                   // Parse the scores from text fields
                   score2211 = Integer.parseInt(textFieldCCS2211.getText());
                   score2212 = Integer.parseInt(textFieldCCS2212.getText());
                   score2213 = Integer.parseInt(textFieldCCS2213.getText());

                   // Check if the score are within the valid range (0-100)
                   if (score2211 < 0 || score2211 > 100 || score2212 < 0 || score2212 > 100 || score2213 < 0 || score2213 > 100) {
                       JOptionPane.showMessageDialog(null, "Error: Marks must be between 0 and 100", "Invalid Input", JOptionPane.ERROR_MESSAGE);
                       return;
                   }
                   tot = score2211 + score2212 + score2213;
                   textFieldTotal.setText(String.valueOf(tot));
                   avg = tot / 3.0;
                   textFieldAverage.setText(String.valueOf(avg));
                   // Determne the grade based on the average
                   if(avg >= 70 ){
                       textFieldGrade.setText("A");
                   } else if (avg >= 60){
                       textFieldGrade.setText("B");
                   } else if (avg >= 50){
                       textFieldGrade.setText("C");
                   } else if (avg >= 40){
                       textFieldGrade.setText("D");
                   } else {
                       textFieldGrade.setText("F");
                   }
               } catch (NumberFormatException e1) {
                   // Handle invalid number input (non-integer values)
                   JOptionPane.showMessageDialog(null, "Error: Please enter valid numbers for marks", "Invalid Input", JOptionPane.ERROR_MESSAGE);
               }



            }
        });
    }
    public static void main(String[] args) {
        new addingMarksGUI();
        //Save the app
    }
}
