import { combineReducers } from 'redux'

import schedule from "./scheduleReducers.js"
import lifeCycle from "./lifeCycle.js"

export default combineReducers({
    schedule,
    lifeCycle,
})