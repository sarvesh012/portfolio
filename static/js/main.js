
// Search
function myFunction() {
	// Declare variables
	var input, filter, project, post, title, i, txtTitle;
	input = document.getElementById("myInput");
	filter = input.value.toUpperCase();
	project = document.getElementById("projects");
	post = project.getElementsByTagName("article");

//   Loop through all title posts, and hide those who don't match the search query
	for (i = 0; i < post.length; i++) {
		title = post[i].getElementsByClassName("post-title")[0];
		if (title) {
			txtTitle = title.textContent || title.innerText;
			if (txtTitle.toUpperCase().indexOf(filter) > -1){
			post[i].style.display = "";
			} else {
			post[i].style.display = "none";
			}
		}
	}
}
