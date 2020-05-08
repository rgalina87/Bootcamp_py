//first
let colors = {
	first: "red", 
	second: "black", 
	third: "beije", 
	fourth: "grey"
	fav: function(colors) {
	console.log("My #1 is" + this.first + )
	}
}

//second
prompt(Write a number!);
if(promt <= 10) {
	console.log(good job);
} else {
	alert(Write another number!);
}

//third

let people = ["Greg", "Mary", "Devon", "James"];
/*1*/  let peop = people.length;
for (var i = 0; i < peop; i++) {
	console.log(people[i]);
}
/*2*/ people.shift()
/*3*/ people.splice(3, 1, 'Jason')
/*4*/ people.push("IIIIII")
/*5*/ ????
/*6*/Let people2 =people.slice(0, 4);
	console.log(people === people2)
/*7*/people.indexOf("Mary")
/*8*/people.indexOf("Foo")
/*9*/let last_element = people[people.length - 1];



//forth
let age = [20,5,12,43,98,55];
let sum = age.reduce(function (a, b){
	return a+b;
}, 0);
console.log(sum);//233

for (let i of age) {
	if (i % 2 ==0){
		console.log(i)
	}else{
		continue;
	}
}

function getMaxOfArray (age) {
	return Math.max.apply(null, age)
}

