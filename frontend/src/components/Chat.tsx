import React from "react"
import { useState } from "react"
import Message from "./Message"



export default function Chat() {

  const [messages, setMessages] = useState<any[]>([])
  const [question, setQuestion] = useState("")

  const API_URL = import.meta.env.VITE_API_URL 
  const askAIMe = async () => {

    const userMessage = { role: "user", text: question }
    setMessages(prev => [...prev, userMessage])

    const res = await fetch(`${API_URL}/ask`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    })

    const data = await res.json()

    const aiMessage = { role: "ai", text: data.answer }
    setMessages(prev => [...prev, aiMessage])

    setQuestion("")
  }

  return (
    <div className="chat">

      <div className="messages">
        {messages.map((m, i) => (
          <Message key={i} text={m.text} role={m.role} />
        ))}
      </div>

      <div className="input-area">
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask AIMe anything about my experience..."
          onKeyDown={(e)=>{
            if(e.key === "Enter"){
              askAIMe()
            }
          }}
        />

        <button onClick={askAIMe}>
          Send
        </button>
      </div>

    </div>
  )
}