import React from "react"
type Props = {
    text: string
    role: "user" | "ai"
}

export default function Message({ text, role }:Props){
    return (
        <div className={`message ${role}`}>
            {text}
        </div>
    )
}