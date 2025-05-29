import streamlit as st


from Linked import LinkedList


st.title("링크드 리스트 구현하기")
st.write("링크드 리스트 구현를 시각화")


if 'linked_list' not in st.session_state:
    st.session_state.linked_list = LinkedList()


st.sidebar.header("링크드 리스트 데이터 삽입")




st.sidebar.text_input("데이터 입력", key="data_input_val")




col1, col2, col3 = st.sidebar.columns(3)




def append_data_callback():
    if st.session_state.data_input_val:
        st.session_state.linked_list.append(st.session_state.data_input_val)
        st.session_state.data_input_val = ''
    else:
        st.sidebar.warning("추가할 데이터 입력")


def prepend_data_callback():
    if st.session_state.data_input_val:
        st.session_state.linked_list.prepend(st.session_state.data_input_val)
        st.session_state.data_input_val = ''
    else:
        st.sidebar.warning("추가할 데이터 입력")

def remove_data_callback():
    if st.session_state.data_input_val:
        st.session_state.linked_list.delete(st.session_state.data_input_val)
        st.session_state.data_input_val = ''
    else:
        st.sidebar.warning("추가할 데이터 입력")


with col1:
    st.button("append", on_click=append_data_callback ,use_container_width=True)

with col2:
    st.button("prepend",on_click=prepend_data_callback,use_container_width=True)

with col3:
    st.button("remove",on_click=remove_data_callback,use_container_width=True)


st.markdown("-----")
st.subheader("연결리스트 출력")


list_display = st.empty()


result = st.session_state.linked_list.display()


list_display.markdown(f"{result}")