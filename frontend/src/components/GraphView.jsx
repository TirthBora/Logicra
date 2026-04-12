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
        console.log(data);

        if (!data.nodes || !data.edges) {
          console.error("Invalid response:", data);
          return;
        }

        const formattedNodes = data.nodes.map((n, i) => {
          const id = n.id.replaceAll("\\", "/"); // extract full path as id
          const label = n.label;
          return {
            id: id,
            data: { label: n.label },
            position: {x: (i % 3) * 250,  y: Math.floor(i / 3) * 150 },
            style: {
              background: "#1e293b",
              color: "#fff",
              border: "1px solid #334155",
              borderRadius: "8px",
              padding: "10px",
            },
          };
        });

        const formattedEdges = data.edges.map((e, index) => {
          return {
            id: `${e.source}-${e.target}-${index}`,
            source: e.source.replaceAll("\\", "/"),
            target: e.target.replaceAll("\\", "/"),
            style: {
              stroke: "#38bdf8",
              strokeWidth: 3,
            },
            type: "smoothstep",
            animated: true,
          };
        });
        setNodes(formattedNodes);
        setEdges(formattedEdges);
      });
  }, []);

  console.log(nodes);
  console.log(edges);

  return (
    <div style={{ width: "100vw", height: "100vh", background: "#0f172a" }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
        fitViewOptions={{ padding: 2}}
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
