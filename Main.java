package com.company;
import javax.swing.text.html.ListView;
import java.io.*;
import java.nio.Buffer;
import java.util.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;
import java.util.Random;
import java.io.BufferedReader;
import java.io.InputStreamReader;



public class Main {


    public static void main(String[] args) {
        System.out.println("Калькулятор готов ввести выражение:\n введите цифру: ");
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> numbers = new ArrayList();
        String op = "";
        int sum = 0;
        do {
            String input = sc.next();

            if (input.equals("выход")) {
                break;
            }
            String[] strings = input.split("\\W");
            String[] operator = input.split("\\w");
            try {
                for (String a:strings){
                    numbers.add(Integer.parseInt(a));
                }
                sum=numbers.get(0);
                for (int i=1;i<operator.length;i++){


                    sum=operation(sum,numbers.get(i),operator[i]);

                }
                System.out.println(sum);
            } catch (Exception e) {
                e.printStackTrace();
                System.out.println("Ошибка ввода попробуйте еще раз: ");
            }
        } while (true);
    }

    private static int operation(int a, int b, String op) {
        switch (op) {
            case "*":
                return a * b;
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "/":
                return a / b;
            default:
                return 0;
        }

    }

}
