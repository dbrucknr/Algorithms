function fizzBuzzSimple(n) {
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

const fizzBuzzConditional = n =>
    Array
        .from({ length: n }, (_, i) => i + 1)
        .forEach((value) => {
            const multipleOfThree = value % 3 === 0;
            const multipleOfFive = value % 5 === 0;

            if (multipleOfThree && multipleOfFive) {
                console.log("FizzBuzz");
            }
            else if (multipleOfThree) {
                console.log("Fizz");
            }
            else if (multipleOfFive) {
                console.log("Buzz");
            } else {
                console.log(value);
            }
        });

const fizzBuzzLookupTable = n =>
    Array
        .from({ length: n }, (_, i) => i + 1)
        .forEach((value) => {
            const multipleOfThree = value % 3 === 0;
            const multipleOfFive = value % 5 === 0;
            const multitpleOfThreeAndFive = multipleOfThree && multipleOfFive;
            const multipleOfNeitherThreeOrFive = !multipleOfThree && !multipleOfFive;

            const conditions = {
                [multipleOfThree]: "Fizz",
                [multipleOfFive]: "Buzz",
                [multitpleOfThreeAndFive]: "FizzBuzz",
                [multipleOfNeitherThreeOrFive]: value
            };

            console.log(conditions[true]);
        });

const fizzBuzzReduce = n =>
    Array
        .from({ length: n }, (_, i) => i + 1)
        .reduce((result, value) => {
            const multipleOfThree = value % 3 === 0;
            const multipleOfFive = value % 5 === 0;
            const multitpleOfThreeAndFive = multipleOfThree && multipleOfFive;
            const multipleOfNeitherThreeOrFive = !multipleOfThree && !multipleOfFive;

            const conditions = {
                [multipleOfThree]: "Fizz",
                [multipleOfFive]: "Buzz",
                [multitpleOfThreeAndFive]: "FizzBuzz",
                [multipleOfNeitherThreeOrFive]: value
            };

            result = [...result, conditions[true]];
            return result;
        }, []);

const fizzBuzzMap = n =>
    Array
        .from({ length: n }, (_, i) => i + 1)
        .map((value) => {
            const multipleOfThree = value % 3 === 0;
            const multipleOfFive = value % 5 === 0;
            const multitpleOfThreeAndFive = multipleOfThree && multipleOfFive;
            const multipleOfNeitherThreeOrFive = !multipleOfThree && !multipleOfFive;

            const conditions = {
                [multipleOfThree]: "Fizz",
                [multipleOfFive]: "Buzz",
                [multitpleOfThreeAndFive]: "FizzBuzz",
                [multipleOfNeitherThreeOrFive]: value
            };

            return conditions[true];
        });