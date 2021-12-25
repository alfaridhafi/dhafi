class Animal{
    constructor(name, age, breed) {
        this.name = name;
        this.age = age;
        this.breed = breed;
    }
    greet() {
        console.log("hello");
    }

    info() {
        this.greet();
        console.log(`nama saya adalah ${this.name}`);
        console.log(`saya berusia ${this.age}`);
        console.log(`saya berkelamin ${this.breed}`);
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
