function getBold_items() {
	let bold = document.getElementsByTagName("strong").querySelectorAll();
}
	let color = document.getElementsByTagName("strong")
	function highlight() {
		color.style.color = "blue";
	}	
	function return_normal() {
		color.style.color = "black"
	}

	color.addEventListener("MouseOver", highlight);
	color.addEventListener("MouseOut", return_normal);