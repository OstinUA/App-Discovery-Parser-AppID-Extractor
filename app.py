import streamlit as st
import requests
from requests.exceptions import RequestException
from parser_logic import extract_google_play_ids, extract_app_store_ids, get_page_title
from translations import LOCALIZATION

st.set_page_config(page_title="App Discovery Parser", layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if 'sources' not in st.session_state:
    st.session_state.sources = [{"type": "HTML", "content": ""}]

with st.sidebar:
    lang = st.selectbox("Language", options=list(LOCALIZATION.keys()))
    t = LOCALIZATION[lang]
    st.divider()
    st.subheader(t["sidebar_info"])
    st.write(t["instr_text"])

st.markdown(f'<div class="main-header">{t["title"]}</div>', unsafe_allow_html=True)

for i in range(len(st.session_state.sources)):
    source_data = st.session_state.sources[i]
    
    # Определение заголовка окна
    display_name = f"{t['source_name']} #{i+1}"
    if source_data["type"] == "URL" and source_data["content"]:
        display_name = source_data["content"]
    elif source_data["type"] == "HTML" and source_data["content"]:
        extracted_title = get_page_title(source_data["content"])
        if extracted_title:
            display_name = extracted_title

    with st.expander(display_name, expanded=(i == len(st.session_state.sources) - 1)):
        col_m, col_v, col_del = st.columns([1, 4, 0.5])
        
        with col_m:
            m_options = [t["mode_html"], t["mode_url"]]
            curr_idx = 0 if source_data["type"] == "HTML" else 1
            mode_choice = st.radio(f"Mode #{i}", m_options, index=curr_idx, key=f"m_{i}", label_visibility="collapsed")
            st.session_state.sources[i]["type"] = "HTML" if mode_choice == t["mode_html"] else "URL"

        with col_v:
            if st.session_state.sources[i]["type"] == "HTML":
                st.session_state.sources[i]["content"] = st.text_area(t["input_label"], value=source_data["content"], key=f"t_{i}", height=100, label_visibility="collapsed")
            else:
                st.session_state.sources[i]["content"] = st.text_input(t["url_label"], value=source_data["content"], key=f"u_{i}", label_visibility="collapsed")
        
        with col_del:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.sources.pop(i)
                st.rerun()

if st.button(f"➕ {t['btn_add']}"):
    st.session_state.sources.append({"type": "HTML", "content": ""})
    st.rerun()

st.divider()

cp1, cp2, _ = st.columns([1, 1, 4])
with cp1:
    parse_btn = st.button(t["btn_parse"], type="primary")
with cp2:
    if st.button(t["btn_clear"]):
        st.session_state.sources = [{"type": "HTML", "content": ""}]
        st.rerun()

if parse_btn:
    combined_html = ""
    for src in st.session_state.sources:
        if src["type"] == "HTML":
            combined_html += src["content"]
        elif src["type"] == "URL" and src["content"]:
            try:
                r = requests.get(src["content"], timeout=10, headers={"User-Agent": "Mozilla/5.0"})
                if r.status_code == 200:
                    combined_html += r.text
            except RequestException as e:
                st.error(f"{t['url_error']}: {src['content']} - {e}")

    gp = extract_google_play_ids(combined_html)
    as_ids = extract_app_store_ids(combined_html)

    r1, r2 = st.columns(2)
    with r1:
        st.markdown(f'<div class="stat-label">{t["gp_header"]}</div>', unsafe_allow_html=True)
        st.metric(t["found"], len(gp))
        st.text_area("GP", value="\n".join(gp), height=200, key="res_gp")
        st.download_button(t["download"], "\n".join(gp), file_name="gp.txt", key="dl_gp")
    with r2:
        st.markdown(f'<div class="stat-label">{t["as_header"]}</div>', unsafe_allow_html=True)
        st.metric(t["found"], len(as_ids))
        st.text_area("AS", value="\n".join(as_ids), height=200, key="res_as")
        st.download_button(t["download"], "\n".join(as_ids), file_name="as.txt", key="dl_as")
