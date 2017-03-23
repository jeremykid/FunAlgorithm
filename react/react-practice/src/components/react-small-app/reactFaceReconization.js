import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
import $ from "jquery"
//todo
class reactFaceReconization extends Component {
	constructor(props) {
	  super(props);
	  console.log("constructor")
	}  

	componentWillMount(){
		console.log("will mount");
	}

	componentDidMount(){
		console.log("did mount");
	}
	shouldComponentUpdate(nextProps, nextState){
		
	}

	send(){
	    // var sendData = {};
	    // sendData.api_key ='Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4';
	    // sendData.api_secret ='tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU';
	    // sendData.return_attributes = 'gender,age,smiling,glass,headpose,facequality,blur';
	    // sendData.image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQKimYbw85PQbu84-o0n9rIsctHhqWJ5ZCeQ8HQSj-gF8mhgM-cnewwg';
	    // console.log(sendData);

	    var sendData = new FormData();
	    sendData.append('api_key','Bn7swhGpvtzxS9uMWG-0CkacJY-_gt-4');
	    sendData.append('api_secret','tNCF8Wd-xjtw-qyQn47yjZh8RzLkVBkU');
	    sendData.append('return_attributes','gender,age,smiling,glass,headpose,facequality,blur');
	    sendData.append('image_url','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQKimYbw85PQbu84-o0n9rIsctHhqWJ5ZCeQ8HQSj-gF8mhgM-cnewwg')
	    console.log(sendData);
	    $.ajax({
	        url: 'https://api-us.faceplusplus.com/facepp/v3/detect',
	        type: 'POST',
	        dataType: 'json',
	        cache: false,
	        data: sendData,
	        processData: false,
	        contentType: false,
        	success: function (data)
	        {
	        	console.log(data);
	        },
	        error:function(data){
	        	console.log(data);
	        }
	    });
	}
	

  render() {
    return (
    	<div>
 		<div>React Login Component </div>
 		 <button onClick={this.send.bind(this)} > </button>
        </div>
    )
  }
}

export default reactFaceReconization

