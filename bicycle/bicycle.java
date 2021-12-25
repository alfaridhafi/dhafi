class Bicycle {
    private String name;
    private String color;
    private int distance = 0;

    Bicycle(String name, String color){
        this.name = name;
        this.color = color;
        
    }
    public void printData(){
        System.out.println("nama" + this.name);
        System.out.println("warna" + this.color);
        System.out.println("jarak:" + this.distance + "km");
    }
    public void run(int distance) {
        System.out.println("bergerak" + distance + "km");
        this.distance += distance;
        System.out.println("jarak:" + this.distance + "km");
    }
}