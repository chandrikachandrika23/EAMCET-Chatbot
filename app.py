import streamlit as st

def chatbot_response(user_input):
    user_input = user_input.lower().strip() # Normalize input
    responses = {
        "what is eamcet": "EAMCET stands for Engineering, Agriculture, and Medical Common Entrance Test. It is an entrance exam conducted for admissions into engineering and medical colleges in Telangana and Andhra Pradesh.",
        "who conducts eamcet": "EAMCET is conducted by Jawaharlal Nehru Technological University (JNTU) on behalf of the respective state councils.",
        "what is the eligibility for eamcet": "To appear for EAMCET, candidates must have completed their 10+2 education with Physics, Chemistry, and Mathematics/Biology as core subjects.",
        "how to apply for eamcet": "You can apply for EAMCET online through the official website by filling out the application form and paying the required fee.",
          "when is EAMCET conducted": "EAMCET is usually conducted in the months of April or May. Exact dates vary each year and are announced on the official website.",
        "what is the syllabus for EAMCET": "The EAMCET syllabus includes topics from Physics, Chemistry, and Mathematics/Biology from the 11th and 12th standard curriculum.",
        "what is the exam pattern for EAMCET": "EAMCET is a computer-based test with multiple-choice questions. It consists of 160 questions: 80 from Mathematics, 40 from Physics, and 40 from Chemistry.",
        "how many marks is EAMCET conducted for": "The EAMCET exam is conducted for a total of 160 marks, with no negative marking.",
        "how to download EAMCET hall ticket": "You can download the hall ticket from the official EAMCET website by entering your registration details.",
        "what is the pass mark for EAMCET": "The minimum qualifying marks for EAMCET is 40 out of 160 for general category candidates. There is no minimum qualifying mark for SC/ST candidates.",
        "how is the EAMCET rank calculated": "The EAMCET rank is calculated based on 75% of the EAMCET score and 25% of the Intermediate Board marks in relevant subjects.",
        "when will EAMCET results be declared": "EAMCET results are typically declared within a few weeks after the exam. The exact date is announced on the official website.",
        "how to check EAMCET results": "You can check your EAMCET results by visiting the official website and entering your hall ticket number.",
        "how to download EAMCET rank card": "The EAMCET rank card can be downloaded from the official website by entering your registration details.",
        "what is the counselling process for EAMCET": "EAMCET counselling includes registration, document verification, choice filling, seat allotment, and final admission to colleges.",
        "how to select colleges during EAMCET counselling": "During EAMCET counselling, you need to fill in your preferred colleges and courses based on your rank. The allotment is based on merit and availability.",
        "what are the documents required for EAMCET counselling": "Documents required include EAMCET hall ticket, rank card, SSC certificate, Intermediate marks memo, caste certificate (if applicable), income certificate, and residence proof.",
        "how to pay the counselling fee for EAMCET": "The counselling fee can be paid online during the registration process on the official counselling website.",
        "how to check seat allotment in EAMCET": "You can check seat allotment results by logging into the official EAMCET counselling portal using your credentials.",
        "what to do after seat allotment in EAMCET": "After seat allotment, candidates must download the allotment order, report to the assigned college, and complete the admission process.",
        "what if I don’t get my preferred college in EAMCET": "You can participate in further rounds of counselling or opt for spot admissions if seats are available.",
        "can I change my allotted college in EAMCET": "You can participate in subsequent counselling rounds to try for a better college. However, once the final allotment is confirmed, changes are not allowed.",
        "is there a second counselling for EAMCET": "Yes, there are multiple rounds of counselling based on seat availability and candidate preferences.",
        "how to get a refund if I cancel my EAMCET admission": "You need to check with the allotted college's refund policy. Some colleges provide refunds with a deduction of processing fees.",
        "what is the EAMCET fee structure for different colleges": "Fee structures vary between government, private, and deemed universities. You can check the official website or the counselling portal for details.",
        "are there scholarships available through EAMCET": "Yes, scholarships are available for merit students and economically weaker sections. Check with the respective college for details.",
        "how can I prepare effectively for EAMCET": "Make a study plan, focus on NCERT textbooks, practice previous year papers, and take mock tests to improve your speed and accuracy.",
        "is coaching necessary for EAMCET": "Coaching is not mandatory, but it can help in structured preparation. Many students prepare by self-study using online resources.",
        "where can I find previous year EAMCET question papers": "You can find previous year question papers on the official website or various educational platforms online.",
        "bye": "Goodbye! All the best for your EAMCET preparation and admission process!",
        # Add more questions here
    }
    
    # Find the closest matching key
    for key in responses.keys():
        if user_input in key:
            return responses[key]
    
    return "I'm sorry, I don't have that information. Please check the official EAMCET website."

st.title("EAMCET Chatbot")
user_input = st.text_input("Ask me about EAMCET:")
if user_input:
    st.write("Chatbot:", chatbot_response(user_input))
