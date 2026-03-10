import React, { useState } from "react"
import Sidebar from "./components/Sidebar"
import Chat from "./components/Chat"
import "./styles.css"

export default function App(){

  const [open,setOpen]=useState(true)

  return(
    <div className="layout">

      <div className={`sidebar-wrapper ${open ? "open" : "closed"}`}>
        <Sidebar/>
      </div>

      <Chat/>

      <button
        className="toggle"
        onClick={()=>setOpen(!open)}
      >
        ☰
      </button>

    </div>
  )
}