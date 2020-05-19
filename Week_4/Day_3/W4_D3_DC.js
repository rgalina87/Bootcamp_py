let allBooks = [
{titel: "Dracula", author: "Bram Stoker", image: (url), status: "alreadyRead"}, //status: alreadyRead(true), 
{tittle: "Interview with a Vapire", author: "Ann Raise", image: (url), status: "alreadyRead"},
];

function generateTableHead(tabel, data){
	let thead = table.creatThead();
	let row = thead.insertRow();
	for (let key of data) {
		let th = document.createElement("th");
		let text = document.createTextNode(key);
		th.appendChild(text);
		row.appendChild(th);
	}
}

function generateTable(table, data) {
	for (let element of data) {
		let row = table.insertRow();
		for (key in element) {
			let cell = row.insertCell();
			let text = document.creatTextNode(element[key]);
			cell.appendChild(text);
		}
	}
}

	let table = document.querySelector("table");
	let data = Object.keys(allBooks[0]);
	generateTable(table, allBooks);
	generateTableHead(table, data);

//?????You have to display the book’s title then “written by” and then the book’s author (Ex: HarryPotter written by JKRolling)
//don't understand the task
	let book = Object.keys(title) "+ written by +" Object.keys(author);

	
	let image = Object.keys(image)[0];
	image.setAttribute("stile", "width:100");

	let status = Object.key(alreadyRead)[0]
	if (status = true) {
		status.setAttribute("style", "color:red");
	} else {
		satatus.setAttribute("style", "none");
	}

	

	
