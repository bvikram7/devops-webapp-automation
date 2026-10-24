from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>DevOps Demo App</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 0; background: #f3f6fb; color: #1f2937; }
          main { max-width: 760px; margin: 8vh auto; padding: 32px; background: white; border-radius: 16px; box-shadow: 0 8px 28px #0001; }
          h1 { color: #174ea6; }
          .tag { display: inline-block; background: #e7f0ff; color: #174ea6; padding: 7px 12px; border-radius: 20px; margin: 4px; }
          code { background: #f1f5f9; padding: 3px 6px; border-radius: 5px; }
        </style>
      </head>
      <body>
        <main>
          <h1>DevOps Automation Demo</h1>
          <p>This sample web application demonstrates a basic DevOps workflow.</p>
          <span class="tag">Python Flask</span>
          <span class="tag">Docker</span>
          <span class="tag">GitHub Actions CI</span>
          <h2>What happens in this project?</h2>
          <ol>
            <li>Source code is stored in GitHub.</li>
            <li>GitHub Actions runs automated checks when code is pushed.</li>
            <li>Docker packages the application into a container.</li>
            <li>The application can be opened in a browser.</li>
          </ol>
          <p>Health endpoint: <a href="/health">/health</a></p>
        </main>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy", application="devops-demo"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
