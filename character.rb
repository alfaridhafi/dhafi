characters = [
    {name: "Ninja Ken", age: 14},
    {name: "Guru Domba"},
    {name: "Baby Ben", age: 5},
    {name: "Birdie"}
]

characters.each do|character|
    puts "-------------------"
    puts "nama saya adalah #{character[:name]}"
 

if character[:age]
    puts "umur saya adalah #{character[:age]}"
else 
    puts "umur saya rahasia"
end
end