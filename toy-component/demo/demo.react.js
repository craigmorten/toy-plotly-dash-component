import React, {Component} from 'react';
import {ToyComponent} from '../src';

class Demo extends Component {
    constructor() {
        super();
        this.state = {
            value: ''
        }
    }

    render() {
        return (
            <div className="container">
                <h1>Demo: toy-component</h1>

                <ToyComponent
                    id="toy-input"
                    label="This is an example label"
                    value={this.state.value}
                    setProps={newProps => this.setState({value: newProps.value})}
                />

                <div id="output">You have entered: {this.state.value}</div>
            </div>
        );
    }
}

export default Demo;
