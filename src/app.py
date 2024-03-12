#import streamlit as st
#from io import StringIO, BytesIO
#from PIL import Image


#st.header("Text Extraction\nFrom Image")

#types = ['jpg', 'png', 'jpeg']

#uploaded_file = st.file_uploader("Upload image file", type=types)

#image_content = None
#flag = False
#image = st.empty()

# if uploaded_file is not None:
#    st.write(f"Uploaded file name: {uploaded_file.name}")
#    image.image(uploaded_file)
#    image_content = uploaded_file.getvalue()
#    st.write(type(image_content))
#    flag = True

# if flag:
#    image = Image.open(uploaded_file)
# ----------------------------------------------------------------------------------------


import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
import gtts
from ocr import add_space



# title
st.title("Extract Text from Images")

# subtitle
#st.markdown("## Text Extraction From Image")

st.markdown("")

# image uploader
image = st.file_uploader(label="Upload your image here",
                         type=['png', 'jpg', 'jpeg'])

@st.cache
def load_model():
    reader = ocr.Reader(
                        ['en'],
                        model_storage_directory='.',
                        gpu=False
                        )
    return reader

# load model
reader = load_model()  
final_text = None
if image is not None:
    # read image
    input_image = Image.open(image) 
    # display image
    st.image(input_image) 

    # Run spinner while extracting text.
    with st.spinner("🤖 AI is at Work! "): 
        result = reader.readtext(np.array(input_image))
        # empty list for results
        result_text = []  

        for text in result:
            result_text.append(text[1])
        final_text = ' '.join(result_text)
        final_text = add_space(final_text)
        st.success("Here you go! Below is the extracted text👇🏻")
        st.code(final_text, language=None)
        image_file_name = image.name if image.name else st.empty()
        st.download_button(
            label="Download the converted text as text file!",
            data=final_text,
            file_name="extracte txt"
        )
    # Text to Audio part......................................................................
    # Supporting variables
    form_holder = st.empty()
    yes_text = "Yes, I want to hear the audio of the text as well."
    no_text = "No, I'm good."
    with form_holder.form("Need audio"):
        st.write("Text to Audio")

        audio_required = st.radio("Want to hear the audio of the text as well?", 
            (yes_text, no_text))

        # Every form must have a submit button.
        with st.spinner("🔊Preparing the audio.."):# Run spinner while converting text to speech.
            
            submitted = st.form_submit_button("Submit")
            #form_holder.empty()
            if submitted and audio_required == yes_text:
                tts = gtts.gTTS(final_text)
                audio_file_name = "my_audio.mp3"
                tts.save(audio_file_name)
                with open(audio_file_name, 'rb') as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3')
        #else:
        #    form_holder.empty()
else:
    st.write("Upload an Image")



st.caption("Made with ❤️ by @TeamRamuKaka")
