// script.js
var sum = 0;
data.forEach(function(d) {
    sum += d;
});

console.log('Sum =' + sum);
console.log('Hello world');

var foo = {'bar': 3, 'baz': 5};
var data = [3, 4, 5];

console.log(foo.bar);
console.log(foo.baz);

// example of loop not used very often anymore
Object.keys(foo).forEach(function(b) {
    console.log(b);
});
