import React from 'react'

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="container">
        <div style={{fontSize: '1.5rem', fontWeight: 'bold'}}>
          Logicra
        </div>
        <div style={{display: 'flex', gap: '1rem'}}>
          <a href="/" style={{color: 'white', textDecoration: 'none'}}>Home</a>
          <a href="/graph" style={{color: 'white', textDecoration: 'none'}}>CodeMap</a>
          <a href="/clones" style={{color: 'white', textDecoration: 'none'}}>Clones</a>
        </div>
      </div>
    </nav>
  )
}
