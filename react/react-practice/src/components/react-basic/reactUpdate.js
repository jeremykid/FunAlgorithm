import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
import update from 'react-addons-update'; // ES6

class reactUpdate extends Component {
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

export default reactUpdate

