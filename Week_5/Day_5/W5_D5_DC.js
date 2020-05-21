function pyramid(height){
	let result = [];
	for(let i = 0; i < height; i++) {
		let spaces = " ".repeat(height - i);
		let block = "*".repeat(i * 2 + 1);
		result.push(`${spaces}${block}${spaces}`);
	}
	return result.join("\n");
}
console.log(pyramid(5));


function pyramid(height){
	let result = [];
	for(let i = 0; i < height; i++) {
		let spaces = " ".repeat(height - i);
		let block = "*".repeat(i * 1 + 1);
		result.push(`${spaces}${block}${spaces}`);
	}
		return result.join("\n");
}
console.log(pyramid(5));