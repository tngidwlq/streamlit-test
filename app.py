import streamlit as st

st.set_page_config(
    page_title="ddasik's Test Streamlit",
    page_icon="👋",
)

st.write("# Welcome to DDasik's Test Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    안녕하세요! 🎉 DDasik의 스트림릿 놀이터에 오신 걸 환영합니다!
    
    여기서는 데이터 사이언스와 머신러닝의 마법을 경험할 수 있어요! ✨
    
    **👈 사이드바에서 데모를 선택해서** 스트림릿의 놀라운 기능들을 체험해보세요!
    
    ### 🚀 더 알아보고 싶다면?
    - [streamlit.io](https://streamlit.io)에서 더 많은 정보를 확인하세요
    - [공식 문서](https://docs.streamlit.io)로 깊이 있게 공부해보세요
    - [커뮤니티 포럼](https://discuss.streamlit.io)에서 궁금한 걸 물어보세요
    
    ### 🎯 멋진 데모들도 구경하세요!
    - [자율주행차 이미지 분석](https://github.com/streamlit/demo-self-driving) - 신경망으로 분석해요!
    - [뉴욕시 우버 데이터 탐색](https://github.com/streamlit/demo-uber-nyc-pickups) - 데이터 시각화의 진수!
    
    🎊 준비되셨나요? 함께 데이터의 세계로 떠나볼까요!
"""
)