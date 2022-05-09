public class ASum {
  
  public static long findNb(long m) {
    long n = 0;
    while (m>0)
    {
        m -= (n+1)*(n+1)*(n+1);
        if(m<0) return -1;
        n++;
    }
    return n;
  }
  
}