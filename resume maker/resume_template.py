from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Name and contact information
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Bhavesh Singhal', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, 'Haryana, India | gyomeibhavesh@gmail.com | 9518208482 | linkedin.com/in/bhavesh-singhal-2400a4328', 0, 1, 'C')
        # Add horizontal line below header
        self.line(10, 30, 200, 30)
        self.ln(6)  # Add some space after the line

    def section_title(self, title):
        # Section title with bold font
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        # Add a thin horizontal line under the title
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)  # Reduce line spacing here for tighter content

    def section_body(self, body, indent=False, bullet=False):
        # Body text with regular font and adjusted line spacing
        self.set_font('Arial', '', 10)
        if indent:
            self.cell(10)  # Add an indentation
        if bullet:
            self.cell(5, 8, '-')  # Add a bullet point symbol
        self.multi_cell(0, 8, body)  # Properly display text with wrapping
        self.ln(2)  # Reduced space after each section for compactness

    def create_resume(self, resume_data):
        self.add_page()

        # Professional Summary Section
        self.section_title('SUMMARY')
        self.section_body(resume_data['summary'])

        # Professional Experience Section
        self.section_title('PROJECTS')
        for project in resume_data['projects']:
            self.section_body(f"{project['name']} - {project['github']}")
            self.section_body(project['description'], indent=True, bullet=True)
            self.section_body(project['learning'], indent=True, bullet=True)

        # Education Section
        self.section_title('EDUCATION')
        self.section_body(resume_data['education'])

        # Skills Section
        self.section_title('TECHNICAL SKILLS')
        self.section_body(', '.join(resume_data['technicalskills']))

        self.section_title('SOFT SKILLS')
        self.section_body(', '.join(resume_data['softskills']))

# Sample dummy data
resume_data = {
    "summary": "Passionate Python Developer with a strong understanding of automated testing, AWS services, and PHP, eager to contribute to the Edison team at NewPage Solutions Inc. Proven ability to build and implement features efficiently, ensuring seamless integration and optimal performance within existing web publishing platforms.",
    "projects": [
        {
            "name": "Project Title 1",
            "description": "Describe the project showcasing Python, AWS, and/or testing skills",
            "learning": "Learned skill 1, skill 2 related to the project",
            "github": "GitHub link if available"
        },
        {
            "name": "Project Title 2",
            "description": "Describe another project highlighting relevant skills",
            "learning": "Learned skill 3, skill 4 related to the project",
            "github": "GitHub link if available"
        }
    ],
    "education": "Your Education (e.g., Bachelor's degree in Computer Science)",
    "softskills": [
        "Collaboration",
        "Communication",
        "Problem-Solving",
        "Adaptability",
        "Time Management"
    ],
    "technicalskills": [
        "Python",
        "AWS",
        "PHP",
        "Automated Testing",
        "REST APIs",
        "Git"
    ]
}

# Generate PDF
pdf = PDF()
pdf.create_resume(resume_data)
pdf.output('resume maker\\resume_template.pdf')
