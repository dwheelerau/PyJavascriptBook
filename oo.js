// Citizen is a base object for building Winner subclasses
var Citizen = {
    setCitizen: function(name, country){
        this.name = name;
        this.country = country;
        return this;
    },
    printDetails: function(){
        console.log('Cit' + this.name + ' from' + this.country);
    }
};
// use Citizen to create a winner object
var Winner = Object.create(Citizen);

Winner.setWinner = function(name, country, category, year){
    this.setCitizen(name, country);
    this.category = category;
    this.year = year;
    return this;
};

Winner.printDetails = function() {
    console.log('Nobel winner' + this.name + ' from' + this.country 
        + 'catog ' + this.category + ' year' + this.year);
};

var albert = Object.create(Winner).setWinner('Albert I', 'swit', 'phy', 2222);

albert.printDetails();
