import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import { connect } from "react-redux"
import $ from "jquery"
import {ButtonToolbar,Button} from 'react-bootstrap'

class WechatLogin extends Component {

  componentWillMount(){

  }

  get(){
    $.ajax({
	    url: 'http://localhost:3000/api/admins',
	    type: 'GET',
	    dataType: 'jsonp',
	    cache: false,
	    data: {
         format: 'json'
      	},
	    processData: false,
	    contentType: false,
	   	success: function (data)
	    {
	    	console.log("success")
	    	console.log(data);
	    	// dispatch({type:"GET_ADMINACCOUNTS_FULFILLED", payload: data})
	    },
	    error:function(data){
	    	console.log(data);
	    	// dispatch({type:"GET_ADMINACCOUNTS_REJECTED", payload: data})
	    }
	});

  }
  render() {
    return (
    	<div>
 		<div>React Login Component </div>
        <button className="btn-sign" onClick={this.get.bind(this)} >send by ajax</button>
        </div>


    )
  }
}

export default WechatLogin
