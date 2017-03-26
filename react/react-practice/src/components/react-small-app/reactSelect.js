import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import Select from 'react-select';

// Be sure to include styles at some point, probably during your bootstrapping
import 'react-select/dist/react-select.css';

var options = [
	{ value: 'one', label: 'One' },
	{ value: 'two', label: 'Two' },
	{ value: 'There', label: 'Are' },
	{ value: 'University', label: 'University' },
	{ value: 'Alberta', label: 'Alberta' },
	{ value: 'one', label: 'One1' },
	{ value: 'two', label: 'Two1' },
	{ value: 'There', label: 'Are1' },
	{ value: 'University', label: 'University1' },
	{ value: 'Alberta', label: 'Alberta1' },
	{ value: 'one', label: 'One2' },
	{ value: 'two', label: 'Two2' },
	{ value: 'There', label: 'Are2' },
	{ value: 'University', label: 'University2' },
	{ value: 'Alberta', label: 'Alberta2' },
];

function logChange(val) {
	console.log("Selected: " + val);
}

class reactSelect extends Component {
	constructor(props) {
	  super(props);
	  console.log("constructor")
		this.state = {
      		value:"",
    	};
	}  

	componentWillMount(){
		console.log("will mount");
	}

	componentDidMount(){
		console.log("did mount");
	}

	onChange(value) {
		this.setState({
			value
		})
	}

  render() {
    return (
    	<div>
			<Select
				name="form-field-name"
				value={this.state.value}
				options={options}
				onChange={this.onChange.bind(this)}
			/>        
		</div>
    )
  }
}

export default reactSelect



