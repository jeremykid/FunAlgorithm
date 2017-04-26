export default function reducer(state={
    error: null,
    fetching: false,
    isFetched: false,
    schedule:{
        mon: {
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        tue: {
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        wed: {
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        thu: {
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        fri:{
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        sat:{
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        },
        sun:{
          am:[1,2,3,4,5],
          pm:[1,2,3,4,5]
        }
    }
    

  }, action) {

    switch (action.type) {

        case "GET_SCHEDULE":{
            return {...state, 
               fetching: true,
               isFetched: false,
            }
        }
        case "GET_SCHEDULE_FULFILLED": {
            return {...state,
               fetching: false,
               isFetched: true, 
               schedule: action.payload 
           }
        }
        case "GET_SCHEDULE_REJECTED": {
            return {...state, 
               fetching: false,
               isFetched: false,
               error: action.payload 
           }
        }
        case "UPDATE_SCHEDULE":{
            return {...state, 
               fetching: true,
               isFetched: false,
            }
        }
        case "UPDATE_SCHEDULE_FULFILLED": {
            return {...state,
               fetching: false,
               isFetched: true, 
           }
        }
        case "UPDATE_SCHEDULE_REJECTED": {
            return {...state, 
               fetching: false,
               isFetched: false,
               error: action.payload 
           }
        }

    }

    return state
}