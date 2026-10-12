"""Give every ID-registering Streamlit element a unique key.

Streamlit computes an element's internal ID from its type plus its parameters.
Two `st.dataframe(df, use_container_width=True, hide_index=True)` calls in one
render therefore share an ID, and the second raises
StreamlitDuplicateElementId - which aborts the whole station, not just the table.

The key is derived from the enclosing function and a counter, so it is stable
across reruns (so widget state survives) and unique within a chapter (so the IDs
never collide).
"""
import ast, pathlib, re

TARGETS = {"st.dataframe", "st.plotly_chart", "st.tabs"}

for path in sorted(pathlib.Path("physics").rglob("*.py")):
    src = path.read_text()
    tree = ast.parse(src)
    edits = []
    for fn in ast.walk(tree):
        if not isinstance(fn, ast.FunctionDef):
            continue
        counter = {}
        for node in ast.walk(fn):
            if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and ast.unparse(node.func) in TARGETS):
                continue
            if any(kw.arg == "key" for kw in node.keywords):
                continue
            kind = node.func.attr
            counter[kind] = counter.get(kind, 0) + 1
            key = f"k_{fn.name}_{kind}{counter[kind]}"
            # insert just before the closing paren of this call
            seg = ast.get_source_segment(src, node)
            close = seg.rindex(")")
            edits.append((node.end_col_offset - 1, node.lineno, key, close))
        # only build keys when needed
    if not edits:
        continue
    lines = src.split("\n")
    # apply per line, right to left
    by_line = {}
    for endcol, lineno, key, close in edits:
        by_line.setdefault(lineno, []).append((endcol, key))
    for lineno, items in by_line.items():
        line = lines[lineno - 1]
        for endcol, key in sorted(items, reverse=True):
            line = line[:endcol] + f', key="{key}"' + line[endcol:]
        lines[lineno - 1] = line
    out = "\n".join(lines)
    ast.parse(out)
    path.write_text(out)
    print(f"  {path}: {len(edits)} element(s) keyed")
