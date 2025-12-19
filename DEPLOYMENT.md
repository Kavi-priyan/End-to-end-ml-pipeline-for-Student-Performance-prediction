# Render Deployment Guide

This guide will help you deploy this ML Pipeline application to Render.

## Prerequisites

1. A GitHub account with this repository
2. A Render account (sign up at https://render.com)

## Deployment Steps

### 1. Prepare Your Repository

Make sure your repository includes:
- ✅ `app.py` - Main Flask application
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Process file for Render
- ✅ `render.yaml` - Render configuration (optional)
- ✅ `artifacts/` folder with:
  - `model.pkl` - Trained model
  - `preprocessor.pkl` - Preprocessor object
- ✅ `templates/` folder with HTML templates

### 2. Deploy on Render

#### Option A: Using Render Dashboard (Recommended)

1. Go to https://dashboard.render.com
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: ml-pipeline-app (or your preferred name)
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Instance Type**: Free tier is fine for testing
5. Click "Create Web Service"

#### Option B: Using render.yaml (Blueprints)

1. Go to https://dashboard.render.com
2. Click "New +" and select "Blueprint"
3. Connect your GitHub repository
4. Render will automatically detect `render.yaml` and configure the service

### 3. Important Notes

- **Artifacts Folder**: Make sure your `artifacts/` folder with `model.pkl` and `preprocessor.pkl` is committed to your repository. If these files are large, consider using Git LFS or storing them in cloud storage.

- **Environment Variables**: No environment variables are required for basic deployment. The PORT is automatically set by Render.

- **Build Time**: The first build may take 5-10 minutes as it installs all dependencies including ML libraries.

- **Health Check**: The app includes a `/health` endpoint that you can use for monitoring.

### 4. Verify Deployment

Once deployed:
1. Visit your Render service URL
2. Test the `/health` endpoint: `https://your-app.onrender.com/health`
3. Test the main application at the root URL

### 5. Troubleshooting

- **Build Fails**: Check the build logs in Render dashboard. Common issues:
  - Missing dependencies in requirements.txt
  - Python version mismatch
  - Missing files (artifacts, templates)

- **App Crashes**: Check the runtime logs:
  - Pipeline loading errors
  - Missing model files
  - Port binding issues

- **Slow Performance**: Free tier instances may spin down after inactivity. First request after inactivity may take 30-60 seconds.

## File Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Process file for Render
├── render.yaml           # Render configuration (optional)
├── artifacts/            # Model and preprocessor files
│   ├── model.pkl
│   └── preprocessor.pkl
├── templates/            # HTML templates
│   ├── index.html
│   └── home.html
└── src/                  # Source code
    └── pipeline/
        └── predict_pipeline.py
```

## Support

For issues specific to:
- **Render Platform**: Check Render documentation at https://render.com/docs
- **Application Code**: Check the application logs in Render dashboard

