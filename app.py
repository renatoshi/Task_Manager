from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo
tasks = [
    {"id": 1, "title": "Learn Flask", "done": False},
    {"id": 2, "title": "Learn TailwindCSS", "done": False},
]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            new_task = {
                "id": tasks[-1]["id"] + 1 if tasks else 1,
                "title": title,
                "done": False,
            }
            tasks.append(new_task)
            return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/update/<int:task_id>", methods=["GET", "POST"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if not task:
        return "Task not found", 404
    if request.method == "POST":
        task["title"] = request.form.get("title", task["title"])
        task["done"] = "done" in request.form
        return redirect(url_for("index"))
    return render_template("update.html", task=task)

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task:
        tasks.remove(task)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
