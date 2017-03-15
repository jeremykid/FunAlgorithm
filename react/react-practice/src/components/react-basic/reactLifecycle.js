import React, { Component } from 'react'
import ReactDOM from 'react-dom'


class reactLifeCycle extends Component {
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

  render() {
    return (
 		<div>React Login Component </div>
    )
  }
}

export default reactLifeCycle

