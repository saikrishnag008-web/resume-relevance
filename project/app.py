from flask import Flask, render_template, request, jsonify, url_for
from utils import extract_text_from_file, evaluate_resume

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("home.html")

    @app.get("/student")
    def student():
        return render_template("student.html")

    @app.get("/admin")
    def admin():
        return render_template("admin.html")

    @app.get("/dashboard")
    def dashboard():
        return render_template("dashboard.html")

    @app.post("/api/evaluate")
    def evaluate():
        jd_file = request.files.get("jdFile")
        resume_file = request.files.get("resume")
        if not jd_file or not resume_file or not jd_file.filename or not resume_file.filename:
            return jsonify({"status": "fail", "message": "Both Job Description and Resume files are required."}), 400

        jd_content = jd_file.read()
        resume_content = resume_file.read()

        jd_text = extract_text_from_file(jd_content, jd_file.filename)
        resume_text = extract_text_from_file(resume_content, resume_file.filename)

        result = evaluate_resume(resume_text, jd_text)
        return jsonify(result)

    @app.post("/api/admin-login")
    def admin_login():
        data = request.get_json(silent=True) or {}
        username = (data.get("username") or "").strip()
        password = data.get("password") or ""

        if username == "admin" and password == "admin123":
            return jsonify({"status": "success", "redirect": url_for("dashboard")})
        return jsonify({"status": "fail", "message": "Invalid credentials"}), 401

    @app.get("/health")
    def health():
        return {"ok": True}

    @app.errorhandler(404)
    def not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("errors/500.html"), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
