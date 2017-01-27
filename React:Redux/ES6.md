ES5 ES6对照表

引入包

ES5

```
var React = require("react");
var { Component } = React;

var MyComponent = require('./MyComponent');
```

ES6

```
import React, { Component } from 'react';

import MyComponent from './MyComponent';
```


建立组件

ES5

```
var MyComponent = React.createClass({
    render: function() {
        return (
            <div>
            	My Component
            </div>
        );
    },
});
```

ES6

```
class Photo extends React.Component {
    render() {
        return (
            <div>
            	My Component
            </div>
        );
    }
}
```