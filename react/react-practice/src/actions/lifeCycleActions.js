import {firebaseApp,firebaseAuth,firebaseDb, firebaseStorage, firebaseAuthInstance } from '../components/Firebase.js'
import { browserHistory } from 'react-router';

export function goToNextState() {
	return function(dispatch) {
		dispatch({type: "GET_SCHEDULE"})
	}
}

export function testPromise() {
	let response = new Promise()
	return function(dispatch) {
		dispatch({type: "TEST_PROMISE"})
	}
}