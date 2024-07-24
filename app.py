import streamlit as st
view = [1,2,3,1,-5,3,12,31,3,2,1,3,3]
view1 = [5,8,3,9,-5,3,1,31,3,2,1,3,3]

# st.set_page_config(
#     page_title="My Custom Streamlit App", # 페이지 제목 설정
#     page_icon="🎈", # 페이지 아이콘 설정 (이모지 사용 가능)
#     layout="centered", # 레이아웃 설정 ("centered" 또는 "wide")
# )

# # 애플리케이션 제목
# st.title("My First Streamlit App")

# # 텍스트 입력
# name = st.text_input("Enter your name:")

# # 버튼 클릭
# if st.button("Submit"):
#     st.write(f"Hello, {name}!")
# else:
#     st.write("Please enter your name and click submit.")
st.line_chart(view1)
st.line_chart(view,color="#ffaa00")