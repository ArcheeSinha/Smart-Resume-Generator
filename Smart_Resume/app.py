import google.generativeai as genai
import streamlit as st

# ✅ Configure the GenAI client
genai.configure(api_key="AIzaSyBg67zYUryM9dKIwaBOqwJK4kDJTMEf9cQ")  # Replace with your actual API key

# ✅ Function to generate a resume using Gemini API
def generate_resume(name, job_title, email, phone, linkedin, university, grad_year):
    # ✅ Create the generative model instance
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    # ✅ Create the context dynamically
    context = f"""
    Name: {name}
    Job Title: {job_title}
    Email: {email}
    Phone Number: {phone}
    LinkedIn: {linkedin if linkedin else 'Not Provided'}
    University: {university}
    Graduation Year: {grad_year}

    Create a professional ATS-friendly resume based on the above information.
    """

    # ✅ Generate content from the model
    response = model.generate_content(contents=[context])

    # ✅ Extract the generated content properly
    if response and response.candidates:
        text = response.candidates[0].content.parts[0].text  # Ensure correct extraction
        return clean_resume_text(text)
    else:
        return "⚠️ Error: Unable to generate resume. Please try again."

# ✅ Function to clean the text (Remove extra placeholders)
def clean_resume_text(text):
    placeholders = [
        "[Add Email Address]", "[Add Phone Number]", "[Add LinkedIn Profile URL (optional)]",
        "[University Name]", "[Graduation Year]"
    ]
    for placeholder in placeholders:
        text = text.replace(placeholder, "")
    return text.strip()

# ✅ Streamlit App UI
st.title("📄 Smart Resume Generator")

# Input fields
name = st.text_input("Enter your Full Name")
job_title = st.text_input("Enter your Job Title")
email = st.text_input("Enter your Email Address")
phone = st.text_input("Enter your Phone Number")
linkedin = st.text_input("Enter your LinkedIn Profile URL (Optional)")
university = st.text_input("Enter your University Name")
grad_year = st.text_input("Enter your Graduation Year")

# Generate button
if st.button("Generate Resume"):
    if name and job_title and email and phone and university and grad_year:
        # ✅ Generate the resume
        resume = generate_resume(name, job_title, email, phone, linkedin, university, grad_year)
        st.markdown("## 📝 Generated Resume")
        st.markdown(resume)
    else:
        st.warning("⚠️ Please fill all the required fields.")
