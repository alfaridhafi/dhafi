class Car {
    private String name;
    private String color;
    private int distance = 0;
    private int fuel = 100;

    Bicycle(String name, String color){
        this.name = name;
        this.color = color;
        
    }
    public void printData(){
        System.out.println("nama" + this.name);
        System.out.println("warna" + this.color);
        System.out.println("jarak:" + this.distance + "km");
        System.out.println("Bahan Bakar: " + this.fuel + "L");
    }
    public void run(int distance) {
        System.out.println("bergerak" + distance + "km");
        if (distance <= this.fuel) {
            this.distance += distance;
            this.distance -= fuel;
        } else {
            Sytem.out.println("bensin tidak cukup");
        }
        System.out.println("jarak:" + this.distance + "km");
        System.outn.println("bensin tersisa" + this.fuel + "L");
    }
    public void charge(int litre) {
        System.out.println("mengisi" + litre + "liter");
        if (litre <= 0) {
            System.out.println("tidak ada bensin tersisa");
        } else if(litre + this.fuel >= 100) {
            System.out.println("minyak sudah penuh");
            this.fuel = 100;
        } else {
            this.fuel = litre;
        }
        System.out.println("Bahan Bakar:" + this.fuel + "L");
    }
}