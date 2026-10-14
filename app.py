from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('register.html')


@app.route('/submit', methods=['POST'])
def register():
    username = request.form.get('username', '').strip()
    password = request.form.get('pwd', '')

    if not username:
        return """
        <script>
        alert('Username cannot be empty.');
        window.history.back();
        </script>
        """

    if len(password) < 6:
        return """
        <script>
        alert('Password must be at least 6 characters.');
        window.history.back();
        </script>
        """

    return f"Hello, {username}! Welcome to website"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
