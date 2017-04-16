import {firebaseApp,firebaseAuth,firebaseDb, firebaseStorage, firebaseAuthInstance } from '../components/Firebase.js'
import { browserHistory } from 'react-router';

export function goToNextState() {
	return function(dispatch) {
		dispatch({type: "GET_SCHEDULE"})
	}
}

const update = (todoId, isDone) => (dispatch) =>
  new Promise(function(resolve, reject) {
    dispatch({
      type: 'SET_SAVING',
      saving: true
    });
    // Function is expected to return a promise
    callUpdateApi(todoId, isDone).then(updatedTodo => {
      dispatch({
        type: 'SET_SAVING',
        saving: false
      });

      resolve(updatedTodo);
    }).catch(error => {
      // TBD: Handle errors for Redux

      reject(error);
    })
  });

export function testPromise() {
	return function(dispatch) {
		dispatch({type: "GET_SCHEDULE"})
	}

}
