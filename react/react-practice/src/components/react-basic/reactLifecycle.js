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

	componentWillReceiveProps(nextProps){
		console.log("receive "+nextProps)
	}

	shouldComponentUpdate(nextProps, nextState){
		console.log("nextProps"+nextProps)
		console.log("nextState"+nextState)
	}

	componentWillUpdate(nextProps, nextState){
		console.log("nextProps"+nextProps)
		console.log("nextState"+nextState)
	}

	componentDidUpdate(prevProps, prevState){
		console.log("nextProps"+nextProps)
		console.log("nextState"+nextState)	
	}
	componentWillUnmount(){

	}

	forceUpdate(){
		
	}

  render() {
    return (
 		<div>React Login Component </div>
    )
  }
}

export default reactLifeCycle

