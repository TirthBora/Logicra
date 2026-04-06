import React, { useState } from 'react'

export default function ErrorBox() {
  const [errorText, setErrorText] = useState('')
  const [explanation, setExplanation] = useState('')

  const handleAnalyze = () => {
    // TODO: Call error translation API
    setExplanation('AI-powered error explanation will appear here')
  }

  return (
    <div>
      <textarea
        placeholder="Paste your error here..."
        value={errorText}
        onChange={(e) => setErrorText(e.target.value)}
        rows={4}
        style={{width: '100%', marginBottom: '1rem'}}
      />
      <button className="btn" onClick={handleAnalyze}>
        Translate Error
      </button>
      {explanation && (
        <div className="card" style={{marginTop: '1rem'}}>
          <h4>Explanation:</h4>
          <p>{explanation}</p>
        </div>
      )}
    </div>
  )
}

