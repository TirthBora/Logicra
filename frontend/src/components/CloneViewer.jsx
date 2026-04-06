import React from 'react'

export default function CloneViewer() {
  const clones = [
    { file1: 'utils.py', file2: 'helper.py', similarity: 0.92 }
  ]

  return (
    <div>
      <h3>Code Clones Found</h3>
      {clones.map((clone, idx) => (
        <div key={idx} className="card" style={{marginBottom: '1rem'}}>
          <div>{clone.file1} ↔ {clone.file2}</div>
          <div>Similarity: {(clone.similarity * 100).toFixed(1)}%</div>
        </div>
      ))}
      {clones.length === 0 && <p>No clones detected</p>}
    </div>
  )
}

