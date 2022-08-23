public class pivot {
    public static void main (String a []){
        int [] arr={1,2,3,5,6,4,3,2};
        int pivot;
        int ans=-1;
        int target=0;
        int start=0;
        int end=arr.length-1;
        pivot=pivotElement(arr);
        System.out.println("Pivot is "+pivot);
        System.out.println("True pivot is "+abspivotElement(arr));
        // System.out.println(arr[end-1]);
        // if(arr[pivot]<=target && target<=arr[end])
        // {
        //     int mid=pivot-(pivot-end)/2;
        //     ans = search(arr, target, pivot, mid, end);


        // }
        // else{
        //     int mid=start-(pivot-end)/2;
        //     ans = search(arr,target,start,mid,pivot);
        // }
        // System.out.println("Answer is "+ans);

    }

    static int  pivotElement(int[] arr){
       

        int low=0;
        int high =arr.length-1;
        int mid = low-(low-high)/2;
        while(low<high){
           
            
        if( arr[0]<=arr[mid]){
            System.out.println("less than m "+arr[mid]);
            
                low = mid+1;
            }
            else{
                System.out.println("more than m "+arr[mid]);
                high = mid;
            }
            mid = low -(low-high)/2;
        }

        return low;
    }
    static int abspivotElement(int [] arr){
        int low=0;
        int high =arr.length-1;
        int mid = low-(low-high)/2;
        while (low<=high){
        if (arr[mid]<arr[mid+1]){
            low = mid+1;
        }
        else{
            high =mid-1;
        }
        mid = low-(low-high)/2;
        }
        return arr[mid];

    }
    
}
