import firebase from 'firebase';
import {FIREBASE_CONFIG} from '../../firebase.config.js';

export const firebaseApp = firebase.initializeApp(FIREBASE_CONFIG);

export const firebaseAuth = firebaseApp.auth();

export const firebaseDb = firebaseApp.database();

export const firebaseStorage = firebaseApp.storage().ref();

export const firebaseUploadState = firebase.storage.TaskEvent.STATE_CHANGED;