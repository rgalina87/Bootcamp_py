let message = prompt('Enter several words', ' ');
if (message != null) {
	document.getElementById("demo").innerHTML =
	"Good choise!"
} 
 
let result = (typeof message === 'string')
console.log(result)

 function repeteadLetters(str, letter) 
{
 let sortArray = 0 
 for (let i = 0; i < str.length; i++) 
 {
    if (str.charAt(i) == letter) 
      {
      letter_Count += 1;
      }
  }
  return letter_Count;
}

console.log(char_count(' ', ' '));