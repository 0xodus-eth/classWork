
function modifyValue(num) {
    num = num * 2;
    console.log("Inside modifyValue, num:", num);
}

function modifyObject(obj) {
    obj.value = obj.value * 2;
    console.log("Inside modifyObject, obj.value:", obj.value);
}

// Main code
let number = 10;
let myObject = { value: 10 };

console.log("Before modifyValue, number:", number);
modifyValue(number);
console.log("After modifyValue, number:", number);

console.log("Before modifyObject, myObject.value:", myObject.value);
modifyObject(myObject);
console.log("After modifyObject, myObject.value:", myObject.value);