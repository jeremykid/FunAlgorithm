import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import {FormControl,FormGroup,ControlLabel,HelpBlock} from 'react-bootstrap'

class FieldGroup extends Component{
    render(){
        return (
            <FormGroup controlId={this.props.id}>
            <ControlLabel>{this.props.label}</ControlLabel>
            <FormControl {...this.props} />
            {this.props.help && <HelpBlock>{this.props.help}</HelpBlock>}
            </FormGroup>
        );
    }
}

export default FieldGroup