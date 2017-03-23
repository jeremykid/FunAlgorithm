import React, { Component } from 'react'
import { Router, Route, Link, IndexRoute, hashHistory, browserHistory } from 'react-router'


import App from "./App.js"
import WechatLogin from "./react-wechat/WechatLogin.js"
import reactLifeCycle from "./react-basic/reactLifeCycle.js"
import reactSelect from "./react-small-app/reactSelect.js"
import reactFaceReconization from "./react-small-app/reactFaceReconization.js"

class ReactRouter extends Component {

	render() {
		return(
			<Router history={hashHistory}>
			<Route path='/' component={App} />
			<Route path='/WechatLogin' component={WechatLogin} />
			<Route path='/reactbasic/reactLifeCycle' component={reactLifeCycle} />
			<Route path='/reactsmallapp/reactFaceReconization' component = {reactFaceReconization}/>
			<Route path='/reactsmallapp/reactSelect' component={reactSelect} />
			{/* 404 not fond page, make sure it stay at bottom */}
        	<Route path='*' component={NotFound} />
			</Router>
		)
		


	}


}


// Hard coded pages (TEMP!)
const NotFound = () => <h1>404.. This page is not found!</h1>

export default ReactRouter
