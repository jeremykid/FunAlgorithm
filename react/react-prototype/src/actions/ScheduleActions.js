import { browserHistory } from 'react-router';


export function getSchedule() {
   return function(dispatch) {
   	   dispatch({type: "GET_SCHEDULE"})

          dispatch({type: "GET_SCHEDULE_FULFILLED", payload: "success"})
         dispatch({type: "GET_SCHEDULE_REJECTED", payload: err.message})

   }
}

export function updateSchedule(schedule) {
   return function(dispatch) {
    dispatch({type: "UPDATE_SCHEDULE"})

    dispatch({type: "UPDATE_SCHEDULE_FULFILLED"})
    dispatch({type: "UPDATE_SCHEDULE_REJECTED", payload: err.message})
   }
}