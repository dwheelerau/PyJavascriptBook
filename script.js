// script.js
var data = [3, 4];
var sum = 0;
data.forEach(function(d){
    sum += d;
});

console.log('Sum =' + sum);
console.log('Hello world');

var foo = {'bar': 3, 'baz': 5};

console.log(foo.bar);
console.log(foo['baz']);

// example of loop not used very often anymore
for (var prop in foo) {
        console.log(prop);
}

// more modern way using underscore
//_.each(foo, function(value, key){
//})

var value1 = 3;
var value2 = 2;
// example of js switch
switch(data[0]){
    case value1:
        // excute if expression eq value
        console.log('will print');
        break;
    case value2:
        // excute if ...
        break;
    default:
        // if all else fails
}



