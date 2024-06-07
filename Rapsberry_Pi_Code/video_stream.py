from flask import Flask, Response
import cv2
import threading
from gevent.pywsgi import WSGIServer
from gevent import monkey
app = Flask(__name__)
FPS = 15
def generate_frames():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device")
        return

    cap.set(cv2.CAP_PROP_FPS, 15)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 210)

    while True:
        success, frame = cap.read()
        if not success:
            print("Error: Could not read frame")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame,[int(cv2.IMWRITE_JPEG_QUALITY), 25])
            if not ret:
                print("Error: Could not encode frame")
                break
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Run the server using a threaded server to handle multiple clients more efficiently
 
    monkey.patch_all()
    http_server = WSGIServer(('192.168.4.1', 5000), app)
    http_server.serve_forever()
