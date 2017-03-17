export default function reducer(state={
    error: null,
    fetching: false,
    isFetched: false,

  }, action) {

    switch (action.type) {
        case "GET_SCHEDULE":{
            return {...state, 
               fetching: true,
               isFetched: false,
            }
        }
    }
    return state
}