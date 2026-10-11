"""End-to-end smoke test of the whole app with a stubbed Streamlit.

The real suite needs streamlit/pandas/plotly, which cannot be installed in this
sandbox. This drives every screen and every open chapter through a recording
stub, which catches import errors, missing data keys and bad values.
"""
import sys
import types
from pathlib import Path

_DELEGATED = set()


class _Ctx:
    """Stands in for Streamlit's DeltaGenerator: a column or a container."""

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def __getattr__(self, name):
        owner = globals().get("st")
        target = getattr(owner, name, None) if owner is not None else None
        if target is not None and name in _DELEGATED:
            return target
        return lambda *a, **k: _Ctx()


def _trace(*args, **kwargs):
    return dict(kwargs, **{"_args": args})


class _Figure:
    def __init__(self, data=None):
        self.traces = list(data or [])

    def add_trace(self, t):
        self.traces.append(t)

    def add_hline(self, **k):
        self.traces.append(("hline", k))

    def add_vline(self, **k):
        self.traces.append(("vline", k))

    def update_layout(self, **k):
        self.layout = k

    def update_xaxes(self, **k):
        pass

    def update_yaxes(self, **k):
        pass


class _GO:
    Figure = _Figure
    Scatter = _trace
    Bar = _trace
    Layout = _trace

    def __getattr__(self, n):
        return lambda **k: _trace(**k)


go = _GO()
pandas = types.ModuleType("pandas")
pandas.DataFrame = lambda rows=None, **k: list(rows or [])
pandas.__getattr__ = lambda n: (lambda *a, **k: []) if n[0].isupper() else _Ctx()
plotly = types.ModuleType("plotly")
plotly.graph_objects = go

st = types.ModuleType("streamlit")
st.session_state = {}
def _tabs(labels=None, **k):
    # st.tabs() receives the station labels, so this is the exact place the
    # ch08-10 surrogate bug used to surface. Encode each label as Streamlit does.
    return [_Ctx() for label in (labels or ["a"]) if _utf8_ok(label)]


def _utf8_ok(label):
    label.encode("utf-8")
    return True


st.tabs = _tabs
st.columns = lambda spec=1, **k: [
    _Ctx() for _ in range(spec if isinstance(spec, int) else len(spec))]


def _selectbox(label=None, options=None, index=0, **k):
    return (options or [None])[index or 0]


def _radio(label=None, options=None, index=0, **k):
    return (options or [None])[index or 0]


def _multiselect(label=None, options=None, default=None, **k):
    return list(default or [])


def _slider(label=None, min=None, max=None, value=None, step=None, **k):
    return value if value is not None else min


def _number_input(label=None, min=None, max=None, value=None, step=None, **k):
    if isinstance(value, (int, float)):
        return value
    if value is not None:
        return 10.0
    return min if min is not None else 0.0


def _checkbox(label=None, value=False, **k):
    return value


def _text_input(label=None, value="", **k):
    return value


def _button(label=None, **k):
    return False


for name, fn in [("selectbox", _selectbox), ("radio", _radio),
                 ("multiselect", _multiselect), ("slider", _slider),
                 ("number_input", _number_input), ("checkbox", _checkbox),
                 ("text_input", _text_input), ("button", _button),
                 ("chat_input", lambda *a, **k: None)]:
    setattr(st, name, fn)

def _utf8_probe(*args, **kwargs):
    """Force every string through the same encode Streamlit performs.

    Streamlit serialises element text to UTF-8, so a lone surrogate in any
    string raises UnicodeEncodeError there and nowhere else. A stub that merely
    swallows the string will happily render all 124 stations while the real app
    is broken, which is exactly what happened once. Encoding here makes the
    stub fail for the same reason and at the same moment as the real thing.
    """
    for value in list(args) + list(kwargs.values()):
        if isinstance(value, str):
            value.encode("utf-8")
        elif isinstance(value, (list, tuple)):
            for item in value:
                if isinstance(item, str):
                    item.encode("utf-8")
    return _Ctx()


for name in ("markdown", "write", "dataframe", "plotly_chart", "expander", "latex",
             "metric", "image", "code", "info", "success", "error", "warning",
             "caption", "subheader", "header", "divider", "set_page_config",
             "chat_message", "rerun", "text_area", "json", "progress",
             "toggle", "file_uploader", "download_button"):
    setattr(st, name, _utf8_probe)

