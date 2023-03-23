import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GUICalculator extends JFrame implements ActionListener {
    private JTextField display;
    private JButton[] numberButtons;
    private JButton addButton, subtractButton, multiplyButton, divideButton, equalsButton, clearButton;
    private double num1, num2, result;
    private char operator;

    public GUICalculator() {
        setTitle("GUI Calculator");
        setSize(350, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container container = getContentPane();
        container.setLayout(new BorderLayout());

        display = new JTextField();
        display.setFont(new Font("Arial", Font.PLAIN, 24));
        container.add(display, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(4, 4, 5, 5));

        numberButtons = new JButton[10];
        for (int i = 0; i < 10; i++) {
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].setFont(new Font("Arial", Font.BOLD, 18));
            numberButtons[i].setBackground(Color.LIGHT_GRAY);
            numberButtons[i].addActionListener(this);
        }

        addButton = createOperationButton("+");
        subtractButton = createOperationButton("-");
        multiplyButton = createOperationButton("*");
        divideButton = createOperationButton("/");
        equalsButton = createOperationButton("=");
        clearButton = createOperationButton("C");

        buttonPanel.add(numberButtons[7]);
        buttonPanel.add(numberButtons[8]);
        buttonPanel.add(numberButtons[9]);
        buttonPanel.add(divideButton);
        buttonPanel.add(numberButtons[4]);
        buttonPanel.add(numberButtons[5]);
        buttonPanel.add(numberButtons[6]);
        buttonPanel.add(multiplyButton);
        buttonPanel.add(numberButtons[1]);
        buttonPanel.add(numberButtons[2]);
        buttonPanel.add(numberButtons[3]);
        buttonPanel.add(subtractButton);
        buttonPanel.add(numberButtons[0]);
        buttonPanel.add(clearButton);
        buttonPanel.add(equalsButton);
        buttonPanel.add(addButton);

        container.add(buttonPanel, BorderLayout.CENTER);

        setVisible(true);
    }

    private JButton createOperationButton(String text) {
        JButton button = new JButton(text);
        button.setFont(new Font("Arial", Font.BOLD, 18));
        button.setBackground(Color.ORANGE);
        button.addActionListener(this);
        return button;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 10; i++) {
            if (e.getSource() == numberButtons[i]) {
                display.setText(display.getText() + i);
            }
        }

        if (e.getSource() == addButton || e.getSource() == subtractButton ||
                e.getSource() == multiplyButton || e.getSource() == divideButton) {
            num1 = Double.parseDouble(display.getText());
            operator = ((JButton) e.getSource()).getText().charAt(0);
            display.setText("");
        }

        if (e.getSource() == equalsButton) {
            num2 = Double.parseDouble(display.getText());

            switch (operator) {
                case '+' -> result = num1 + num2;
                case '-' -> result = num1 - num2;
                case '*' -> result = num1 * num2;
                case '/' -> result = num1 / num2;
            }

            if (result % 1 == 0) {
                display.setText(String.valueOf((int) result));
            } else {
                display.setText(String.valueOf(result));
            }
        }

        if (e.getSource() == clearButton) {
            display.setText("");
        }
    }

    public static void main(String[] args) {
        new GUICalculator();
    }
}
