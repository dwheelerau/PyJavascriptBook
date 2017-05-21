var studentData = [
    {'name': 'Bob', 'id': 0, 'scores': [50,60,60,70]}, 
    {'name': 'Alice', 'id': 1, 'scores': [55,65,65,75]}, 
    {'name': 'Carol', 'id': 2, 'scores': [53,63,63,73]}, 
    {'name': 'Dan', 'id': 3, 'scores': [57,66,67,76]}, 
];

function processStudentData(data, passThres, meritThres){
    passThres = typeof passThres !== 'undefined'?\
                passThres: 60;