_CALLS = {}


def _fragment(func=None, *, run_every=None):
    """Stand-in for st.fragment: records the call, returns the original function."""
    def wrap(f):
        _CALLS.setdefault("fragments", 0)
        _CALLS["fragments"] += 1
        return f
    return wrap(func) if func is not None else wrap


def _cache_data(func=None, *, show_spinner=False, **kw):
    """Stand-in for st.cache_data: memoises by args so the decorator is exercised."""
    _CALLS.setdefault("cache_hits", 0)
    _CALLS.setdefault("cache_calls", 0)

    def wrap(f):
        store = {}

        def memo(*a, **k):
            _CALLS["cache_calls"] += 1
            key = (a, tuple(sorted(k.items())))
            try:
                hit = key in store
            except TypeError:
                key = repr(key)
                hit = key in store
            if hit:
                _CALLS["cache_hits"] += 1
                return store[key]
            store[key] = f(*a, **k)
            return store[key]

        memo.__name__ = getattr(f, "__name__", "memo")
        memo.__qualname__ = getattr(f, "__qualname__", "memo")
        memo.__module__ = getattr(f, "__module__", __name__)
        memo.clear = store.clear
        return memo

    return wrap(func) if func is not None else wrap


st.cache_data = _cache_data
st.fragment = _fragment

_DELEGATED.update({"number_input", "slider", "selectbox", "radio", "multiselect",
                   "checkbox", "text_input", "button", "markdown", "write", "info",
                   "success", "error", "warning", "caption", "subheader", "dataframe",
                   "plotly_chart", "expander", "latex", "metric", "image", "code",
                   "chat_input"})

sys.modules["streamlit"] = st
sys.modules["pandas"] = pandas
sys.modules["plotly"] = plotly
sys.modules["plotly.graph_objects"] = go

sys.path.insert(0, ".")
from physics import ai_tutor, curriculum, engine  # noqa: E402

failures = []
built = [c["number"] for c in curriculum.CHAPTERS if c["available"]]
print(f"chapters open: {built}\n")

for slot in curriculum.chapter_slots():
    n = slot["number"]
    if not slot["available"]:
        print(f"  Chapter {n:2d}  LOCKED")
        continue
    try:
        ui = curriculum.chapter_ui(n)
        engine.render(ui.SPEC)
        engine.exit_report(ui.SPEC)
        print(f"  Chapter {n:2d}  {ui.station_count():2d} stations, "
              f"{slot['slo_count']:2d} outcomes  OK")
    except Exception:
        failures.append(n)
        print(f"  Chapter {n:2d}  FAILED")
        import traceback
        traceback.print_exc()

print("\n--- tutor ---")
for n in built:
    prompts = ai_tutor.suggestions(n)
    unanswered = [p for p in prompts if "I do not know that one" in ai_tutor.answer(p, n)]
    print(f"  Chapter {n:2d}: {len(prompts)} prompts, {len(unanswered)} unanswered")
    if unanswered:
        failures.append(n)

print("\n--- caching / fragments ---")
print(f"  @cache_data decorator applied and exercised: {_CALLS['cache_calls']} calls, "
      f"{_CALLS['cache_hits']} served from cache")
print(f"  @fragment  decorations created:                {_CALLS['fragments']}")

print("\n--- app shell (each screen, executed for real) ---")
# The app's router is a module-level statement, so every function it can reach
# must already be defined by the time it runs. Executing each screen against the
# stub catches a helper defined *below* the router, which renders fine in a linter
# and explodes with a NameError in the browser.
import runpy
import streamlit as st

_APP = str(Path(__file__).resolve().parent.parent / "streamlit_app.py")
for view in ("chapters", "chapter", "report"):
    st.session_state.clear()
    st.session_state["view"] = view
    st.session_state["active_chapter"] = len(curriculum.CHAPTERS)
    try:
        runpy.run_path(_APP, run_name="__main__")
        print(f"  view={view:10s} OK")
    except Exception as exc:
        failures.append(view)
        print(f"  view={view:10s} FAILED -> {type(exc).__name__}: {exc}")

print("\nFAILURES:", failures or "none")
sys.exit(1 if failures else 0)