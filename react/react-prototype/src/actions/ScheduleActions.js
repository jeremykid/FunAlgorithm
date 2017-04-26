import {firebaseApp,firebaseAuth,firebaseDb, firebaseStorage, firebaseAuthInstance } from '../components/Firebase.js'
import { browserHistory } from 'react-router';

function jsonToArray(json){
        var arr = [];
        for (var prop in json) {
            arr.push(json[prop]);
        }
        return arr
    }

export function getSchedule() {
   return function(dispatch) {
   	   dispatch({type: "GET_SCHEDULE"})
       firebaseDb.ref('/weekschedule/').once('value')
       .then((snapshot) => {
          // var raw = jsonToArray(snapshot.val());
          dispatch({type: "GET_SCHEDULE_FULFILLED", payload: snapshot.val()})
       })
       .catch((err) => {
         dispatch({type: "GET_SCHEDULE_REJECTED", payload: err.message})
       })

   }
}

export function updateSchedule(schedule) {
   return function(dispatch) {
       dispatch({type: "UPDATE_SCHEDULE"})
       firebaseDb.ref('/weekschedule/').set(schedule)
       .then((snapshot) => {
          dispatch({type: "UPDATE_SCHEDULE_FULFILLED"})
          window.location.reload()
       })
       .catch((err) => {
         dispatch({type: "UPDATE_SCHEDULE_REJECTED", payload: err.message})
       })

   }
}