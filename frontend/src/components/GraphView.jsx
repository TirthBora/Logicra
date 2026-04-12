import React, { useEffect, useState } from "react";
import ReactFlow from "reactflow";
import "reactflow/dist/style.css";

function GraphView() {
  const [edges, setEdges] = useState([]);
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/graph/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        project_path: "D:/Dev_Projects/Logicra/sample_projects/project1"
      })
    })
      .then(res => res.json())
     .then(data => {
  if (!data.nodes || !data.edges) {
    console.error("Invalid response:", data);
    return;
  }

  const formattedNodes = data.nodes.map((n, i) => ({
    id: n.id,
    data: { label: n.label },
    position: { x: i * 200, y: 100 }
  }));

  const formattedEdges = data.edges.map((e, i) => ({
    id: "e" + i,
    source: e.source,
    target: e.target
  }));

  setNodes(formattedNodes);
  setEdges(formattedEdges);
});
  }, []);

  return (
    <div style={{ width: "100%", height: "100vh" }}>
      <ReactFlow nodes={nodes} edges={edges} fitView />
    </div>
  );
}

export default GraphView;