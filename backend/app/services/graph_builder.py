def detect_cycles(edges):
    graph={}
    for e in edges:
        graph.setdefault(e["source"],[]).append(e["target"])

    visited=set()
    stack=set()
    cycles=set()

    def dfs(node,path):
        if node in stack:
            cycles.update(path)
            return
        if node in visited:
            return
        
        visited.add(node)
        stack.add(node)

        for neighbor in graph.get(node,[]):
            dfs(neighbor,path+[neighbor])

        stack.add(node)

        for neighbor in graph.get(node,[]):
            dfs(neighbor,path+[neighbor])

        stack.remove(node)
    for node in graph:
        dfs(node,[node])

    return list(cycles)
def build_graph(dependancy_map):
    nodes = []
    edges = []

    file_set = set(dependancy_map.keys())

    normalized_map = {
        file: file.replace("\\", "/")
        for file in file_set
    }

    for file in dependancy_map:
        nodes.append({
            "id": file,
            "label": file.replace("\\", "/").split("/")[-1]
        })

    name_map = {}
    for file in file_set:
        normalized = normalized_map[file]
        base = normalized.split("/")[-1]
        name = base.split(".")[0]

        if name not in name_map:
            name_map[name] = []
        name_map[name].append(file)
    def resolve_import(import_name, current_file):
        if not import_name:
            return None

        import_name = import_name.replace("\\", "/")
        import_name = import_name.split("/")[-1]
        import_name = import_name.split(".")[0]

        for file in file_set:
            normalized = file.replace("\\", "/")

            if normalized.endswith(f"/{import_name}.py") or normalized.endswith(f"{import_name}.py"):
                return file

        return None
    seen_edges = set()

    for file, data in dependancy_map.items():
        imports = data.get("imports", [])
        lang = data.get("language", "unknown")

        for imp in imports:
            target = resolve_import(imp, file)

            if not target:
                continue
            if target == file:
                continue

            edge_key = (file, target)

            if edge_key in seen_edges:
                continue

            edges.append({
                "source": file,
                "target": target,
                "type": lang
            })

            seen_edges.add(edge_key)
            cycles=detect_cycles(edges)
    return {
        "nodes": nodes,
        "edges": edges,
        "cycles":cycles
    }