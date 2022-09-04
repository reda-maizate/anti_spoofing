import React from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './components/header/Header';
import UploadPicture from './components/uploadPicture/UploadPicture';

function App() {
  return (
    <div className="App">
      <Header />
      <UploadPicture />
    </div>
  );
}

export default App;
