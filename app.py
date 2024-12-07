from flask import Flask
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/')
def home():
  return render_template('index.html')

tasks = ["Faire les courses", "Répondre aux e-mails", "Préparer la réunion"]
@app.route('/tasks')
def task_list():
 return render_template('tasks.html', tasks=tasks)

@app.route("/contact")
def contact():
   return "Voici la page du contact !"
if __name__ == '__main__':
  app.run(debug=True, port=5002)
