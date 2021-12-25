const characters = [
    {name: "Ninja Ken", age: 14},
    {name: "Guru Domba", age: 100},
    {name: "Baby Ninja Ben", age: 5},
    {name: "Birdie"}
];

for (let i = 0; i < characters.length; i++){
    console.log("--------------------");

    const character = characters[i];
    console.log(`nama saya adalah ${character.name}`);

    if(age === undefined){
        console.log("umur saya rahasia!");
    } else {
        console.log(`umur saya ${character.age}`);
    }
}