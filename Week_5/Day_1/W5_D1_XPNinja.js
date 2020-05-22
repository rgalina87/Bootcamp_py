function calculateTips() {
	let billAmt = document.getElementById('billamt').innerHTML;
	let serviceQual = document.getElementById('serviceQual');
	let numOfPeople = parseInt(document.getElementById("numOfPeople").innerHTML);

		if (serviceQual === 0 || billAmt === 'undefined') {
			alert("Enter the values!");
			return;
		}

		if (!numOfPeople || numOfPeople < 1){
			let each = document.getElementById("each");
      each.setAttribute("display", "none");
    }     

	let total = billAmt*serviceQual/numOfPeople;
	total.toFixed(2); 
}


calculateTips()


let total = document.getElementById("totalTip");
	total.setAttribute("display", "block");
	let tip = parseInt(document.getElementById("tip").innerHTML = [total]);
	if (!calculateTips)
		total.setAttribute("display", "none");
	let calculate =document.getElementById("calculate").addEventListener('click' calculateTips);
	if(calculate === true){
		console.log(calculateTips());
	} 




