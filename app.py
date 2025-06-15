from flask import Flask, render_template, request, send_from_directory
import os
from dotenv import load_dotenv
from inference import get_model
import supervision as sv
import cv2

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load your Roboflow API key
load_dotenv()
api_key = os.getenv("ROBOFLOW_API_KEY")
MODEL_ID = "multi-class-object-detection-qjnaq/1"
model = get_model(model_id=MODEL_ID, api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    detections = []
    img_url = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("index.html", detections=[], img_url=None)

        file = request.files["image"]
        if file.filename == "":
            return render_template("index.html", detections=[], img_url=None)

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        image = cv2.imread(filepath)
        results = model.infer(image)[0]  # returns a dictionary
        detection_data = sv.Detections.from_inference(results)

        # Annotate image
        box_annotator = sv.BoxAnnotator()
        label_annotator = sv.LabelAnnotator()
        annotated_image = box_annotator.annotate(scene=image, detections=detection_data)
        annotated_image = label_annotator.annotate(scene=annotated_image, detections=detection_data)

        out_path = os.path.join(app.config['UPLOAD_FOLDER'], 'out_' + file.filename)
        cv2.imwrite(out_path, annotated_image)
        img_url = f"/uploads/out_{file.filename}"

        # ✅ FIX: Extract detected objects correctly
        detections = [
            {"class": pred.class_name, "confidence": f"{pred.confidence * 100:.1f}%"}
            for pred in results.predictions
        ]

    return render_template("index.html", detections=detections, img_url=img_url)

@app.route("/uploads/<path:filename>")
def send_image(filename):
    return send_from_directory("uploads", filename)

if __name__ == "__main__":
    app.run(debug=True)
