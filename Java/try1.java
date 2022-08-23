package Java;


public class try1 {
    public static void main(String [] ag){

        String name ="Aron";
        String [] li={name,"surname"};
        print(li);
    }
    public static void  print(String [] li){
        for (int i=0 ; i<li.length;i++){
            System.out.println(li[i]);
        }
    }

}
