package Sorting.SelectionSort;

public class selection {
    public static void main(String [] args)
    {
        int [] a = {2,3,4,5,0,6,7,8,9};
        int temp;
        int min ;
        for( int i = 0 ; i<a.length-1;i++){
            min = i;
            for(int j = i+1;j<a.length;j++){
                if (a[min] < a[j]){
                     min = j;
                }

            }
            temp = a[i];
            a[i] = a[min];
            a[min] = temp;
        
        }
    for(int i = 0; i<a.length ; i++){
        System.out.println(a[i]);
    }
    }
    
}
