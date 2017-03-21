import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import WechatLogin from "./react-wechat/WechatLogin.js"
import reactLifeCycle from "./react-basic/reactLifeCycle.js"
import { Router, Route, Link, browserHistory, IndexRoute  } from 'react-router'

class App extends Component {
  render() {
    return (
    <div>	
      <h1>Wechat</h1>
      <WechatLogin />
			<Link to="/reactbasic/reactLifeCycle" > gotoLifeCycle </Link>

			<Link to="/reactsmallapp/reactSelect" > react autocomplete </Link>

      </div>
    )
  }
}

export default App
