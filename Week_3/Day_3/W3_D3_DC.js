
 let string= "This book is not so bad!"
 function replacString('not || bad', 'good', [string]){
 for (var i = 0; i < string.length; ++i){
 if (string.substring(i, i + not || bad.length) == not || bad) {
 	string = string.substring(0, i) + good + string.substring(i + not || bad.length, string.length);
 }else{
 	return string;
 }
}
