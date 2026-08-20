import os
from dotenv import load_dotenv

load_dotenv()
print("Main Key:", os.getenv("GROQ_API_KEY")[:15] + "...")
print("Main.py API Key:", os.getenv("GROQ_API_KEY"))
import streamlit as st
from prompt_based import PromptBasedLearning
from post_generator import generate_post


def main():
    st.title("X Post Generator")

    try:
        # Create PromptBasedLearning object
        pb = PromptBasedLearning()

        # Display sample filtered posts
       # posts = pb.get_filtered_posts(
        #    "Short",
         #   "English",
          #  "Ai"
        #)
        #st.write("Sample Posts:")
        #st.write(posts)

    except Exception as e:
        st.error(f"Error creating PromptBasedLearning instance: {e}")
        return

    # Create three columns
    col1, col2, col3 = st.columns(3)

    # Tag selection
    with col1:
        selected_tag = st.selectbox(
            "Tag",
            options=pb.get_tags()
        )

    # Length selection
    with col2:
        length_options = ["Short", "Medium", "Long"]
        selected_length = st.selectbox(
            "Length",
            options=length_options
        )

    # Language selection
    with col3:
        language_options = ["English"]
        selected_language = st.selectbox(
            "Language",
            options=language_options
        )

    # Generate button
    if st.button("Generate"):
        try:
            post = generate_post(
                selected_length,
                selected_language,
                selected_tag
            )
            st.subheader("Generated Post")
            st.write(post)

        
        except Exception:
                import traceback
                st.code(traceback.format_exc())


if __name__ == "__main__":
    main()