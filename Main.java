package com.company;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.Random;
import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;



public class Main {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int num1 = getInt();
        char operation = getOperation();    
        int num2 = getInt();
        char get =get2();
        int num3 = getInt();

        int result = calc(num1,num2,num3,operation);
        System.out.println("Результат операции: "+result);
    }

    public static int getInt(){
        System.out.println("Введите число:");
        int num;
        if(scanner.hasNextInt()){
            num = scanner.nextInt();
        } else {
            System.out.println("Вы допустили ошибку при вводе числа. Попробуйте еще раз.");
            scanner.next();//рекурсия
            num = getInt();
        }
        return num;
    }

    public static char getOperation(){
        System.out.println("Введите операцию:");
        char operation;
        if(scanner.hasNext()){
            operation = scanner.next().charAt(0);
        } else {
            System.out.println("Вы допустили ошибку при вводе операции. Попробуйте еще раз.");
            scanner.next();
            operation = getOperation();
        }
        return operation;
    }
    public static char get2(){
        System.out.println("Введите операцию:");
        char get;
        if (scanner.hasNext()){
            get = scanner.next().charAt(0);
        }else {
            System.out.println("Вы допустили ошибку при вводе операции. Попробуйте еще раз.");
            scanner.hasNext();
            get =get2();
        }
        return get;
    }
    public static int calc(int num1, int num2,int num3, char operation){
        int result;
        switch (operation){
            case '+':
                result = num1+num2-num3;
                break;
            case '-':
                result = num1-num2+num3;
                break;
            case '*':
                result = num1*num2/num3;
                break;
            case '/':
                result = num1/num2*num3;
                break;
            default:
                System.out.println("Операция не распознана. Повторите ввод.");
                result = calc(num1, num2,num3, getOperation());
        }
        return result;
    }

}


