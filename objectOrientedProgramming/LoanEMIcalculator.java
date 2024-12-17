import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;

public class LoanEMIcalculator extends JFrame {
    private JTextField loanAmountField;
    private JTextField durationField;
    private JTextField interestRateField;
    private JCheckBox earlyPaymentCheckBox;
    private JTextField monthlyPaymentField;
    private JButton calculateButton;
    private JButton exitButton;
    private JPanel mainPanel;

    public LoanEMIcalculator() {
        setTitle("LoanEMICalculator (Samuel C026-01-0736/2023)");
        setContentPane(mainPanel);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);

        calculateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                calculateEMI();
            }
        });
        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });
    }

    private void calculateEMI() {
        try {
            double loanAmount = Double.parseDouble(loanAmountField.getText());
            int duration = Integer.parseInt(durationField.getText());
            double interestRate = Double.parseDouble(interestRateField.getText()) / 12 / 100;

            double emi = (loanAmount * interestRate * Math.pow(1 + interestRate, duration)) /
                    (Math.pow(1 + interestRate, duration) - 1);

            if (earlyPaymentCheckBox.isSelected()) {
                emi *= 0.9; // Assuming 10% discount for early payment.
            }

            DecimalFormat df = new DecimalFormat("0.00");
            monthlyPaymentField.setText(df.format(emi));
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Please enter valid numbers.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new LoanEMIcalculator().setVisible(true);
            }
        });
    }
}