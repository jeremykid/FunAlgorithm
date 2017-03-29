import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
import $ from "jquery"
import FieldGroup from "../react-basic/FieldGroup.js"
import {uploadAvatar, getAvatar} from "../../actions/faceReconizationActions.js"
import {ButtonToolbar,Button} from 'react-bootstrap'

//todo

@connect((store) => {
  return {
    faceReconization: store.faceReconization
  };
})
class reactFaceReconization extends Component {
  constructor(props) {
    super(props)
    this.state = {file: '',imagePreviewUrl: '', age:0, gender:""
	}
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

	componentWillReceiveProps(nextProps){
		// console.log(nextProps.faceReconization.url);
		console.log(nextProps)
		if (nextProps.faceReconization.url != ""){
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
			    	this.setState({
			    		age: data.faces[0].attributes.age.value,
						gender: data.faces[0].attributes.gender.value,
			    	})
			    }.bind(this),
			    error:function(data){
			    	console.log(data);
			    }
			});
		}

	 }
	

	
	send(){
		console.log(this.state)
		if (this.state.file){
			this.props.dispatch(uploadAvatar(this.state.file))
		}
	}
	

	render() {
    let {imagePreviewUrl} = this.state;
    let imagePreview = null;
    if (imagePreviewUrl) {
      imagePreview = (<img src={imagePreviewUrl} />)
    } else {
      imagePreview = (<div>Please choose an image. </div>)
    }
    	return (
		<div className="previewComponent">
	        <form>
	          <FieldGroup
	            id="formControlsAvatar"
	            type="file"
	            label=""
	            onChange={(e)=>this.imageChange(e)}
	          />
	          <ButtonToolbar>
	            <Button type="submit" bsStyle="primary" onClick = {this.send.bind(this)}>
	              Upload
	            </Button>
	            <Button 
	              type="reset" 
	              onClick={()=>this.setState({
	                file: '',
	                imagePreviewUrl: ''
	              })}
	              >
	              Cancel
	            </Button>
	          </ButtonToolbar>
	        </form>
	        {this.state.age}
	        {this.state.gender}
		</div>
    )
  }
}

export default reactFaceReconization

