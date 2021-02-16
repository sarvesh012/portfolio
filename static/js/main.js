
let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}


function setTheme(mode){
	
	// static variable from main.html

	if(mode == 'light'){
		document.getElementById('theme-style').href = static + '/white.css'
	}
	if(mode == 'dark'){
		document.getElementById('theme-style').href = static + '/dark.css'
	}
	localStorage.setItem('theme', mode)
}