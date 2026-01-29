import streamlit as st

st.set_page_config(page_title="Media & Translation App", layout="centered")

# ---------- TITLE ----------
st.title("📱 Media & Translation Application")
st.write("Select what you want to perform")
st.divider()

# ---------- USER CHOICE ----------
option = st.radio(
    "Choose an option:",
    ("Upload Image", "Upload Video", "Text Translation")
)

st.divider()

# ---------- IMAGE SECTION ----------
if option == "Upload Image":
    st.header("🖼 Image Upload")

    image_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    if image_file is not None:
        st.subheader("📤 Output")
        st.image(image_file, caption="Uploaded Image", use_column_width=True)

# ---------- VIDEO SECTION ----------
elif option == "Upload Video":
    st.header("🎥 Video Upload")

    video_file = st.file_uploader(
        "Choose a video",
        type=["mp4", "mov", "avi", "mkv"]
    )

    if video_file is not None:
        st.subheader("📤 Output")
        st.video(video_file)

# ---------- TRANSLATION SECTION ----------
elif option == "Text Translation":
    st.header("🌐 Text Translation")

    input_text = st.text_area("Enter text to translate")

    target_language = st.selectbox(
        "Select target language",
        ["English", "Kannada", "Hindi", "Telugu", "Tamil"]
    )

    if st.button("Translate"):
        if input_text.strip() == "":
            st.warning("Please enter some text")
        else:
            st.subheader("📤 Output")
            translated_text = f"[{target_language}] Translation of: {input_text}"
            st.success("Translated Text")
            st.text_area("Output", translated_text, height=120)

st.caption("Frontend-only UI | Backend logic can be added later")
