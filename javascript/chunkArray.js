function chunk(array, size) {
    // Create empty array to hold chunks
    let result = [];
    // For each element in the original array
    for (let i = 0; i < array.length; i += size) {
        // Slice off a chunk from the original array and
        // push it into the result
        result.push(array.slice(i, i + size));
    }
    return result;
}

let example1 = chunk([1, 2, 3, 4], 2); // [[1, 2], [3, 4]]
// console.log(example1);
let example2 = chunk([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
// console.log(example2);
// ------------------------------------------------------------------------------------------------------
function chunkAlt(array, size) {
    // Create an empty array to hold chunks called result
    const result = [];
    // For each element in the original array
    for (let element of array) {
        // Retrieve the last element in the result array
        const last = result[result.length - 1];
        // If the last element does not exist, or if the length 
        // is equal to the size param
        if (!last || last.length === size) {
            // Push a new chunk into result with current element
            result.push([element]);
        } else {
            // Else add the current element into the chunk
            last.push(element);
        }
    }
    return result;
}

let example1alt = chunkAlt([1, 2, 3, 4], 2); // [[1, 2], [3, 4]]
// console.log(example1alt);
let example2alt = chunkAlt([1, 2, 3, 4, 5], 2); // [[1, 2], [3, 4], [5]]
// console.log(example2alt);

// ES6 + Syntax
// ------------------------------------------------------------------------------------------------------
const chunkReduce = (array, size) =>
    array.reduce((result, value, index) => (
        index % size
            ? result[result.length - 1].push(value)
            : result.push([value]), result
    ), []);

// console.log(chunkReduce([1, 2, 3, 4], 2));
// ------------------------------------------------------------------------------------------------------
const chunkMap = (array, size) =>
    [...Array(Math.ceil(array.length / size))]
        .map((_, index) =>
            array.slice(index * size, size + size * index)
        );

// console.log(chunkMap([1, 2, 3, 4], 2));
// console.log(chunkMap([1, 2, 3, 4, 5], 2));
// ------------------------------------------------------------------------------------------------------
const chunkRecursive = (array, size) =>
    array.length === 0
        ? []
        : [array.slice(0, size)]
            .concat(
                chunkRecursive(array.slice(size), size)
            );

console.log(chunkRecursive([1, 2, 3, 4], 2));
console.log(chunkRecursive([1, 2, 3, 4, 5], 2));