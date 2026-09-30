import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    st.markdown(
        """
        <style>
        .cv-subject-card {
            background:#fff; border:1px solid #e3e9e2; border-left:4px solid #286b57;
            padding:20px 22px 16px; border-radius:14px; margin:0 0 14px;
            box-shadow:0 3px 12px #263c2f08;
        }
        .cv-subject-card h3 { margin:0; color:#1a2b3a; font:750 18px 'Manrope',sans-serif; }
        .cv-subject-meta { color:#708078; margin:8px 0 13px; font:13px 'DM Sans',sans-serif; }
        .cv-subject-code { background:#eaf3ed; color:#286b57; padding:3px 8px; border-radius:6px; font-weight:700; }
        .cv-subject-stats { display:flex; gap:8px; flex-wrap:wrap; }
        .cv-subject-stat { background:#f3f7f2; padding:7px 11px; border-radius:9px; color:#53645b; font:12px 'DM Sans',sans-serif; }
        .cv-subject-stat b { color:#1a2b3a; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    html = f"""
        <div class="cv-subject-card">
            <h3>{name}</h3>
            <div class="cv-subject-meta">Code <span class="cv-subject-code">{code}</span> &nbsp;·&nbsp; Section {section}</div>
    """

    if stats:
        html += '<div class="cv-subject-stats">'
        for icon, label, value in stats:
            html += f'<div class="cv-subject-stat">{icon} &nbsp;<b>{value}</b> {label}</div>'
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
