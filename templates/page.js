// const element= document.getElementById('op1');
// if(element.value=="bhopal"){
//     element.value=1;
// }
// else{
//     element.value=2;
// }
/*
const ele1= document.getElementById('op1');
element.value=1;
const ele2 =document.getElementById('op2');
element.value=2;
const ele3 =document.getElementById('op3');
element.value=3;
const ele4 =document.getElementById('op4');
element.value=4;
const ele11 =document.getElementById('op11');
element.value=11;
const ele12 =document.getElementById('op12');
element.value=12;
const ele13 =document.getElementById('op13');
element.value=13;
const ele14 =document.getElementById('op14');
element.value=14;
const ele21 =document.getElementById('op21');
element.value=21;
const ele22 =document.getElementById('op22');
element.value=22;
const ele23 =document.getElementById('op23');
element.value=23;
const ele24 =document.getElementById('op24');
element.value=24;
*/

const values = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24];

values.forEach(val => {
    const ele = document.getElementById(`op${val}`);
    if (ele) {
        ele.value = val;
    }
});
