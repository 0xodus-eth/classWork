function xor(a, b) {
    return a ^ b;
}

// Example usage:
const result = xor(5, 3); 
console.log(result); // Output: 6

function xor(...args) {
    return args.reduce((acc, curr) => acc ^ curr, 0);
}
console.log(xor(5, 3)); // Output: 6
console.log(xor(5, 3, 7)); // Output: 5 (since 5 ^ 3 ^ 7 = 5)
