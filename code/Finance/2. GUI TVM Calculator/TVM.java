import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class TVM extends JFrame implements ActionListener {
    private JTextField display;
    private JButton[] numberButtons;
    private JButton addButton, subtractButton, multiplyButton, divideButton, equalsButton, clearButton;
    private JButton nButton, iYButton, pvButton, pmtButton, fvButton;
    private JButton percentButton, sqrtButton, squareButton, reciprocalButton, cubeButton, openParenthesisButton, closeParenthesisButton, powerButton, lnButton, stoButton, rclButton, decimalButton, plusMinusButton;
    private double num1, num2, result;
    private char operator;
    private double n, iY, pv, pmt, fv;
    private char tvmOperator;
    private final Color baseColor = new Color(255, 255, 230);
    private final Color operationColor = new Color(255, 230, 128);

    public TVM() {
        setTitle("GUI Calculator");
        setSize(450, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container container = getContentPane();
        container.setLayout(new BorderLayout());

        display = new JTextField();
        display.setFont(new Font("Arial", Font.PLAIN, 24));
        container.add(display, BorderLayout.NORTH);

        JPanel buttonPanel = new JPanel();
        buttonPanel.setLayout(new GridLayout(7, 5, 5, 5));

        numberButtons = new JButton[10];
        for (int i = 0; i < 10; i++) {
            numberButtons[i] = new JButton(String.valueOf(i));
            numberButtons[i].setFont(new Font("Arial", Font.BOLD, 18));
            numberButtons[i].setBackground(Color.LIGHT_GRAY);
            numberButtons[i].addActionListener(this);
        }

        addButton = createOperationButton("+", operationColor);
        subtractButton = createOperationButton("-", operationColor);
        multiplyButton = createOperationButton("*", operationColor);
        divideButton = createOperationButton("/", operationColor);
        equalsButton = createOperationButton("=", operationColor);
        clearButton = createOperationButton("C", operationColor);

        nButton = createOperationButton("N", baseColor);
        iYButton = createOperationButton("I/Y", baseColor);
        pvButton = createOperationButton("PV", baseColor);
        pmtButton = createOperationButton("PMT", baseColor);
        fvButton = createOperationButton("FV", baseColor);

        percentButton = createOperationButton("%", baseColor);
        sqrtButton = createOperationButton("√x", baseColor);
        squareButton = createOperationButton("x^2", baseColor);
        reciprocalButton = createOperationButton("1/x", baseColor);
        cubeButton = createOperationButton("x^3", baseColor);
        openParenthesisButton = createOperationButton("(", baseColor);
        closeParenthesisButton = createOperationButton(")", baseColor);
        powerButton = createOperationButton("y^x", baseColor);
        lnButton = createOperationButton("ln", baseColor);
        stoButton = createOperationButton("STO", baseColor);
        rclButton = createOperationButton("RCL", baseColor);
        decimalButton = createOperationButton(".", baseColor);
        plusMinusButton = createOperationButton("+/-", baseColor);

        buttonPanel.add(nButton);
        buttonPanel.add(iYButton);
        buttonPanel.add(pvButton);
        buttonPanel.add(pmtButton);
        buttonPanel.add(fvButton);
        buttonPanel.add(percentButton);
        buttonPanel.add(sqrtButton);
        buttonPanel.add(squareButton);
        buttonPanel.add(reciprocalButton);
        buttonPanel.add(divideButton);
        buttonPanel.add(cubeButton);
        buttonPanel.add(openParenthesisButton);
        buttonPanel.add(closeParenthesisButton);
        buttonPanel.add(powerButton);
        buttonPanel.add(multiplyButton);
        buttonPanel.add(lnButton);
        buttonPanel.add(numberButtons[7]);
        buttonPanel.add(numberButtons[8]);
        buttonPanel.add(numberButtons[9]);
        buttonPanel.add(subtractButton);
        buttonPanel.add(stoButton);
        buttonPanel.add(numberButtons[4]);
        buttonPanel.add(numberButtons[5]);
        buttonPanel.add(numberButtons[6]);
        buttonPanel.add(addButton);
        buttonPanel.add(rclButton);
        buttonPanel.add(numberButtons[1]);
        buttonPanel.add(numberButtons[2]);
        buttonPanel.add(numberButtons[3]);
        buttonPanel.add(equalsButton);
        buttonPanel.add(clearButton);
        buttonPanel.add(numberButtons[0]);
        buttonPanel.add(decimalButton);
        buttonPanel.add(plusMinusButton);

        container.add(buttonPanel, BorderLayout.CENTER);

        setVisible(true);
    }

    private JButton createOperationButton(String text, Color color) {
        JButton button = new JButton(text);
        button.addActionListener(this);
        button.setBackground(color);
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
                        case '^' -> result = Math.pow(num1, num2);
                    }
        
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == clearButton) {
                    display.setText("");
                }
        
                if (e.getSource() == nButton || e.getSource() == iYButton || e.getSource() == pvButton ||
                        e.getSource() == pmtButton || e.getSource() == fvButton) {
                    tvmOperator = ((JButton) e.getSource()).getText().charAt(0);
                    num1 = Double.parseDouble(display.getText());
                    display.setText("");
                }

                if (e.getSource() == percentButton) {
                    num1 = Double.parseDouble(display.getText());
                    num2 = Double.parseDouble(display.getText());
                    result = num1 % num2;
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == sqrtButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = Math.sqrt(num1);
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == squareButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = Math.pow(num1, 2);
                    display.setText(formatResult(result));
                }

                if (e.getSource() == reciprocalButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = 1 / num1;
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == cubeButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = Math.pow(num1, 3);
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == powerButton) {
                    num1 = Double.parseDouble(display.getText());
                    operator = '^';
                    display.setText("");
                }
        
                if (e.getSource() == lnButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = Math.log(num1);
                    display.setText(formatResult(result));
                }
        
                if (e.getSource() == decimalButton) {
                    if (!display.getText().contains(".")) {
                        display.setText(display.getText() + ".");
                    }
                }
        
                if (e.getSource() == plusMinusButton) {
                    num1 = Double.parseDouble(display.getText());
                    result = num1 * (-1);
                    display.setText(String.valueOf(result));
                }
        
                if (tvmOperator != 0 && !display.getText().isEmpty()) {
                    double num2 = Double.parseDouble(display.getText());
                    switch (tvmOperator) {
                        case 'N' -> n = num2;
                        case 'I' -> iY = num2;
                        case 'P' -> pv = num2;
                        case 'M' -> pmt = num2;
                        case 'F' -> fv = num2;
                    }
                    tvmOperator = 0;
                }
            }

            private String formatResult(double result) {
                if (result == Math.floor(result)) {
                    return String.valueOf((int) result);
                } else {
                    return String.valueOf(result);
                }
            }

            private void handleKeyEvent(KeyEvent e) {
                char keyChar = e.getKeyChar();
        
                if (Character.isDigit(keyChar)) {
                    display.setText(display.getText() + keyChar);
                } else if (keyChar == '+' || keyChar == '-' || keyChar == '*' || keyChar == '/') {
                    num1 = Double.parseDouble(display.getText());
                    operator = keyChar;
                    display.setText("");
                } else if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    actionPerformed(new ActionEvent(equalsButton, ActionEvent.ACTION_PERFORMED, ""));
                } else if (e.getKeyCode() == KeyEvent.VK_BACK_SPACE) {
                    String text = display.getText();
                    if (!text.isEmpty()) {
                        display.setText(text.substring(0, text.length() - 1));
                    }
                }
            }
        
            public static void main(String[] args) {
                new TVM();
            }
        }
        