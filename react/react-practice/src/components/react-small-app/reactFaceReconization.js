import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
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

	

  render() {
    return (
    	<div>
 		<div>React Login Component </div>
        </div>
    )
  }
}

export default reactFaceReconization

