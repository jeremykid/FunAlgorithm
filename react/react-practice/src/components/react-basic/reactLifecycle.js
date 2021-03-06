import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect,createStore, applyMiddleware } from "react-redux"
import { getSchedule, testPromise } from '../../actions/lifeCycleActions.js'
import thunk from 'redux-thunk';
import rootReducer from '../../reducers'

const store = createStore(
  rootReducer,
  applyMiddleware(thunk)
);

@connect((store) => {
  return {
    lifeCycle: store.lifeCycle
  };
})
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
		console.log("will unmount")
	}

	forceUpdate(){

	}

	testState(){
		// this.props.dispatch(testPromise()).then(()=>{
		// 	console.log("in then")
		// })
	}

  render() {
    return (
    	<div>
 		<div>React Login Component </div>
        <button className="btn-sign" onClick={this.testState.bind(this)} >Test State</button>
        </div>
    )
  }
}

export default reactLifeCycle

