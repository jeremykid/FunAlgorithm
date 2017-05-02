import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import {getSchedule,updateSchedule} from '../actions/ScheduleActions.js'
import { connect } from "react-redux"
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';

@connect((store) => {
  return {
    schedule: store.schedule
  };
})
class Schedule extends Component {
  componentWillMount(){
    this.props.dispatch(getSchedule())
  }

  componentWillReceiveProps(nextProps){
    console.log(this.props)
  }
  render() {


    return (
      <div>
      
      </div>
    )
  }
}

export default Schedule
