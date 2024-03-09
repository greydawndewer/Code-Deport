import java.util.Random;
import java.text.DecimalFormat;

public class m {
    private static final DecimalFormat df = new DecimalFormat("0.00000");
    public String calc(int n){
        double pi;
        Random rand = new Random();
        double x;
        double y;
        double z;
        double cir = 0;
        double squ = 0;
        for (int i = 0; i < n; i++) {
            x = rand.nextDouble();
            y = rand.nextDouble();
            z = (x*x) + (y*y);
            if (z < 1) {
                cir++;
            }
            squ++;
        }
        pi = (4 * cir)/squ;
        return df.format(pi);
    }
    public static void main(String[] args) {
        m eng = new m();
        double c = 0;
        String pi = "3.14159";
        String ans = "";
        ans = eng.calc(1000000);
        while (!ans.equals(pi)) {
            c++;
            ans = eng.calc(1000000);
            System.out.println(ans);
        }
        System.out.println("Pi is " + ans + " with " + c + " attempts.");
    }
}
