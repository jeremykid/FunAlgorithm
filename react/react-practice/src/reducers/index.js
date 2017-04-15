import { combineReducers } from 'redux'

import schedule from "./scheduleReducers.js"
import lifeCycle from "./lifeCycleReducers.js"
import faceReconization from "./faceReconizationReducers.js"

// export default combineReducers({
//     schedule,
//     lifeCycle,
//     faceReconization,
// })

const rootReducer = combineReducers({
    schedule,
    lifeCycle,
    faceReconization,
})
export default rootReducer;
