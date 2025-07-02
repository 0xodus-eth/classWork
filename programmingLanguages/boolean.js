function booleanOperations(a, b) {
    // AND operator (&&)
    const andResult = a && b;
    console.log(`${a} && ${b} = ${andResult}`);

    // OR operator (||)
    const orResult = a || b;
    console.log(`${a} || ${b} = ${orResult}`);

    // NOT operator (!)
    const notA = !a;
    const notB = !b;
    console.log(`!${a} = ${notA}`);
    console.log(`!${b} = ${notB}`);

    // Equality operator (===)
    const equalityResult = a === b;
    console.log(`${a} === ${b} = ${equalityResult}`);
}


booleanOperations(true, false);
booleanOperations(1, 0);
booleanOperations('hello', 'hello');
booleanOperations(null, undefined);