import os
from app import app, db
from models import Employee

def init_database():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        dummy_employees = [
            Employee(
                employee_id='EMP001',
                name='John Doe',
                email='john.doe@company.com',
                role='Senior Software Engineer',
                location='New York, NY',
                skills='Python, Flask, PostgreSQL, React, Docker',
                is_available=True
            ),
            Employee(
                employee_id='EMP002',
                name='Jane Smith',
                email='jane.smith@company.com',
                role='Full Stack Developer',
                location='San Francisco, CA',
                skills='JavaScript, Node.js, MongoDB, Vue.js, AWS',
                is_available=False
            ),
            Employee(
                employee_id='EMP003',
                name='Robert Johnson',
                email='robert.johnson@company.com',
                role='DevOps Engineer',
                location='Austin, TX',
                skills='Docker, Kubernetes, Jenkins, Terraform, Python',
                is_available=True
            ),
            Employee(
                employee_id='EMP004',
                name='Emily Davis',
                email='emily.davis@company.com',
                role='Data Scientist',
                location='Seattle, WA',
                skills='Python, Machine Learning, TensorFlow, SQL, R',
                is_available=True
            ),
            Employee(
                employee_id='EMP005',
                name='Michael Brown',
                email='michael.brown@company.com',
                role='Frontend Developer',
                location='Boston, MA',
                skills='React, TypeScript, CSS, HTML, Redux',
                is_available=False
            ),
            Employee(
                employee_id='EMP006',
                name='Sarah Wilson',
                email='sarah.wilson@company.com',
                role='Backend Developer',
                location='Chicago, IL',
                skills='Java, Spring Boot, MySQL, Microservices, Kafka',
                is_available=True
            ),
            Employee(
                employee_id='EMP007',
                name='David Martinez',
                email='david.martinez@company.com',
                role='Cloud Architect',
                location='Denver, CO',
                skills='AWS, Azure, GCP, Serverless, CloudFormation',
                is_available=False
            ),
            Employee(
                employee_id='EMP008',
                name='Lisa Anderson',
                email='lisa.anderson@company.com',
                role='QA Engineer',
                location='Portland, OR',
                skills='Selenium, Jest, Pytest, CI/CD, Automation',
                is_available=True
            ),
            Employee(
                employee_id='EMP009',
                name='James Taylor',
                email='james.taylor@company.com',
                role='Mobile Developer',
                location='Miami, FL',
                skills='React Native, Swift, Kotlin, Firebase, iOS',
                is_available=True
            ),
            Employee(
                employee_id='EMP010',
                name='Patricia Garcia',
                email='patricia.garcia@company.com',
                role='Product Manager',
                location='Los Angeles, CA',
                skills='Agile, Scrum, JIRA, Product Strategy, Analytics',
                is_available=False
            ),
            Employee(
                employee_id='EMP011',
                name='Christopher Lee',
                email='christopher.lee@company.com',
                role='Security Engineer',
                location='Washington, DC',
                skills='Cybersecurity, Penetration Testing, SIEM, Python',
                is_available=True
            ),
            Employee(
                employee_id='EMP012',
                name='Amanda White',
                email='amanda.white@company.com',
                role='UI/UX Designer',
                location='Atlanta, GA',
                skills='Figma, Sketch, Adobe XD, User Research, Prototyping',
                is_available=True
            ),
            Employee(
                employee_id='EMP013',
                name='Daniel Harris',
                email='daniel.harris@company.com',
                role='Database Administrator',
                location='Phoenix, AZ',
                skills='PostgreSQL, MySQL, MongoDB, Oracle, Performance Tuning',
                is_available=False
            ),
            Employee(
                employee_id='EMP014',
                name='Jennifer Clark',
                email='jennifer.clark@company.com',
                role='Machine Learning Engineer',
                location='San Diego, CA',
                skills='PyTorch, TensorFlow, NLP, Computer Vision, MLOps',
                is_available=True
            ),
            Employee(
                employee_id='EMP015',
                name='Matthew Lewis',
                email='matthew.lewis@company.com',
                role='Solutions Architect',
                location='Philadelphia, PA',
                skills='System Design, Microservices, REST APIs, GraphQL',
                is_available=True
            )
        ]
        
        for employee in dummy_employees:
            db.session.add(employee)
        
        db.session.commit()
        print(f"Successfully added {len(dummy_employees)} employees to the database!")

if __name__ == '__main__':
    init_database()
