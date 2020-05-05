import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

it('renders without crashing...', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('this is just a duplicate to see if realtime changes are tracked...', () => {
  const div = document.createElement('div');
  ReactDOM.render(<App />, div);
  ReactDOM.unmountComponentAtNode(div);
});