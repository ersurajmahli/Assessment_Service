##Flask App Routing

from flask import Flask, request, jsonify

## create a simple flask application

app = Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the Assessment Service"

@app.route("/upload", methods=["POST"])
def upload():
    data = request.json
    git_repo_url = data.get("git_repo_url")
    branch = data.get("git_branch", "main")
    hit_token = data.get("git_token")

    response_data = {"assesmentId":"assessmentId1"+branch};
    return jsonify(response_data)

@app.route('/status/<assesmentid>')
def status(assesmentid):
    assessment_status = {
        "Tech Stack Analysis":"In progress",
        "Complexity Analysis":"Todo",
        "Author Analysis":"Todo",
        "Commit Analysis":"Todo",
        "Branch & Tag Analysis":"Todo"
    }
    return jsonify(assessment_status)



if __name__=="__main__":
    app.run(debug=True)