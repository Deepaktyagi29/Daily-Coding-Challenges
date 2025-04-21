public class UniqueNumberI {
    public int findUnique(int[] arr) {
        int result = 0;
        for (int num : arr) {
            result ^= num;
        }
        return result;
    }

    public static void main(String[] args) {
        UniqueNumberI obj = new UniqueNumberI();
        int[] arr = {2, 3, 5, 4, 5, 3, 4};
        System.out.println(obj.findUnique(arr)); // Output: 2
    }
}
