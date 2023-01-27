function fizzBuzz(n) {
    // Step 1: Iterate from 1 to n
    for (let i = 1; i <= n; i++) {
        // Create a result variable:
        let result = "";
        // Check conditions and build result:
        if (i % 3 === 0) result += "fizz";
        if (i % 5 === 0) result += "buzz";
        console.log(result || i);
    }
}