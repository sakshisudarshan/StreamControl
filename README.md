# StreamControl

**StreamControl** is a gesture-based video control web application that enables hands-free interaction with YouTube videos using real-time hand gesture recognition.

---

## Features

### Gesture-based Controls

* Open Palm – Play/Pause the video
* Closed Fist – Mute/Unmute the video
* Two Fingers – Skip forward by 10 seconds

### Real-time Webcam Feed

* Processes live camera feed for gesture detection
* Uses OpenCV and MediaPipe to identify hand positions

### Seamless YouTube Integration

* Accepts a YouTube URL and embeds the video
* Gesture commands directly control the YouTube player

### User-Friendly Interface

* Modern UI with responsive design
* Gradient color scheme and soft shadows for a clean look

---

## Tech Stack

### Frontend

* HTML5, CSS3, JavaScript
* YouTube IFrame API
* Socket.IO (client-side)

### Backend

* Flask
* Socket.IO (server-side)
* OpenCV
* MediaPipe

---

## Setup & Installation

1.  **Clone the Repository**

    ```bash
    git clone [https://github.com/your-repo/streamcontrol.git](https://github.com/your-repo/streamcontrol.git)
    cd streamcontrol
    ```

2.  **Create and Activate a Virtual Environment**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application**

    ```bash
    python app.py
    ```

---

![PHOTO-2024-12-20-14-53-12 5](https://github.com/user-attachments/assets/f1a7617f-2b86-4964-b10a-96efc358a814)
![PHOTO-2024-12-20-14-53-12](https://github.com/user-attachments/assets/fc1a729d-0957-4f28-80e8-22b4e7978376)
![PHOTO-2024-12-20-14-53-12 3](https://github.com/user-attachments/assets/86a413cf-3316-42e3-b314-2cece113e710)
![PHOTO-2024-12-20-14-53-12 4](https://github.com/user-attachments/assets/1b7ce67c-03f0-49ab-b231-f2db430b0734)
![PHOTO-2024-12-20-14-53-12 2](https://github.com/user-attachments/assets/5897bc88-4228-4558-b9ab-57883a8075c9)





## Code Overview

### 1. Backend (`app.py`)

* **Flask Application**
    * Handles HTTP requests and serves the frontend.
    * Uses Flask-SocketIO for real-time communication between the backend and frontend.
    * Opens a video capture stream using OpenCV for gesture detection.
* **Gesture Detection**
    * Uses MediaPipe to track hand landmarks.
    * Recognizes gestures based on hand positions:
        * Open Palm – Play/Pause
        * Closed Fist – Mute/Unmute
        * Two Fingers – Forward 10 seconds
    * Sends recognized gestures to the frontend using Socket.IO.
* **YouTube Integration**
    * Parses YouTube URL and extracts video ID.
    * Loads the video into an iframe using the YouTube IFrame API.

---

### 2. Frontend (`templates/`)

* **HTML**
    * `consent.html` – Displays a consent form to enable the webcam.
    * `index.html` – Main interface with webcam feed, video player, and gesture guide.
* **JavaScript**
    * Handles YouTube IFrame API for video controls.
    * Listens for gesture events from the backend using Socket.IO.
    * Maps gestures to YouTube player actions (play, pause, mute, forward).
* **CSS**
    * Modern, responsive design using flexbox and grid.
    * Gradient color scheme and hover effects for better UX.

---

### 3. Static Files (`static/`)

* **style.css** – Styles for UI elements and layout.

---

### 4. Gesture Recognition Logic

* **Open Palm** – Fingers extended above reference points.
* **Closed Fist** – Fingers curled below reference points.
* **Two Fingers** – Index and middle fingers extended; others curled.

---

### 5. Socket.IO Communication

* Backend emits gesture events to frontend.
* Frontend listens for events and maps them to YouTube controls.

---

## Contributing

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact [Sakshi Sudarshan](mailto:sakshisudarshan4@gmail.com).
