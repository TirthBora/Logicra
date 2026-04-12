def build_graph(dependancy_map):
    nodes=[]
    edges=[]

    file_set = set(dependancy_map.keys())

    for file in dependancy_map:
        nodes.append({
            "id":file,
            "label": file})
    name_map={}
    for file in file_set:
        normalized=file.replace("\\","/")
        base=normalized.split("/")[-1]
        name=base.split(".")[0]

        if name not in name_map:
            name_map[name]=[]
        name_map[name].append(file)

    def resolve_import(import_name):
        if not import_name:
            return None
        import_name = import_name.replace("\\", "/")
        import_name = import_name.split("/")[-1]
        import_name = import_name.split(".")[0]

        if import_name in file_set:
            return import_name
        matches=name_map.get(import_name)
        if matches:
            return matches[0]
        return None
    for file,data in dependancy_map.items():
        imports=data.get("imports",[])
        lang=data.get("language","unknown")

        for imp in imports:
            target=resolve_import(imp)

            if target:
                
                edges.append({
                    "source":file,
                    "target":target,
                    "type" :lang
                })
    return {
        "nodes":nodes,
        "edges":edges}
