const printKen = () => {
    console.log("ninja ken");
}

const call = (callback) => {
    console.log("function baru dipanggil");
    callback;
}

call(printKen);

call (() => {
    console.log("guru domba");
});