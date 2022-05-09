public class BouncingBall {
  
  public static int bouncingBall(double h, double bounce, double window) {
    if(h <= 0.0f|| window <= 0.0f || window >= h || bounce <= 0.0f || bounce >= 1.0f) return -1;
    int counter = 1;
    double heightAfterBounce = h;
    while(heightAfterBounce > window)
    {
      heightAfterBounce *= bounce;
      if(heightAfterBounce > window) counter += 2;
    }
      return counter;
  }
}