import streamlit as st

def main():
    st.set_page_config(page_title="Intelligent Document Query System", page_icon=":books:")

    st.header(":books: Intelligent Document Query System :books:")
    st.text_input("Ask a question about the documents")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upoad your PDFs here and click on 'Process'")
        st.button("Process")



if __name__ == "__main__":
    main()