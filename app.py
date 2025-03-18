from flask import Flask, render_template, Response, request
from flask_socketio import SocketIO, emit
import cv2
import mediapipe as mp
import re
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

video_id = None
last_gesture_time = 0
GESTURE_COOLDOWN = 1

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

def generate_frames():
    global last_gesture_time
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            gesture = None
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    if is_palm(hand_landmarks):
                        gesture = "Full Palm"
                    elif is_fist(hand_landmarks):
                        gesture = "Closed Fist"
                    elif is_two_fingers(hand_landmarks):
                        gesture = "Two Fingers"

                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            current_time = time.time()
            if gesture and (current_time - last_gesture_time > GESTURE_COOLDOWN):
                perform_action(gesture)
                last_gesture_time = current_time

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def is_palm(landmarks):
    return all(landmarks.landmark[i].y < landmarks.landmark[i - 2].y for i in [8, 12, 16, 20])

def is_fist(landmarks):
    return all(landmarks.landmark[i].y > landmarks.landmark[i - 2].y for i in [8, 12, 16, 20])

def is_two_fingers(landmarks):
    return (landmarks.landmark[8].y < landmarks.landmark[5].y and
            landmarks.landmark[12].y < landmarks.landmark[9].y and
            landmarks.landmark[16].y > landmarks.landmark[13].y)


def perform_action(gesture):
    print(f"Gesture detected: {gesture}")
    if gesture == "Full Palm":
        socketio.emit('video_control', {'action': 'play_pause'})
    elif gesture == "Closed Fist":
        socketio.emit('video_control', {'action': 'mute'})
    elif gesture == "Two Fingers":
        socketio.emit('video_control', {'action': 'forward'})

@app.route('/')
def consent():
    return render_template('consent.html')

@app.route('/main')
def index():
    return render_template('index.html', video_id=video_id)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/set_video', methods=['POST'])
def set_video():
    global video_id
    url = request.form.get('video_url')
    match = re.search(r"(https?://(?:www\.)?youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        video_id = match.group(2)
    else:
        video_id = None
    return render_template('index.html', video_id=video_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)
