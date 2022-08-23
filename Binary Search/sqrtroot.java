public class sqrtroot {
    public static void main(String [] a){
        int number =256;
        int an=sqrt(number);
        System.out.println(an);
        double ans =precision(3,an,number);
        System.out.println("Ans is "+ans);

    }
    static int sqrt(int number){
        int s,e,m,ans;
        s=0;
        e=number;
        ans=-1;
        m=s-(s-e)/2;
        while(s<=e){
            if (m*m==number){
                return m;
            }
            else if(m*m>number){
                e=m-1;
            }
            else if(m*m<number){
                ans=m;
                s=m+1;
            }
            m=s-(s-e)/2;


        }
        return ans;
    }
    static double precision(int prec,int temp,int n){
        double ans=temp;
        double factor =1.0;
        for (int i=0 ;i<prec;i++){
            factor=factor/10;
            for(double j=ans;j*j<n;j=j+factor){
                ans=j;
                System.out.println(j*j);
            }

        }
        return ans;
    }
    
}
