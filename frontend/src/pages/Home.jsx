import React, { useState } from 'react'
import GraphView from '../components/GraphView.jsx'
import CloneViewer from '../components/CloneViewer.jsx'
import FileDetails from '../components/FileDetails.jsx'

export default function Home() {
  const [activeTab, setActiveTab] = useState('graph')
  const [projectPath, setProjectPath] = useState('')

  return (
    <div className="container">
      <div className="card">
        <h1>🚀 Logicra - Code Intelligence</h1>
        <p>Analyze your codebase with AI-powered insights</p>
        
        <div style={{marginTop: '2rem'}}>
          <input 
            type="text" 
            placeholder="Enter project path (e.g., sample_projects/project1)"
            value={projectPath}
            onChange={(e) => setProjectPath(e.target.value)}
            style={{padding: '0.75rem', width: '300px', marginRight: '1rem'}}
          />
          <button className="btn" onClick={() => console.log('Analyze:', projectPath)}>
            Analyze Project
          </button>
        </div>
      </div>

      <div className="grid">
        <div className="card">
          <h2>CodeMap</h2>
          <GraphView />
        </div>
        <div className="card">
          <h2>Code Clones</h2>
          <CloneViewer />
        </div>
        <div className="card">
          <h2>File Details</h2>
          <FileDetails />
        </div>
      </div>
    </div>
  )
}

