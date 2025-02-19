##Flask App Routing

from flask import Flask, request, jsonify
import threading
import time

## create a simple flask application

app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    rprint("Welcome to the Assessment Service")

@app.route("/upload", methods=["POST"])
def upload():
    global upload_request  
    upload_request = request.json 

    thread =threading.Thread(target=start_bc)
    thread.start()
    response_data = {"assesmentId":"assessmentId1"+upload_request.get("git_branch", "main")};
    return jsonify(response_data)


def start_bc():
    try:   
        git_repo_url = upload_request.get("git_repo_url")
        branch = upload_request.get("git_branch", "main")
        git_token = upload_request.get("git_token")     
        print(git_repo_url)
        print(branch)
        print(git_token)
        
        i = 1
        while i<1000000:
            print(i)
            i+=1
        time.sleep(5)
        print("Assessment done")
        ##return redirect("/")
    except Exception as e:
        return jsonify({"status":"error", "message":str(e)})

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