    	function volum () {
    		let volum;
    		let radius = document.getElementsById('radius').value;
    		radius = Math.abs(radius);
    		volum = (4/3) * Math.PI * Math.pow(radius, 3);
    		volum = volum.toFixed(4);
    		document.getElementsById('volume').value = volume;
    		return false;
    	}