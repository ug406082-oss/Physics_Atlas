"""Insert a unique ``key=`` into every ID-registering Streamlit element.

Streamlit computes an element's internal ID from its type plus its parameters,
so two `st.dataframe(df, use_container_width=True, hide_index=True)` calls in
one render share an ID and the second raises StreamlitDuplicateElementId, which
aborts the whole station. `st.plotly_chart` and `st.tabs` behave the same way.

Works by scanning characters and balancing parentheses, so it is immune to the
UTF-8 byte offsets that make an AST-based rewrite misplace the insertion in
files full of "m s^-1".
"""
import re
import pathlib

TARGETS = ("st.dataframe", "st.plotly_chart", "st.tabs")


def key_for(text, pos):
    """A stable key from the enclosing function and a per-function counter."""
    fn = "_"
    for m in re.finditer(r"^def\s+(\w+)\s*\(", text, re.M):
        if m.start() <= pos:
            fn = m.group(1)
    state = key_for._state
    if state[0] is not text:
        state[0], state[1] = text, {}
    table = state[1]
    table[fn] = table.get(fn, 0) + 1
    return f"k_{fn}_{table[fn]}"


key_for._state = [None, {}]


def add_keys(text):
    out = text
    changed = 0
    while True:
        hit = None
        for target in TARGETS:
            for m in re.finditer(re.escape(target) + r"\(", out):
                start = m.end()               # just after the open paren
                depth, i, in_str = 1, start, None
                while depth and i < len(out):
                    c = out[i]
                    if in_str:
                        if c == in_str and out[i - 1] != "\\":
                            in_str = None
                    elif c in "\"'":
                        in_str = c
                    elif c == "(":
                        depth += 1
                    elif c == ")":
                        depth -= 1
                    i += 1
                body = out[start:i - 1]
                if re.search(r"(^|[,\s])key\s*=", body):
                    continue
                key = key_for(out, m.start())
                hit = i - 1
                out = out[:hit] + f', key="{key}"' + out[hit:]
                changed += 1
                break
            if hit is not None:
                break
        if hit is None:
            break
    return out, changed


for path in sorted(pathlib.Path("physics").rglob("*.py")):
    text = path.read_text()
    out, n = add_keys(text)
    if n:
        import ast
        ast.parse(out)
        path.write_text(out)
        print(f"  {path.name}: {n} keyed")
print("done")
