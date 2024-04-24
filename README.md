# Alwrity - AI Generator for OATH Copywriting Formula

Alwrity is a web application built with Streamlit that utilizes OpenAI's GPT-3.5 model to generate marketing copy using the OATH (Oblivious-Apathetic-Thinking-Hurting) formula. This application enables users to create compelling marketing content by inputting key details about their brand and addressing different stages of audience awareness and emotional response.

## OATH Copywriting Formula

The OATH formula focuses on guiding the audience through different stages of awareness and emotional response:

1. **Oblivious**: Addressing the audience who may not be aware of the problem or need.
2. **Apathetic**: Engaging with the audience who may know about the problem but are indifferent or apathetic.
3. **Thinking**: Connecting with the audience who are actively thinking about the problem and potential solutions.
4. **Hurting**: Reaching out to the audience who are experiencing pain or urgency related to the problem.

The OATH formula helps tailor the copy to different stages of awareness and emotional states, leading to more effective communication and engagement.

### OATH Copywriting Formula: Simple Example

- **Oblivious**: "Did you know that poor posture can lead to chronic back pain?"
- **Apathetic**: "While you may have heard about the importance of good posture, it's easy to overlook its impact on your health."
- **Thinking**: "As you consider the long-term effects of poor posture, you may be wondering how to improve it."
- **Hurting**: "If you're tired of dealing with constant back pain, it's time to take action and prioritize your posture."

## Features

- **OATH Formula**: Utilizes the Oblivious-Apathetic-Thinking-Hurting copywriting formula to guide users in creating persuasive marketing copy.
- **AI-Powered**: Employs OpenAI's GPT-3.5 model to generate high-quality marketing content based on user inputs.
- **User-Friendly Interface**: Offers an intuitive interface for users to input campaign details and view generated copy.
- **Retry Logic**: Implements retry logic using the Tenacity library to handle potential errors when communicating with the OpenAI API.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Set up your OpenAI API key as an environment variable named `OPENAI_API_KEY`.
4. Run the `app.py` file.

## Dependencies

- Streamlit
- OpenAI
- Streamlit Lottie
- Tenacity

## Acknowledgements

- Special thanks to OpenAI for providing access to the GPT-3.5 model.
- This project was inspired by the need for efficient and effective marketing copy generation.
