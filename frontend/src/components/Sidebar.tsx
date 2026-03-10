import React from "react"
export default function Sidebar(){
    return (
        <div className="sidebar">
            <div className="text">
                <h2>AIMe</h2>
                <p>
                    AIMe is an AI assistant trained on my engineering projects and professional experience.
                </p>
            </div>
            <div className="links">
                <a href="https://linkedin.com/in/frida-cardona-810858202" target="_blank">
                    View my LinkedIn
                </a>
                <a href="https://github.com/fridacardonae-hash" target="_blank">
                    View my GitHub
                </a>
                <a href="/frida_cardona_resume.pdf" download>
                    Download my resume
                </a>
            </div>
        </div>
    )
}