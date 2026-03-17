import React from "react"
import { useState, useRef, useEffect } from "react"
import Message from "./Message"



export default function Chat() {


  const [messages, setMessages] = useState<any[]>([])
  const [question, setQuestion] = useState("")

  const messagesEndRef = useRef<HTMLDivElement | null>(null)
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [messages])

  const API_URL = "https://aime-backend.victoriousmoss-666ea086.centralus.azurecontainerapps.io"
  const askAIMe = async () => {

    const userMessage = { role: "user", text: question }
    setMessages(prev => [...prev, userMessage])
    setQuestion("")

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

  }

  return (
    <div className="chat">

      <div className="messages">
        
        {messages.map((m, i) => (
          <Message key={i} text={m.text} role={m.role} />
        ))}
        <div ref={messagesEndRef}/>
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