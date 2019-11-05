function passMessageToPy(){
	var username = document.getElementById('icon_prefix').value;
	var message = document.getElementById('icon_message').value;
	//sendint to python
	console.log(username)
	eel.get_message(username, message)(function(ret) {console.log(ret)})
}

