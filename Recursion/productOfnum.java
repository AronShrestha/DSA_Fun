package Recursion;

public class productOfnum {
    public static void main (String a[]){
        int n =155;
        System.out.println(product(n));
    }
    public static int product(int n){
        if (n%10==n){
            return n;
        }
        else{
            int rem = n%10;
            return rem *product(n/10);
        }

    }
    
}
