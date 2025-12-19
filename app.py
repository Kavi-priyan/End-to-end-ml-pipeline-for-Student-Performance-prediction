import os
from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
import traceback

app = Flask(__name__)

# Load pipeline once
pipeline = None
pipeline_error = None
try:
    pipeline = PredictPipeline()
    print("✓ Pipeline loaded successfully")
except Exception as e:
    pipeline = None
    pipeline_error = str(e)
    print("✗ Error loading pipeline:", e)
    traceback.print_exc()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    """Health check endpoint for Render"""
    import os
    
    # Check if artifacts exist
    model_path = os.path.join("artifacts", "model.pkl")
    preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
    model_exists = os.path.exists(model_path)
    preprocessor_exists = os.path.exists(preprocessor_path)
    
    response = {
        "status": "healthy",
        "pipeline_loaded": pipeline is not None,
        "model_file_exists": model_exists,
        "preprocessor_file_exists": preprocessor_exists,
        "current_directory": os.getcwd(),
        "files_in_artifacts": os.listdir("artifacts") if os.path.exists("artifacts") else "artifacts folder not found"
    }
    
    if pipeline_error:
        response["pipeline_error"] = pipeline_error
    
    return response, 200

@app.route("/predict_datapoint", methods=["GET", "POST"])
def predict_datapoint():
    try:
        if request.method == "GET":
            return render_template("home.html")
        else:
            data = CustomData(
                gender=request.form.get("gender"),
                race_ethnicity=request.form.get("ethnicity"),
                parental_level_of_education=request.form.get("parental_level_of_education"),
                lunch=request.form.get("lunch"),
                test_preparation_course=request.form.get("test_preparation_course"),
                reading_score=float(request.form.get("reading_score")),
                writing_score=float(request.form.get("writing_score"))
            )
            pred_df = data.get_data_as_dataframe()
            if pipeline is None:
                return render_template("home.html", results="Pipeline not loaded")
            results = pipeline.predict(pred_df)
            return render_template("home.html", results=results[0])
    except Exception as e:
        traceback.print_exc()
        return render_template("home.html", results=f"Error: {str(e)}")

# Dynamic port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
