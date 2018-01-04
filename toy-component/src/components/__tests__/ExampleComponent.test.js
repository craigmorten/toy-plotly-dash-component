import React from 'react';
import {shallow} from 'enzyme';
import ToyComponent from '../ToyComponent.react';

describe('ToyComponent', () => {

    it('renders', () => {
        const component = shallow(<ToyComponent label="Test label"/>);
        expect(component).to.be.ok;
    });
});
