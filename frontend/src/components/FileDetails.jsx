import React, { useState } from 'react'

export default function FileDetails() {
  const [selectedFile, setSelectedFile] = useState(null)

  return (
    <div>
      <h3>Selected File</h3>
      {selectedFile ? (
        <div>
          <pre>{selectedFile.content}</pre>
        </div>
      ) : (
        <p>Select a file from the graph</p>
      )}
    </div>
  )
}

