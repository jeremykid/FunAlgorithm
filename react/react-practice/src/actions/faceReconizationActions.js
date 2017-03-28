import {firebaseApp,firebaseAuth,firebaseDb, firebaseStorage, firebaseAuthInstance } from '../components/Firebase.js'
import { browserHistory } from 'react-router';

export function uploadAvatar(imgFile, userId){
    return function(dispatch) {
    dispatch({type: "SEND_AVATAR"})
    var uploadTask = firebaseStorage.child('User/' + userId + '/Avatar').put(imgFile)

    // Listen for state changes, errors, and completion of the upload.
    uploadTask.on(firebaseUploadState, // or 'state_changed'
      function(snapshot) {
        // Get task progress, including the number of bytes uploaded and the total number of bytes to be uploaded
        var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        console.log('Upload is ' + progress + '% done');
        switch (snapshot.state) {
          case firebase.storage.TaskState.PAUSED: // or 'paused'
            console.log('Upload is paused');
            break;
          case firebase.storage.TaskState.RUNNING: // or 'running'
            console.log('Upload is running');
            break;
        }
      }, function(err) {
        console.log(err)
        dispatch({type: "SEND_AVATAR_REJECTED", payload: err.code})
    }, function() {
      // Upload completed successfully, now we can get the download URL
      dispatch({type: "SEND_AVATAR_FULFILLED", payload: uploadTask.snapshot.downloadURL})
      // var downloadURL =uploadTask.snapshot.downloadURL;
    });
  }
}

export function getAvatar(){
    return function(dispatch) {
    dispatch({type: "GET_AVATAR"})
    // Create a reference to the file we want to download
    var currentUser = firebaseAuth.currentUser;
    var starsRef = firebaseStorage.child('User/'+currentUser.uid+'/Avatar');

    // Get the download URL
    starsRef.getDownloadURL().then(function(url) {
      console.log(url)
      dispatch({type: "GET_AVATAR_FULFILLED", payload: url})
    }).catch(function(err) {
      console.log(err)
      var url = "/src/images/Avatar.png"
      dispatch({type: "GET_AVATAR_REJECTED",payload: url})
    });
  }
}