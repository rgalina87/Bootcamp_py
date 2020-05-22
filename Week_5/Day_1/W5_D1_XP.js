function task(){
		let addclass = document.getElementsByTagName("p");
		addclass.setAttribute('class', 'para-article');
		//addclass += ' para_article';
		//addclass.classList.add('para_article')
	}
		let para = document.getElementsByTagName("p");
		para.removeChild(para.lastChiled);
		// let parent = document.getElementsByTagName("article");
		// let child = document.getElementsById("para4");
		// parent.removeChild(chiled);

		let h2 = getElementsByTagName("h2");
		h2.addEventListener("click", function(remove){
			let target = remove.target;
			if (target.id === 'yes') {
				h2.parentNode.removeChild("h2");
			}
		});

		//function randomFontSize (size) {
		document.getElementsByTagName("h1").style.fontSize = Math.random(1, 101);

		
			let p = document.getElementsByTagName("p")
			p.addEventListener('click', hideParagraph);
			function hideParagraph (first_para) {
			let hidde = first_para;
			if (hidde === 'yes') {
				//para_article > p:first-chiled{
					display:none;
				}
			}

	let paragraphs = document.getElementsByTagName("p");
	let p2 = paragraphs[1];
	p2.setAttribute("onclick", "fadeOutEffect()");
	console.log(p2);	

	function fadeOutEffect() {
	    let fadeTarget = p2;
	    let fadeEffect = setInterval(function () {
	        if (!fadeTarget.style.opacity) {
	            fadeTarget.style.opacity = 1;
	        }
	        if (fadeTarget.style.opacity > 0) {
	            fadeTarget.style.opacity -= 0.3;
	        } 
	    }, 2000);
	}