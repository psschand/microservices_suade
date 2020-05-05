import React, { useState, useEffect } from "react";

export default function DataLoader() {
  const [data, setData] = useState([]);

 const update = () => {

    fetch("http://192.168.99.100:8081/v1/reports/")
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.log(error));
  }

  return (
    <div>
      <button onClick={update}>fetch results</button>
  
      <li>
      {JSON.stringify(data)}
      </li>
    </div>
  );
}