public class bookAllocation {
    public static void main(String [] A){
        int [] books ={10,20,30,40,50};
        int no_of_student = 2;
        //modularizing  code 
        int answer = 0;
        answer = binaryAllocator(books,no_of_student);
        System.out.println(answer);
        
    }
     static int binaryAllocator(int [] books,int no_of_student){
        int ans=0;
        int low,high,mid;
    
        low = books[books.length-1];
        high =0;

        for (int i =0 ;i<books.length;i++){
                high+=books[i];
        }
        mid = low-(low-high)/2;

        while(low<=high){

       
            
            
            if (canAllocate(books,mid,no_of_student)){
                
          
                high = mid -1;
                ans = mid;
                


            }
            else{
                low = mid +1;
            }
            mid = low-(low-high)/2;
            
        }
        return ans;
    }
    static  boolean canAllocate(int [] books,int mid,int n){
        int sum=0 ;
        int noStd=1;
        for(int i=0;i<books.length;i++){
            if(mid < books[i]){
                return false;
            }
            if (sum+books[i]>mid){
                noStd+=1;
                sum=books[i];
                if(noStd>n){
                    return false;
                }
            }

            else{
                sum+=books[i];
            }
        }
        return true;

    }
    
}
