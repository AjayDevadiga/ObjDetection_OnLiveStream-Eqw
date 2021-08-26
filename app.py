import json
from re import DEBUG, sub
from flask import Flask, render_template, request,Response, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
from Obj_Detection_Equations_work import Run_Obj_Detect
from detect import PassImages
import cv2

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
# print(app.instance_path, uploads_dir)
os.makedirs(uploads_dir, exist_ok=True)
frame = cv2.imread('static/Loader.jpg')
# frame = cv2.imread("static/load_loading.gif")
JSON_FLAG_FILE = 'static/flag.json'
@app.route("/")
def hello_world():

    return render_template('index.html')

def generate_video():
    while True:
        global frame
        newImg = PassImages()
        # cv2.imshow("mywinn", newImg)
        # cv2.waitKey(1)
        ret, buffer = cv2.imencode('.jpg', newImg)
        frame_bytes = buffer.tobytes()

        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes+ b'\r\n')


@app.route("/detect", methods=['POST'])
def detect():
    with open(JSON_FLAG_FILE, "r") as jsonFile:
        Flag_data = json.load(jsonFile)

    Flag_data["flag"] = "RUN"

    with open(JSON_FLAG_FILE, "w") as jsonFile:
        json.dump(Flag_data, jsonFile)
    global frame
    # frame = cv2.imread("static/eqw.png")
    if not request.method == "POST":
        return
    print(request.form.get("InputType"))
    if request.form.get("InputType") == "Inputfile":
        video = request.files['Video']
        print(video)
        video.save(os.path.join(uploads_dir, secure_filename(video.filename)))
        Video_File_Path = "instance/uploads/"+secure_filename(video.filename)
        print(secure_filename(video.filename))
        global frame
        frame = Run_Obj_Detect(Video_File_Path)
    elif request.form.get("InputType") == "URL":
        print(request.form.get("Video"))
        src_url = request.form.get("Video")

        frame = Run_Obj_Detect(src_url)

    # cv2.imshow("Mywin", frame)
    # cv2.waitKey(0)
    # subprocess.run("ls")
    # subprocess.run(['python3', 'detect.py', '--source', os.path.join(uploads_dir, secure_filename(video.filename))])

    # return os.path.join(uploads_dir, secure_filename(video.filename))
    # obj = secure_filename(video.filename)
    return "Your response was recieved"


@app.route('/video', methods=['GET'])
def video():
    return Response(generate_video(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/Stopprocess', methods=['POST'])
def Stopprocess():
    with open(JSON_FLAG_FILE, "r") as jsonFile:
        Flag_data = json.load(jsonFile)

    Flag_data["flag"] = "KILL"

    with open(JSON_FLAG_FILE, "w") as jsonFile:
        json.dump(Flag_data, jsonFile)

    global frame
    frame = cv2.imread('static/Loader.jpg')

    return Flag_data
# @app.route('/return-files', methods=['GET'])
# def return_file():
#     obj = request.args.get('obj')
#     loc = os.path.join("runs/detect", obj)
#     print(loc)
#     try:
#         return send_file(os.path.join("runs/detect", obj), attachment_filename=obj)
#         # return send_from_directory(loc, obj)
#     except Exception as e:
#         return str(e)
@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    app.run(debug=False)

    with open(JSON_FLAG_FILE, "r") as jsonFile:
        Flag_data = json.load(jsonFile)

    Flag_data["flag"] = "RUN"

    with open(JSON_FLAG_FILE, "w") as jsonFile:
        json.dump(Flag_data, jsonFile)



# @app.route('/display/<filename>')
# def display_video(filename):
# 	#print('display_video filename: ' + filename)
# 	return redirect(url_for('static/video_1.mp4', code=200))
