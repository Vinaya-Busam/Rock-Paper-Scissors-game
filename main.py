from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
        result = ""
        user_choice = ""
        computer_choice = ""
        if request.method == "POST":
            if request.form.get("reset") == "true":
                pass
            else:
                choices = ["Rock", "Paper", "Scissors"]
                user_choice = request.form["choice"]
                computer_choice = random.choice(choices)

                if user_choice == computer_choice:
                    result = "It's a draw!"
                elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
                    (user_choice == 'Paper' and computer_choice == 'Rock') or \
                    (user_choice == 'Scissors' and computer_choice == 'Paper') :
                    result = "You Win!"
                else:
                    result = "You Lose!"
    
        return render_template("index.html", result=result, user=user_choice, computer=computer_choice)

if __name__ == "__main__":
    app.run(debug=True)