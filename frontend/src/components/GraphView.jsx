import React, { useEffect, useState } from "react";
import ReactFlow, { Background, Controls, MiniMap } from "reactflow";
import "reactflow/dist/style.css";

function GraphView() {
  const [edges, setEdges] = useState([]);
  const [nodes, setNodes] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/graph/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        project_path: "D:/Dev_Projects/Logicra/sample_projects/project1",
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (!data.nodes || !data.edges) {
          console.error("Invalid response:", data);
          return;
        }

        const formattedNodes = data.nodes.map((n, i) => ({
          id: n.id,
          data: { label: n.label },
          position: { x: i * 200, y: 100 },
          style: {
            background: "#1e293b",
            color: "#fff",
            border: "1px solid #334155",
            borderRadius: "8px",
            padding: "10px",
          },
        }));

        const formattedEdges = data.edges.map((e, i) => ({
          id: "e" + i,
          source: e.source,
          target: e.target,
        }));

        setNodes(formattedNodes);
        setEdges(formattedEdges);
      });
  }, []);

  return (
    <div style={{ width: "100vw", height: "100vh", background: "#0f172a" }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
        style={{ background: "#0f172a" }}
      >
        <MiniMap
          nodeColor="#60a5fa"
          maskColor="rgba(0,0,0,0.2)"
          nodeStrokeWidth={3}
        />

        <Controls />
        <Background color="#ccc" gap={20} size={1} />
      </ReactFlow>
    </div>
  );
}

export default GraphView;
