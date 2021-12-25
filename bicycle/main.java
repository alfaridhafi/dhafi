Scanner scanner = new Scanner(System.in);
class bicycle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Bicycle bicycle = new Bicycle("polygon", "hijau");
        System.out.println("selamat datang");
        bicycle.printData();
        System.out.println("-----------------");
        System.out.print("Masukkan jarak yang akan ditempuh: ");
        int bicycleDistance = scanner.nextInt();
        bicycle.run(bicycleDistance);
        System.out.println("-----------------");
        Car car = new Car("ferari", "red");
        System.out.println("selamat datang");
        car.printData();
        System.out.println("-----------------");
        System.out.print("Masukkan jarak yang akan ditempuh: ");
        int carDistance = scanner.nextInt();
        car.run(carDistance);
        System.out.println("-----------------");
        System.out.print("Masukkan jumlah isi ulang bahan bakar: ");
        int litre = scanner.nextInt();
        car.charge(litre);
    }
}