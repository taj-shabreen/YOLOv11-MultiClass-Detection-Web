# 🎯 YOLOv11 Multi-Class Object Detection – Web Application

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-WebApp-lightgrey?logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-%23E34F26.svg?&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-%231572B6.svg?&logo=css3&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-vision-green?logo=opencv)
![Roboflow](https://img.shields.io/badge/Trained%20with-Roboflow-purple?logo=data:image/png;base64,iVBORw0KGgo)

---

## 🌐 About the Project

This is a **YOLOv11-powered multi-class object detection web interface**, built using **Flask** and styled for a sleek, interactive user experience.

The object detection model was **trained using Roboflow's hosted training pipeline** using images combined from various public Universe projects.  
The complete frontend & backend is **developed by Shabreen Taj**.

---

## ⚡ Live UI Demo

### 🖥️ Web Interface
![UI](result/1.png)

### 🚗 Vehicle Detection
![Cars](result/2.png)
![Multiple Cars](result/3.png)
![Bus](result/4.png)

### 🐾 Animal & Person Detection
![Animals](result/6.png)
![Motorbike + Person](result/8.png)

---

## 📊 Model Performance

### Training Graphs
![Training Graph](result/traininggraph.png)

### Advanced Metrics
![Advanced Training Graph](result/advancedtraining.png)

> **Model Type**: YOLOv11 (Fast)  
> **mAP@50**: 34.1% | **Precision**: 37.5% | **Recall**: 37.1%  
> **Trained Images**: 37,647  
> **Epochs**: 90  

---

## 📁 Dataset & Augmentations

### Split Summary

| Split      | %   | Images |
|------------|-----|--------|
| Train      | 89% | 33,390 |
| Validation | 8%  | 3,059  |
| Test       | 3%  | 1,198  |

### Preprocessing & Augmentations

- ✅ Auto-Orient  
- 📐 Resize to 640x640  
- ⚙️ Adaptive Equalization  
- 🔄 Horizontal Flip  
- 🔄 Rotation ±15°  
- ✂️ Shear ±5%  
- 🎨 Hue ±10%  
- 🌓 Saturation ±5%  
- 🌞 Brightness ±10%  
- 📷 Exposure ±5%  
- 🌀 Blur (up to 1px)  
- ⚡ Noise (up to 0.54%)  

---

## ⚙️ Technologies Used

- 🧠 **YOLOv11** model  
- 🔬 Roboflow training  
- 🎯 Flask for Web Interface  
- 🖼️ OpenCV for image handling  
- 🧠 Supervision for annotation overlay  
- 💅 HTML, CSS, JS for frontend  

---

<a href="https://universe.roboflow.com/objectdetectionlab-9hw4e/multi-class-object-detection-qjnaq/model/">
  <img src="https://app.roboflow.com/images/try-model-badge.svg" alt="Try in Roboflow" />
</a>
<a href="https://universe.roboflow.com/objectdetectionlab-9hw4e/multi-class-object-detection-qjnaq">
  <img src="https://app.roboflow.com/images/download-dataset-badge.svg" alt="Download Dataset" />
</a>

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/taj-shabreen/YOLOv11-MultiClass-Detection-Web.git

cd YOLOv11-MultiClass-Detection-Web

python -m venv .venv

.venv\Scripts\activate  # or source .venv/bin/activate

pip install -r requirements.txt
```
📄 Create .env file
```
ROBOFLOW_API_KEY=your_private_api_key_here
```
## 🔐 API & Access Instructions

🔐 Your workspace and API key remain secure

🗝️ Model access requires user's own Roboflow API key

🧠 Others cannot modify your model or use your credits

✅ Safe for GitHub public usage (if .env is ignored)

## ✨ Features
✅ Clean drag-and-drop or upload interface

🎯 Real-time visual predictions

📋 Object name + confidence

📱 Mobile-responsive

🚫 Graceful error when no objects detected

💾 Result image saved locally

## 👩‍💻 Developed By

<p align="center">
  <img src="https://raw.githubusercontent.com/taj-shabreen/YOLOv11-MultiClass-Detection-Web/main/result/developed-by-light-glitch-unscreen.gif" alt="Developed by Shabreen Taj" width="420">
</p>

<p align="center">
  <a href="https://github.com/taj-shabreen" target="_blank">
    🔗 github.com/taj-shabreen
  </a>
</p>

## 🌟 Contribute or Star
⭐️ If you liked the project, give it a star!
