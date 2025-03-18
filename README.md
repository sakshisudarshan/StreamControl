# StreamControl

**StreamControl** is a gesture-based video control web application that enables hands-free interaction with YouTube videos using real-time hand gesture recognition.
---

## Features
### Gesture-based Controls
- Open Palm – Play/Pause the video  
- Closed Fist – Mute/Unmute the video  
- Two Fingers – Skip forward by 10 seconds  

### Real-time Webcam Feed
- Processes live camera feed for gesture detection  
- Uses OpenCV and MediaPipe to identify hand positions  

### Seamless YouTube Integration
- Accepts a YouTube URL and embeds the video  
- Gesture commands directly control the YouTube player  

### User-Friendly Interface
- Modern UI with responsive design  
- Gradient color scheme and soft shadows for a clean look  

---

## Tech Stack
### Frontend
- HTML5, CSS3, JavaScript  
- YouTube IFrame API  
- Socket.IO (client-side)  

### Backend
- Flask  
- Socket.IO (server-side)  
- OpenCV  
- MediaPipe  

---

## Setup & Installation  

```bash
# 1. Clone the Repository
git clone https://github.com/your-repo/streamcontrol.git  
cd streamcontrol  

# 2. Create and Activate a Virtual Environment
python3 -m venv env  
source env/bin/activate  

# 3. Install Dependencies
pip install -r requirements.txt  

# 4. Run the Application
python app.py  

  

## Code Overview  

### 1. Backend (`app.py`)  
- **Flask Application**  
   - Handles HTTP requests and serves the frontend.  
   - Uses Flask-SocketIO for real-time communication between the backend and frontend.  
   - Opens a video capture stream using OpenCV for gesture detection.  

- **Gesture Detection**  
   - Uses MediaPipe to track hand landmarks.  
   - Recognizes gestures based on hand positions:  
     - Open Palm – Play/Pause  
     - Closed Fist – Mute/Unmute  
     - Two Fingers – Forward 10 seconds  
   - Sends recognized gestures to the frontend using Socket.IO.  

- **YouTube Integration**  
   - Parses YouTube URL and extracts video ID.  
   - Loads the video into an iframe using the YouTube IFrame API.  

---

### 2. Frontend (`templates/`)  
- **HTML**  
   - `consent.html` – Displays a consent form to enable the webcam.  
   - `index.html` – Main interface with webcam feed, video player, and gesture guide.  

- **JavaScript**  
   - Handles YouTube IFrame API for video controls.  
   - Listens for gesture events from the backend using Socket.IO.  
   - Maps gestures to YouTube player actions (play, pause, mute, forward).  

- **CSS**  
   - Modern, responsive design using flexbox and grid.  
   - Gradient color scheme and hover effects for better UX.  

---

### 3. Static Files (`static/`)  
- **style.css** – Styles for UI elements and layout.  

---

### 4. Gesture Recognition Logic  
- **Open Palm** – Fingers extended above reference points.  
- **Closed Fist** – Fingers curled below reference points.  
- **Two Fingers** – Index and middle fingers extended; others curled.  

---

### 5. Socket.IO Communication  
- Backend emits gesture events to frontend.  
- Frontend listens for events and maps them to YouTube controls.  

---

## Contributing  
Contributions are welcome! To contribute:  
1. Fork the repository.  
2. Create a new branch:  
```bash
git checkout -b feature/your-feature-name

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please contact [Sakshi Sudarshan](mailto:sakshisudarshan4@gmail.com).

