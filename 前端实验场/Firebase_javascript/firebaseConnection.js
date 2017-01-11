var firebaseDBgirls = new Firebase('https://vipspa-4c43f.firebaseio.com/girl');
// var firebaseDBgirls = new Firebase('https://moviefire.firebaseio.com/movies');

function saveToList(event) {
    if (event.which == 13 || event.keyCode == 13) { // as the user presses the enter key, we will attempt to save the data
        var girl = document.getElementById('girl').value.trim();
        if (girl.length > 0) {
            saveToFB(girl);
        }
        document.getElementById('girl').value = '';
        return false;
    }
};
 
function saveToFB(girl) {
    // this will save data to Firebase
    firebaseDBgirls.push({
        name: girl
    });
};
 
function refreshUI(list) {
    var lis = '';
    console.log(list);

    for (var i = 0; i < list.length; i++) {
        lis += '<li data-key="' + list[i].key + '">' + list[i].name + ' [' + genLinks(list[i].key, list[i].name) + ']</li>';
    };
    document.getElementById('favMovies').innerHTML = lis;
};
 
function genLinks(key, mvName) {
    var links = '';
    links += '<a href="javascript:edit(\'' + key + '\',\'' + mvName + '\')">Edit</a> | ';
    links += '<a href="javascript:del(\'' + key + '\',\'' + mvName + '\')">Delete</a>';
    return links;
};
 
function edit(key, mvName) {
    var movieName = prompt("Update the movie name", mvName); // to keep things simple and old skool :D
    if (movieName && movieName.length > 0) {
        // build the FB endpoint to the item in movies collection
        var updateMovieRef = buildEndPoint(key);
        updateMovieRef.update({
            name: movieName
        });
    }
}
 
function del(key, mvName) {
    var response = confirm("Are certain about removing \"" + mvName + "\" from the list?");
    if (response == true) {
        // build the FB endpoint to the item in movies collection
        var deleteMovieRef = buildEndPoint(key);
        deleteMovieRef.remove();
    }
}
 
function buildEndPoint (key) {
	return new Firebase('https://vipspa-4c43f.firebaseio.com/girl' + key);
}
 
// this will get fired on inital load as well as when ever there is a change in the data
firebaseDBgirls.on("value", function(snapshot) {
    console.log(snapshot);
    var data = snapshot.val();

    var list = [];
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
            name = data[key].name ? data[key].name : '';
            if (name.trim().length > 0) {
                list.push({
                    name: name,
                    key: key
                })
            }
        }
    }
    // refresh the UI
    refreshUI(list);
});