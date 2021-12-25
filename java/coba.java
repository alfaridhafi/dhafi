class main{
    public static void main (String[] args){
        printData("dhafi alfaridzi", 18, 1.6, 50.0);
        printData("okta setiawan", 18, 1.75, 80.0)
    }
    public static void printData(String name, int age, double height, double weight){
        System.out.println("nama saya adalah" + name + ".");
        system.out.println("saya berumur" + age + ".");
        System.out.println("tinggi saya adalah" + height + ".");
        System.out.println("berat saya adalah" + weight + "kilogram.")
        double bmi = bmi(height, weight);

        System.out.println("bmi saya adalah" + bmi + ".")
    }
    public static double bmi(double height, double weight){
        return weight / height / height;
    }
}