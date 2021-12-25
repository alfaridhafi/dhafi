const cafe = {
    name: "dhafi cafe",
    businessHours: {
        opening: "10.00",
        closing: "20.00"
    },
    menu = ["ayam goreng", "es teh", "jus jeruk", "nasi goreng"]
};

console.log(`nama cafe ini adalah ${cafe.name}`);
console.log(`cafe ini dibuka pada jam ${cafe.businessHours.opening} dan tutup pada jam ${cafe.businessHours.closing}`);
console.log(`----------------------------`);
console.log("menu rekomendasi");

for (let i = 0; i < cafe.menu.length; i ++){
    console.log(cafe.menu[i]);
}