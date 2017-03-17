import {firebaseApp,firebaseAuth,firebaseDb, firebaseStorage, firebaseAuthInstance } from '../components/Firebase.js'
import { browserHistory } from 'react-router';

export function goToNextState() {
	return function(dispatch) {
		dispatch({type: "GET_SCHEDULE"})
	}
}