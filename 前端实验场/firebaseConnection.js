function saveToList(event) {
    if (event.which == 13 || event.keyCode == 13) { // as the user presses the enter key, we will attempt to save the data
        var movieName = document.getElementById('movieName').value.trim();
        if (movieName.length > 0) {
        	var li = '<li>' + movieName + '</li>';
            document.getElementById('favMovies').innerHTML += li;
        }
        document.getElementById('movieName').value = '';
        return false;
    }
}