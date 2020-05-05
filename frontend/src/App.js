// import React from 'react';
import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
// import GithubCommit from "./component/comp1"
import DataLoader from "./component/comp2"
function App() {
  const greeting = 'Do database migration to fetch results from api';
  return (
    <div className="App">
      <header className="App-header">
       <DataLoader/>
      
      <Headline prop1 ={greeting} />
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          This is written in React and orchestrated using Docker.
        </a>
      </header>
    </div>
  );
}

// function Headline2(props) {
 
 
//   return   <h1>{props.value}</h1>  ;
// }

// const Headline = ({prop1})=><div><h1>{prop1}</h1> <h1>{prop1}</h1></div> 
 
const Headline = ({prop1}) => {
  const [greeting, setGreeting] = useState(
    'Hello, DO DB Migration to fetch results'
  );
 
  return (
    <div>
      <h1>{greeting}</h1>
 
      <input
        type="text"
        value={prop1}
        onChange={event => setGreeting(event.target.value)}
      />
    </div>
  );
};
export default App;
