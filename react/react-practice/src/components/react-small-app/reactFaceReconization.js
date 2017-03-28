import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
import $ from "jquery"
//todo
class reactFaceReconization extends Component {
  constructor(props) {
    super(props)
    this.state = {file: '',imagePreviewUrl: ''}
  }
 
  upload(e) {
    e.preventDefault()
    console.log('temp file object '+this.state.file)
  }

  imageChange(e) {
    e.preventDefault()
    let reader = new FileReader()
    let file = e.target.files[0]
    reader.onloadend = () => {
      this.setState({
        file: file,
        imagePreviewUrl: reader.result
      })
    }
    reader.readAsDataURL(file)
  }

	componentWillMount(){
		console.log("will mount");
	}

	componentDidMount(){
		console.log("did mount");
	}
	shouldComponentUpdate(nextProps, nextState){
		
	}
	componentWillReceiveProps(nextProps){
		//checkt if the image save to the firebase
	}
	

	
	send(){
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
		let {imagePreviewUrl} = this.state;
		let $imagePreview = null;
		    if (imagePreviewUrl) {
		      $imagePreview = (<img src={imagePreviewUrl} />);
		    } else {
		      $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
		    }
    	return (
		<div className="previewComponent">
			<div>React Login Component </div>
			 <button onClick={this.send.bind(this)} > </button>
			<form onSubmit={(e)=>this._handleSubmit(e)}>
			  <input className="fileInput" 
			    type="file" 
			    onChange={(e)=>this._handleImageChange(e)} />
			  <button className="submitButton" 
			    type="submit" 
			    onClick={(e)=>this._handleSubmit(e)}>Upload Image</button>
			</form>
			<div className="imgPreview">
			  {$imagePreview}
			</div>
		</div>
    )
  }
}

export default reactFaceReconization

