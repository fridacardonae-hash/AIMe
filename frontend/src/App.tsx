import React, { useState } from "react"
import Sidebar from "./components/Sidebar"
import Chat from "./components/Chat"
import "./styles.css"

export default function App(){

 const [open,setOpen] = useState(true)

 return(

  <div className="app">

    <header className="header">

      <button
        className="toggle"
        onClick={() => setOpen(prev => !prev)}
      >
        ☰
      </button>

      <h1>AIMe</h1>

    </header>

    <div className={`main ${open ? "sidebar-open" : ""}`}>

      <div className={`sidebar-wrapper ${open ? "open" : "closed"}`}>
        <Sidebar/>
      </div>

      <Chat/>

    </div>

  </div>

 )
}