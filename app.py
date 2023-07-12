import streamlit as st
from transformers import T5ForConditionalGeneration,T5Tokenizer
from streamlit_option_menu import option_menu
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        

    }}
    </style>
    """,
    unsafe_allow_html=True
    )


@st.cache_resource()
def generate_summary(input_text):
    
    # Load the T5 model and tokenizer
    model_name = 't5-base'
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    tokenizer = T5Tokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer([input_text], truncation=True, padding='longest', max_length=512, return_tensors='pt')

    # Generate the summary
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, length_penalty=2.0)

    # Decode the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary



def main():
    


    add_bg_from_local('D:\Text Summarizer\image.png')
    choice = option_menu(

        menu_title=None,
        options=["Home","About","Summarize"],
        icons=['house','info-circle','file-text'],
        menu_icon=['cast'],
        default_index=0,
        orientation="horizontal",

        styles={
        "container": {"padding": "0!important"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(238, 238, 238, 0.2)"},
        "nav-link-selected": {"background-color": "green"},
    }
    )

    # Display the selected page content
    if choice == "Home":
        # Introduction to Text Summarization
        st.header("Introduction to Text Summarization")
        st.write("Text summarization is the process of distilling the key information from a text document to produce a shorter version while retaining its main ideas.")
        st.write("It plays a crucial role in information retrieval, allowing users to quickly grasp the essence of lengthy documents.")

        # How Text Summarization Works
        st.header("How Text Summarization Works")
        st.write("Text summarization can be achieved through two main approaches: extractive and abstractive summarization.")
        st.subheader("Extractive Summarization")
        st.write("Extractive summarization involves identifying the most important sentences or phrases from the original text and assembling them to form a summary.")
        st.write("This approach relies on statistical methods, natural language processing techniques, and features like sentence relevance and importance.")
        st.subheader("Abstractive Summarization")
        st.write("Abstractive summarization aims to generate a summary by understanding the meaning of the text and producing a condensed version using natural language generation techniques.")
        st.write("It involves paraphrasing and rephrasing the original text, often using deep learning models and neural networks.")

        # NLP Models for Text Summarization
        st.header("NLP Models for Text Summarization")
        st.write("Various NLP models and techniques are available for text summarization. Some popular models include:")
        st.subheader("1. Transformer-based Models")
        st.write("Transformer-based models, such as BERT (Bidirectional Encoder Representations from Transformers) and GPT (Generative Pre-trained Transformer), have been successfully applied to text summarization tasks.")
        st.write("These models leverage attention mechanisms and large-scale pre-training on vast amounts of text data to generate high-quality summaries.")
        st.subheader("2. Seq2Seq Models")
        st.write("Sequence-to-sequence (Seq2Seq) models, particularly those based on recurrent neural networks (RNNs) and encoder-decoder architectures, have also been used for text summarization.")
        st.write("These models learn to map input sequences to output sequences, allowing them to generate abstractive summaries.")
        st.subheader("3. Transformer-based Reinforcement Learning")
        st.write("Recent research has explored the combination of transformer-based models with reinforcement learning techniques for text summarization.")
        st.write("By using rewards and fine-tuning strategies, these models can further improve the quality and coherence of generated summaries.")
        


    elif choice == "About":
        st.header("About This Project")
        st.write("1. This Text Summarization Project aims to provide an efficient way to summarize large texts, making it easier to grasp the main points and save time.")
        st.write("2. The project utilizes advanced NLP techniques and machine learning models to perform text summarization.")
        st.write("3. By leveraging these techniques, the project aims to generate accurate and meaningful summaries that capture the essence of the original text.")
        st.write("4. The summarization process is powered by transformer-based models, specifically the T5 model, which is fine-tuned for the task of text summarization.")
        st.write("5. Feel free to explore the different summarization techniques and options available.")
        st.write("6. Whether you're a student, researcher, or professional, this Text Summarization Project can assist you in extracting the most important information from large amounts of text.")
        st.write("7. For any feedback or suggestions, please contact us.")

        st.header("Project Features")
        st.write("- Quick and efficient summarization of long texts.")
        st.write("- Easy-to-use interface with real-time summarization results.")

    elif choice == "Summarize":
        st.title("Text Summarization")
        input_text = st.text_area("Enter your text here")
        if st.button("Generate Summary"):
            # Call the generate_summary function
            summary = generate_summary(input_text)
            # Display the summary in the Streamlit app
            st.write("Summary:", summary)

if __name__ == "__main__":
    main()
