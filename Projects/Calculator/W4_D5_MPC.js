function javascript(x) {
	document.getElementById('inputwindow').value += x;
}

function clearInput(y) {
	document.getElementById('inputwindow').value = y;
}

function calculateResult() {
	let result = eval(document.getElementById('inputwindow').value);
	document.getElementById('inputwindow').value = result;
}