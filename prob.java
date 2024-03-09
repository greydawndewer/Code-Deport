import java.util.Arrays;

public class problem {
    int md_num;
    int door_open = 0;
    public problem(int n){
        md_num = n;
    }
    int[] doors_stat;
    public void create_doors() {
        doors_stat = new int[md_num];
        for (int i = 0; i<md_num; i++) {
            doors_stat[i] = 0;
        }
    }
    public void change_stat(){
        for (int monkey = 1; monkey<md_num+1; monkey++){

            for (int door = 0; door<md_num; door++) {
                if ((door+1)%monkey == 0) {
                    if (doors_stat[door] == 0) {
                        doors_stat[door] = 1;
                    } else {
                        doors_stat[door] = 0;
                    }
                }

            }

        }
    }
    public int count_doors_open(){

        for (int door = 0; door<md_num; door++){
            if (doors_stat[door] == 1) {
                door_open++;
            }
        }
        return door_open;
    }
    public static void main(String[] args) {
        problem x = new problem(100);
        x.create_doors();
        x.change_stat();
        System.out.println(Arrays.toString(x.doors_stat));
        System.out.println(x.count_doors_open());
    }
}
