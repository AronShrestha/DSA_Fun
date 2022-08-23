public class firstandlast {
    public static void main (String [] a){
        int target;
        target = 8;
        int [] li ={1,2,3,4,4,4,4,5,6,7,7,8,8,8,8,8,8};
        System.out.println(1/2);
        int first,last;
        first = getFirst(li,target);
        last = getLast(li, target);
        System.out.println("Occured at :"+first+ " and last at :"+last);
        System.out.println("Number of occurance is "+(last-first+1));

    }
    static int getFirst(int [] li,int t)
    {
        System.out.println("@1st");
        int l,h,m,ans;
        l=0;
        ans=-1;
        h = li.length -1;
        m = l-(l-h)/2;
        while (l<=h){
            if(t==li[m]){
                    ans = m;
                    h= m-1;
            }
            else if (li[m]<t){
                l= m+1;
            }
            else{
                h = m -1;
            }
            m = l-(l-h)/2;
        }
        return ans;
    }
    static int getLast(int [] li,int t)
    {
        System.out.println("@nds");

        int l,h,m,ans;
        l=0;
        ans=-1;
        h = li.length -1;
        m = l-(l-h)/2;
        while (l<=h){
            if(t==li[m]){
                    ans = m;
                    l= m+1;
            }
            else if (li[m]<t){
                l= m+1;
            }
            else{
                h = m -1;
            }
            m = l-(l-h)/2;
        }
        return ans;
    }

    
}
