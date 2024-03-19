import time
import os
import json
import openai
import streamlit as st
from streamlit_lottie import st_lottie
from tenacity import retry, stop_after_attempt, wait_random_exponential

def main():
    set_page_config()
    custom_css()
    hide_elements()
    sidebar()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity",
        layout="wide",
        page_icon="img/logo.png"
    )

def custom_css():
    st.markdown("""
        <style>
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            [class="st-emotion-cache-7ym5gk ef3psqc12"] {
                display: inline-block;
                padding: 5px 20px;
                background-color: #4681f4;
                color: #FBFFFF;
                width: 300px;
                height: 35px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

def sidebar():
    st.sidebar.image("img/alwrity.jpeg", use_column_width=True)
    st.sidebar.markdown("🧕 :red[Checkout Alwrity], complete **AI writer & Blogging solution**:[Alwrity](https://alwrity.netlify.app)")


def title_and_description():
    st.title("✍️ Alwrity - AI Generator for OATH Copywriting Formula")
    with st.expander("What is **OATH Copywriting Formula** & **How to Use**? 📝❗"):
        st.markdown('''
            ### What's OATH Copywriting Formula, and How to use this AI generator 🗣️
            ---
            #### OATH Copywriting Formula

            OATH stands for Oblivious-Apathetic-Thinking-Hurting. It's a copywriting formula that focuses on guiding the audience through different stages of awareness and emotional response:

            1. **Oblivious**: Addressing the audience who may not be aware of the problem or need.
            2. **Apathetic**: Engaging with the audience who may know about the problem but are indifferent or apathetic.
            3. **Thinking**: Connecting with the audience who are actively thinking about the problem and potential solutions.
            4. **Hurting**: Reaching out to the audience who are experiencing pain or urgency related to the problem.

            The OATH formula helps in tailoring the copy to different stages of awareness and emotional states, leading to more effective communication and engagement.

            #### OATH Copywriting Formula: Simple Example

            - **Oblivious**: "Did you know that poor posture can lead to chronic back pain?"
            - **Apathetic**: "While you may have heard about the importance of good posture, it's easy to overlook its impact on your health."
            - **Thinking**: "As you consider the long-term effects of poor posture, you may be wondering how to improve it."
            - **Hurting**: "If you're tired of dealing with constant back pain, it's time to take action and prioritize your posture."

            ---
        ''')


def input_section():
    with st.expander("**PRO-TIP** - Easy Steps to Create Compelling OATH Copy", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        with col1:
            brand_name = st.text_input('**Enter Brand/Company Name**', help="Enter the name of your brand or company.")
        with col2:
            description = st.text_input(f'**Describe What {brand_name} Does ?** (In 5-6 words)', help="Describe your product or service briefly.")

        oblivious = st.text_input(f'**Address the Oblivious Audience**', help="Highlight a problem or need that the audience may not be aware of.")
        apathetic = st.text_input(f'**Engage with the Apathetic Audience**', help="Connect with the audience who may know about the problem but are indifferent.")
        thinking = st.text_input(f'**Connect with the Thinking Audience**', help="Engage with the audience who are actively considering solutions.")
        hurting = st.text_input(f'**Reach out to the Hurting Audience**', help="Address the audience who are experiencing pain or urgency related to the problem.")

        if st.button('**Get OATH Copy**'):
            if oblivious.strip() and apathetic.strip() and thinking.strip() and hurting.strip():
                with st.spinner("Generating OATH Copy..."):
                    oath_copy = generate_oath_copy(brand_name, description, oblivious, apathetic, thinking, hurting)
                    if oath_copy:
                        st.subheader('**👩🔬👩🔬 Your OATH Copy**')
                        st.markdown(oath_copy)
                    else:
                        st.error("💥 **Failed to generate OATH copy. Please try again!**")
            else:
                st.error("All fields are required!")

    page_bottom()


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_oath_copy(brand_name, description, oblivious, apathetic, thinking, hurting):
    prompt = f"""As an expert copywriter, I need your help in creating a marketing campaign for {brand_name},
        which is a {description}. Your task is to use the OATH (Oblivious-Apathetic-Thinking-Hurting) formula to craft compelling copy.
        Here's the breakdown:
        - Oblivious: {oblivious}
        - Apathetic: {apathetic}
        - Thinking: {thinking}
        - Hurting: {hurting}
        Do not provide explanations, provide the final marketing copy.
    """
    return openai_chatgpt(prompt)


def page_bottom():
    """Display the bottom section of the web app."""
    data_oracle = import_json(r"lottie_files/brain_robot.json")
    st_lottie(data_oracle, width=600, key="oracle")

    st.markdown('''
    Copywrite using OATH Copywriting Formula - powered by AI (OpenAI, Gemini Pro).

    Implemented by [Alwrity](https://alwrity.netlify.app).

    Learn more about [Google's Stance on AI generated content](https://alwrity.netlify.app/post/googles-guidelines-on-using-ai-generated-content-everything-you-need-to-know).
    ''')

    st.markdown("""
    ### Oblivious:
    Are you aware of the impact poor posture can have on your health?

    ### Apathetic:
    While you may have heard about the importance of good posture, it's easy to overlook its effects on your well-being.

    ### Thinking:
    As you contemplate the consequences of poor posture, you may be considering ways to improve it.

    ### Hurting:
    If you're experiencing back pain or discomfort due to poor posture, it's time to take action and prioritize your spinal health.
    """)



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def openai_chatgpt(prompt, model="gpt-3.5-turbo-0125", max_tokens=500, top_p=0.9, n=1):
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            n=n,
            top_p=top_p
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        st.error(f"OpenAI API Error: {e}")
    except openai.APIConnectionError as e:
        st.error(f"Failed to connect to OpenAI API: {e}")
    except openai.RateLimitError as e:
        st.error(f"Rate limit exceeded on OpenAI API request: {e}")
    except Exception as err:
        st.error(f"An error occurred: {err}")


# Function to import JSON data
def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url



if __name__ == "__main__":
    main()

