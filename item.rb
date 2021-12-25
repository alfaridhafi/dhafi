def price_with_shipping(price1, price2)
    if price >= 50
        return price
    end

    return price + 5
end

price_with_shipping(30, 100)
puts "Total harga adalah $30"
puts "Dengan ongkos kirim, totalnya menjadi $#{price_with_shipping}"
puts "-----------"
puts "Total harga adalah $100"
puts "Dengan ongkos kirim, totalnya menjadi $#{price_with_shipping}"
