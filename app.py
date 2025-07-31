from flask import Flask, request, render_template
import datetime

app = Flask(__name__)

# Sample productivity responses
def generate_response(user_input):
    if "time" in user_input.lower():
        return f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "focus" in user_input.lower():
        return "Take a 5-minute break, then focus for 25 minutes. You got this! 💪"
    elif "motivate" in user_input.lower():
        return "Remember why you started. Stay consistent. Great things take time!"
    else:
        return "I'm here to help you stay productive. Ask me anything!"

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form.get("query")
        response = generate_response(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
