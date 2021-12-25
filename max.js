const number1 = 103;
const number2 = 72;
const number3 = 189;

const getMax = (a, b, c) => {
    let max = a;

    if (b > max) {
        max = b;
    }
    if (c > max) {
        max = c;
    }
    return max;
};
const max = getMax(number1, number2 , number3);
console.log(`nomor maksimumnya adalah ${max}`);