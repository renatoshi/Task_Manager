Task Manager

Description
Task Manager is a simple web application that allows users to manage tasks. It was built using Flask as the backend framework and TailwindCSS for the frontend design.

Technologies Used
Flask: Lightweight backend framework.
TailwindCSS: Utility-first CSS framework.
Python: Programming language.
HTML5/CSS3: For frontend templates and styles.

Features
Create new tasks.
Update existing tasks.
Mark tasks as completed.
Delete tasks.
Responsive and clean design with TailwindCSS.


Prerequisites
Python 3.7 or higher: to run Flask.
Node.js: to install and use TailwindCSS.

1. Clone repository:
git clone https://github.com/your-username/task_manager.git
cd task_manager

2. Set Up the Virtual Environment
python -m venv venv
venv\Scripts\activate

3. venv\Scripts\activate
pip install -r requirements.txt

4. Set Up TailwindCSS
npm install
npx tailwindcss -i ./static/css/styles.css -o ./static/css/output.css --watch

5. Run the Application Start the Flask server
python app.py
