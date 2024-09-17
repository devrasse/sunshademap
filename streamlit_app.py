import streamlit as st
from streamlit_lottie import st_lottie
import json
import asyncio

async def load_data():
    # 데이터를 읽어오는 작업을 시뮬레이션합니다.
    await asyncio.sleep(1)  # 1초 동안 대기
    with open("sunshademap.html", "r", encoding="utf-8") as f:
        return f.read()

async def main():
    st.set_page_config(layout="wide")

    st.markdown('<div class="centered"><h1 style="text-align:center;"> 미추홀구 그늘막 </h1></div>', unsafe_allow_html=True)
    
    with open("lottiefiles/loading.json", "r") as f:
        lottie_loading = json.load(f)

    loading_state = st.empty()
    
    with loading_state.container():
        with st.spinner('데이터 읽어오는 중...'):
            lottie_placeholder = st.empty()
            lottie_placeholder.markdown(
                f'<div id="lottie-container" style="width:100%;height:300px;"></div>',
                unsafe_allow_html=True
            )
            st_lottie(lottie_loading, key="lottie", height=300)
            
            # 비동기적으로 데이터를 로드합니다.
            html_code = await load_data()
    
    loading_state.empty()
    
    with st.container(border=True, height=740):
        # Streamlit 앱에 HTML 표시
        st.components.v1.html(html_code, height=700, scrolling=False)

if __name__ == "__main__":
    asyncio.run(main())
