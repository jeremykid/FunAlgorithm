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

	//Reference from https://facebook.github.io/react/docs/update.html
	simpleUpdate(){
		var initialArray = [1, 2, 3];
		var newArray = update(initialArray, {$push: [4]}); // => [1, 2, 3, 4]
		console.log(initialArray);
		console.log(newArray);
	}
	
	nestedCollections(){
		const collection = [1, 2, {a: [12, 17, 15]}];
		const newCollection = update(collection, {2: {a: {$splice: [[1, 1, 13, 14]]}}});
		// => [1, 2, {a: [12, 13, 14, 15]}]
		console.log(collection);
		console.log(newCollection);
	}
	
	updateByCurrentOne(){
		const obj = {a: 5, b: 3};
		const newObj = update(obj, {b: {$apply: function(x) {return x * 2;}}});
		// => {a: 5, b: 6}
		// This is equivalent, but gets verbose for deeply nested collections:
		const newObj2 = update(obj, {b: {$set: obj.b * 2}});
		console.log(newObj2)
		console.log(newObj)
	}
	
	merge(){
		const obj = {a: 5, b: 3};
		const newObj = update(obj, {$merge: {b: 6, c: 7}}); // => {a: 5, b: 6, c: 7}
		console.log(newObj)
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

