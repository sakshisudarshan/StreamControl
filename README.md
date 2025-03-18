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

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/streamcontrol.git
cd streamcontrol

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   4. **Run the Application**
      '''bash
      python app.py
      '''

  ---
  # ImageCaptionApp

## Overview  
**ImageCaptionApp** is a tool that extracts text from images and generates meaningful captions using a pre-trained BLIP model. It provides an intuitive user interface built with Kivy and processes images using Flask on the backend.

---

## Backend (`backend.py`)  
- Flask application to handle image processing requests.  
- Uses **pytesseract** to extract text from images.  
- Uses a pre-trained **BLIP model** to generate image captions.  

---

## Models (`models.py`)  
- Contains functions for preprocessing images and generating captions using the BLIP model.  

---

## Frontend (`main.py`)  
- Kivy application to create a user interface.  
- Allows users to select images, send them to the backend for processing, and receive audible descriptions.  

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

