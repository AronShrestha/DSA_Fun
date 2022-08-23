public class Bs {
     public static void main (String [] a){
            int [] li ={1,2,3,4,5,6,7,8};
            int target=5;
            System.out.println(search(li,target,0,(li.length-1)/2,li.length-1));
    }
     static int search(int [] li,int target,int start,int mid,int end){

    
           if (end>=start) {
    
                if(target==li[mid]){
                    System.out.println("here");
                    return mid;
            }
            
                if(li[mid]<target){
                    start = mid +1;
                    mid = start-(start-end)/2;
                    return search(li,target,start,mid,end);
                }
                if (li[mid]>target){
                    end = mid-1;
                    mid = start-(start-end)/2;
                    return search(li,target,start,mid,end);

                }
            
        }

        
        
        
        return -1;
        

    }
}
