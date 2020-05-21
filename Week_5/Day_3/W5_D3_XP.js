function myMove() {
	let move = document.getElementById("animate");
	let pos = 0;
	let id = setInterval(frame, 1);
	function frame() {
		if (pos == 350) {
		clearInterval(id);
	}else { 
		pos++;
		move.style.left = pos + 'px';
		move.style.right = pos + 'px';
	}
	}
}