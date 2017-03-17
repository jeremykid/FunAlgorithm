import { combineReducers } from 'redux'

import schedule from "./scheduleReducers.js"
import lifeCycle from "./lifeCycleReducers.js"

export default combineReducers({
    schedule,
    lifeCycle,
})