package Recursion;

public class hanoi {
    public static void TOH(int n,String S,String H,String D){
        if(n == 1 ){
            System.out.println("Move disk "+n+" from " +S+" to "+D);

        }
        else{
            TOH(n-1,S,D,H);
            System.out.println("Move disk "+n+" from " +S+" to "+D);
            TOH(n-1,H,S,D);

        }

    }
    public static void main(String [] args){
        int number = 3;

        TOH(number,"S","H","D");


    }
    
}
