//first part
	function playTheGame(){
	let question = prompt("Do you want to play?");
	let userNumber
	if (question.toLowerCase() == "yes") {
		userNumber = prompt("Please choose a number between 0-10: ")
	}
	else {
		alert("No problem, Goodbye");
		return;	
	}
	if (isNaN(userNumber)){
		alert("Sorry Not a number, Goodbye")
	}
	else if (userNumber < 0 || userNumber > 10){
			alert("Sorry it's not a good number,Goodbye")			
	}
	else {
		let computerNumber = Math.floor(Math.random() * 11);
		console.log(computerNumber);
	}
}
	playTheGame()

//second part
function test (myNumber, computerNumber){
	if ("myNumber" = "computerNumber") {
		alert ("You won!!!");
	else if ("myNumber" > "computerNumber")
		alert ("It's to big. One more try!!!");
	else if("myNumber" < "computerNumber")	
		alert ("It's to small. One more try!!!");	
	} else {
		alert ("You cant try anymore. The right answer is ${computer}")
	}
}
//third part

test(0, 10)