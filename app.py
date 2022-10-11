from flask import Flask, render_template, Response
from webcam import detect_mask

app = Flask(__name__)

def gen():
    while True:
        frame= detect_mask()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' +frame+ b'r\n\r\n')

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/live")
def live():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)