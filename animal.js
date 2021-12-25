class Animal{
    constructor(name, age, breed) {
        this.name = name;
        this.age = age;
        this.breed = breed;
    }
    greet() {
        console.log("hallo");
    }
    info() {
        this.greet();
        console.log(`halo nama saya ${this.name}`);
        console.log(`saya berusia ${this.age} tahun`);
        console.log(`jenis kelamin saya adalah ${this.breed}`);
    }
}
class Dog extends Animal {
    getHumanAge() {
        return this.age * 7;
    }
}
const dog = new Dog("leo", 4, "lakik");
dog.info();
const humanAge = dog.getHumanAge();
console.log(`dalam ukuran manusia saya berumur ${humanAge}`);
    