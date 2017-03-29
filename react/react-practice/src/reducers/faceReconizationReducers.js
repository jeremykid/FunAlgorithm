export default function reducer(state={
    error: null,
    fetching: false,
    isFetched: false,
    url:"",
  }, action) {

    switch (action.type) {
        case "SAVE_PICTURE":{
            return {...state, 
               fetching: true,
               isFetched: false,
            }
        }
        case "SAVE_PICTURE_FULFILLED":{
            return {...state, 
              fetching: true,
              isFetched: false,
              url: action.payload, 
            }
        }
        case "SAVE_PICTURE_REJECTED":{
            return {...state, 
               fetching: true,
               isFetched: false,
               error: action.payload 
        }
        }
    }
    return state
}