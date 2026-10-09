"""Streamlit presentation helpers for Physics Atlas.

Keeps all custom CSS, card markup and Plotly styling in one place so the
learning content stays readable and the look stays consistent.
"""

from __future__ import annotations

import streamlit as st

TEAL = "#2dd4bf"
CYAN = "#22d3ee"
AMBER = "#fbbf24"
ROSE = "#fb7185"
GREEN = "#34d399"
VIOLET = "#a78bfa"
MUTED = "#94a3b8"
INK = "#e2e8f0"

SEQUENCE_COLORS = [CYAN, TEAL, AMBER, VIOLET, ROSE, GREEN]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
.stApp{
  background:
    radial-gradient(1100px 620px at 8% -8%, #12324f 0%, rgba(9,20,37,0) 55%),
    radial-gradient(900px 520px at 100% 0%, #103a44 0%, rgba(9,20,37,0) 55%),
    linear-gradient(180deg, #081426 0%, #060d1a 60%, #04080f 100%);
  color:#e6eefb;
  font-family:'Sora',system-ui,sans-serif;
}
.block-container{max-width:1240px;padding-top:3.6rem;padding-bottom:3rem}
[data-testid="stHeader"]{background:transparent;height:2.2rem}
[data-testid="stToolbar"]{right:1rem}
[data-testid="stTabs"]{margin-top:1.1rem;position:relative;z-index:2}
[data-testid="stSidebar"]{background:#07101f;border-right:1px solid #1d3350}
h1,h2,h3{font-weight:800;letter-spacing:-.02em}
h1{font-size:clamp(2rem,3.6vw,3.3rem)!important}
h2{font-size:clamp(1.4rem,2.4vw,2rem)!important}
p,li,label{color:#c6d6ea}
a{color:#5eead4}
[data-testid="stMetric"]{background:linear-gradient(160deg,rgba(20,42,68,.85),rgba(9,20,35,.92));
  border:1px solid #21436a;border-radius:16px;padding:14px}
[data-testid="stMetricValue"]{color:#5eead4;font-weight:800}
[data-testid="stMetricLabel"]{color:#9fb4cc}
.stButton>button,.stDownloadButton>button{
  border:1px solid #2f6f86;background:linear-gradient(100deg,#0f766e,#0e7490);
  color:#f0fdfa;border-radius:12px;font-weight:700}
.stButton>button:hover,.stDownloadButton>button:hover{border-color:#5eead4;color:#ffffff}
[data-testid="stTabs"] button{font-weight:600}
[data-testid="stExpander"]{border:1px solid #1e3a5c;border-radius:14px;background:rgba(10,22,38,.55)}
.code,.mono,code,pre{font-family:'JetBrains Mono',monospace}
.kicker{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#5eead4}
.atlas-card{background:linear-gradient(150deg,rgba(22,46,74,.92),rgba(8,18,32,.96));
  border:1px solid #21436a;border-radius:18px;padding:20px 22px;margin:4px 0 14px}
.atlas-card h3{margin:.15rem 0 .5rem;color:#f1f7ff}
.atlas-card .body{color:#c6d6ea}
.pill{display:inline-block;padding:3px 11px;border-radius:999px;font-size:11px;font-weight:700;
  font-family:'JetBrains Mono',monospace;letter-spacing:.06em;margin:2px 4px 2px 0}
.pill-good{background:rgba(52,211,153,.15);color:#6ee7b7;border:1px solid rgba(52,211,153,.5)}
.pill-bad{background:rgba(251,113,133,.15);color:#fda4af;border:1px solid rgba(251,113,133,.5)}
.pill-info{background:rgba(34,211,238,.14);color:#67e8f9;border:1px solid rgba(34,211,238,.5)}
.pill-warn{background:rgba(251,191,36,.15);color:#fcd34d;border:1px solid rgba(251,191,36,.5)}
.pill-mute{background:rgba(148,163,184,.14);color:#cbd5e1;border:1px solid rgba(148,163,184,.4)}
.chapter-card{background:linear-gradient(150deg,rgba(18,38,62,.9),rgba(8,17,30,.95));
  border:1px solid #1f3c5c;border-radius:18px;padding:18px;min-height:172px;height:100%;
  display:flex;flex-direction:column;justify-content:space-between}
.chapter-card.live{border-color:#2dd4bf;box-shadow:0 0 0 1px rgba(45,212,191,.25),0 12px 34px -18px rgba(45,212,191,.65)}
.chapter-card.locked{opacity:.9}
.chapter-no{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.16em;color:#7dd3fc}
.chapter-title{font-weight:700;font-size:1.05rem;color:#eef6ff;margin:.35rem 0}
.chapter-blurb{color:#a9bdd6;font-size:.86rem}
.hmgood{color:#6ee7b7;font-weight:700}
.hmbad{color:#fda4af;font-weight:700}
div[data-testid="stDataFrame"]{border-radius:12px;overflow:hidden}
hr{border-color:#1c3450}
"""


def inject_css() -> None:
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


def card(title: str, body: str, tag: str = "FIELD NOTE") -> None:
    st.markdown(
        f'<div class="atlas-card"><div class="kicker">{tag}</div>'
        f"<h3>{title}</h3><div class='body'>{body}</div></div>",
        unsafe_allow_html=True,
    )


def pill(text: str, kind: str = "info") -> str:
    return f'<span class="pill pill-{kind}">{text}</span>'


def section_intro(tag: str, title: str, body: str) -> None:
    st.markdown(
        f'<div class="atlas-card"><div class="kicker">{tag}</div>'
        f"<h2>{title}</h2><div class='body'>{body}</div></div>",
        unsafe_allow_html=True,
    )


def style_fig(fig, height: int = 380):
    fig.update_layout(
        height=height,
        margin=dict(l=14, r=16, t=42, b=16),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(7,16,30,.6)",
        font=dict(color="#d7e5f7", family="Sora, sans-serif"),
        legend=dict(orientation="h", y=1.12, x=0),
        hovermode="closest",
        title_font=dict(color="#eef6ff"),
    )
    fig.update_xaxes(gridcolor="#18304b", zerolinecolor="#24486e")
    fig.update_yaxes(gridcolor="#18304b", zerolinecolor="#24486e")
    return fig


def metric_row(items: list[tuple[str, str]]) -> None:
    columns = st.columns(len(items))
    for column, (label, value) in zip(columns, items):
        column.metric(label, value)
