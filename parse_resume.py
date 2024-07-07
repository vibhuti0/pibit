import json

def parse_resume_to_json(resume_text):
    resume_json = {
        "name": "",
        "contact": {
            "email": "",
            "phone": "",
            "address": ""
        },
        "summary": "",
        "education": [],
        "experience": [],
        "skills": [],
        "projects": []
    }
    
    lines = resume_text.split('\n')
    current_section = None

    for line in lines:
        line = line.strip()
        if line.lower().startswith("name:"):
            resume_json["name"] = line[len("name:"):].strip()
        elif line.lower().startswith("email:"):
            resume_json["contact"]["email"] = line[len("email:"):].strip()
        elif line.lower().startswith("phone:"):
            resume_json["contact"]["phone"] = line[len("phone:"):].strip()
        elif line.lower().startswith("address:"):
            resume_json["contact"]["address"] = line[len("address:"):].strip()
        elif line.lower().startswith("summary:"):
            current_section = "summary"
            resume_json["summary"] = line[len("summary:"):].strip()
        elif line.lower().startswith("education:"):
            current_section = "education"
        elif line.lower().startswith("experience:"):
            current_section = "experience"
        elif line.lower().startswith("skills:"):
            current_section = "skills"
        elif line.lower().startswith("projects:"):
            current_section = "projects"
        else:
            if current_section == "education":
                resume_json["education"].append(line)
            elif current_section == "experience":
                resume_json["experience"].append(line)
            elif current_section == "skills":
                resume_json["skills"].append(line.split(","))
            elif current_section == "projects":
                resume_json["projects"].append(line)

    return json.dumps(resume_json, indent=4)

# Sample resume text input
resume_text = """
Name: John Doe
Email: john.doe@example.com
Phone: 123-456-7890
Address: 123 Main St, Anytown, USA

Summary: Experienced software engineer with expertise in AI and machine learning.

Education:
Bachelor of Science in Computer Science, XYZ University, 2020

Experience:
Software Engineer at ABC Corp, 2020-2023
AI Intern at DEF Inc, Summer 2019

Skills:
Python, Java, Machine Learning, Data Analysis

Projects:
AI Chatbot for customer service
Machine learning model for predictive analysis
"""

# Parse resume and print JSON
print(parse_resume_to_json(resume_text))
