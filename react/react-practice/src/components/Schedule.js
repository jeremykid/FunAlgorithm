import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import {getSchedule,updateSchedule} from '../actions/ScheduleActions.js'
import { connect } from "react-redux"
import { BootstrapTable, TableHeaderColumn } from 'react-bootstrap-table';
var schedule = [{
      id: 1,
      name: "Item name 1",
      price: 100
  },{
      id: 2,
      name: "Item name 2",
      price: 100
  }];

const girlNameArray = [' ','Alexa','Katana','Lexi','Stacey','Cherry','Indira','Kelly','Princess','Scarlette','Sterling',"Tasia","Uliana","Jaina","Anastajza","Sugarplum","Maliah"];

const cellEditProp = {
  mode: 'click',
  blurToSave: true

};
@connect((store) => {
  return {
    schedule: store.schedule
  };
})
class Schedule extends Component {
  showSchedule(){
    // console.log(schedule)
    console.log(this.props.schedule.schedule)
    console.log(this.reverseSchedule())
  }
  updateSchedule(){
    this.props.dispatch(updateSchedule(this.reverseSchedule()));
  }
  componentWillMount(){
  	this.props.dispatch(getSchedule())
  }

  convertSchedule(){
    var returnArray = []
    var weekDays = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']; 
    for (var index = 0;index<7;index++){
      if (this.props.schedule.schedule[index]){
        var row = {
          id:weekDays[index],
          am1:this.props.schedule.schedule[index].am[0],
          am2:this.props.schedule.schedule[index].am[1],
          am3:this.props.schedule.schedule[index].am[2],
          am4:this.props.schedule.schedule[index].am[3],
          am5:this.props.schedule.schedule[index].am[4],
          pm1:this.props.schedule.schedule[index].pm[0],
          pm2:this.props.schedule.schedule[index].pm[1],
          pm3:this.props.schedule.schedule[index].pm[2],
          pm4:this.props.schedule.schedule[index].pm[3],
          pm5:this.props.schedule.schedule[index].pm[4],
        };
        returnArray.push(row)
      }
    }
    return returnArray
  }
  reverseSchedule(){
    var returnArray = []
    for (var index = 0;index<7;index++){
      if (schedule[index]){
        var am = []
        am.push(schedule[index].am1)
        am.push(schedule[index].am2)
        am.push(schedule[index].am3)
        am.push(schedule[index].am4)
        am.push(schedule[index].am5)
        var pm = []
        pm.push(schedule[index].pm1)
        pm.push(schedule[index].pm2)
        pm.push(schedule[index].pm3)
        pm.push(schedule[index].pm4)
        pm.push(schedule[index].pm5)


        var row = {am:am,pm:pm
        };

        returnArray.push(row)
      }
    }

     return returnArray
  }

  render() {
    schedule=  this.convertSchedule()


    return (
      <div>
             <button   onClick = {this.showSchedule.bind(this)} />
      <BootstrapTable data={ schedule }
                  cellEdit={ cellEditProp }>
           
        <TableHeaderColumn dataField='id' isKey>ID</TableHeaderColumn>
        <TableHeaderColumn dataField='am1' editable={ { type: 'select', options: { values: girlNameArray } } }> 1 </TableHeaderColumn>
        <TableHeaderColumn dataField='am2' editable={ { type: 'select', options: { values: girlNameArray } } }> 2 </TableHeaderColumn>
        <TableHeaderColumn dataField='am3' editable={ { type: 'select', options: { values: girlNameArray } } }> 3 </TableHeaderColumn>
        <TableHeaderColumn dataField='am4' editable={ { type: 'select', options: { values: girlNameArray } } }> 4 </TableHeaderColumn>
        <TableHeaderColumn dataField='am5' editable={ { type: 'select', options: { values: girlNameArray } } }> 5 </TableHeaderColumn>
        <TableHeaderColumn dataField='pm1' editable={ { type: 'select', options: { values: girlNameArray } } }> 1 </TableHeaderColumn>
        <TableHeaderColumn dataField='pm2' editable={ { type: 'select', options: { values: girlNameArray } } }> 2 </TableHeaderColumn>
        <TableHeaderColumn dataField='pm3' editable={ { type: 'select', options: { values: girlNameArray } } }> 3 </TableHeaderColumn>
        <TableHeaderColumn dataField='pm4' editable={ { type: 'select', options: { values: girlNameArray } } }> 4 </TableHeaderColumn>
        <TableHeaderColumn dataField='pm5' editable={ { type: 'select', options: { values: girlNameArray } } }> 5 </TableHeaderColumn>
      </BootstrapTable>
       <button   onClick = {this.updateSchedule.bind(this)} >update</button>
      </div>
    )
  }
}

export default Schedule
