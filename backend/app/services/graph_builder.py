def build_graph(dependancy_map):
    nodes=[]
    edges=[]

    file_set=set(dependancy_map.key())

    for file in dependancy_map:
        nodes.append({
            "id":file,
            "label": file})
        
    def resolve_import(import_name):
        if import_name in file_set:
            return import_name
        
        possible=import_name+".py"
        if possible in file_set:
            return possible
        
        for file in file_set:
            if file.startswith(import_name):
                return file 
        return None
    for file,data in dependancy_map.items():
        imports=data.get("imports",[])

        for imp in imports:
            target=resolve_import(imp)

            if target:
                edges.append({
                    "source":file,
                    "target":target
                })
    return {
        "nodes":nodes,
        "edges":edges}
