
 //let string= "This book is not so bad!"
 //function replacString('not || bad', 'good', [string]){
 //for (var i = 0; i < string.length; ++i){
 //if (string.substring(i, i + not || bad.length) == not || bad) {
 	//string = string.substring(0, i) + good + string.substring(i + not || bad.length, string.length);
 //}else{
 	//return string;
 //}
//}


function replaceString(any_string) {
	let not_pos = any_string.indexOf("not");
	let bad_pos = any_string.indexOf("bad");
	if (bad_pos > not_pos && not_pos != -1) {
		any_string = any_string.substring(0, not_pos);
		any_string = any_string + "good!";
	}
	console.log(any_string);
}
replaceString("This book is not that bad!");
replaceString("This book is bad!");
replaceString("This book is good!");
