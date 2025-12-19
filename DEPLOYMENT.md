# Render Deployment Guide

## ⚠️ CRITICAL: Python Version Configuration

**Render is currently using Python 3.13 by default, which causes pandas compilation errors.**

### Solution: Manually Set Python Version

1. Go to your Render dashboard: https://dashboard.render.com
2. Select your web service
3. Go to **Settings** → **Environment**
4. Find **"Python Version"** or **"Runtime"** setting
5. **Manually select Python 3.11.9**
6. Save and trigger a new deployment

Alternatively, if using Blueprints:
- The `runtime.txt` file should work, but Render sometimes ignores it
- You may need to manually set Python version in the dashboard after initial deployment

## Files Included

- ✅ `runtime.txt` - Specifies Python 3.11.9
- ✅ `Procfile` - Gunicorn start command
- ✅ `render.yaml` - Optional Blueprint configuration
- ✅ `build.sh` - Build script (optional)
- ✅ `requirements.txt` - All dependencies with pinned versions

## Current Configuration

- **Python**: 3.11.9 (specified in runtime.txt)
- **Pandas**: 2.2.2 (supports Python 3.13 if needed, but Python 3.11 recommended)
- **Scikit-learn**: 1.3.2 (required for model compatibility - don't change!)

## Deployment Steps

### Option 1: Using Render Dashboard

1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: ml-pipeline-app
   - **Environment**: Python 3
   - **Python Version**: **3.11.9** (IMPORTANT - set manually!)
   - **Build Command**: `pip install --upgrade pip setuptools wheel && pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
5. Click "Create Web Service"

### Option 2: Using Blueprints (render.yaml)

1. Go to https://dashboard.render.com
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will detect `render.yaml`
5. **After deployment, manually verify Python version is 3.11.9 in settings**

## Troubleshooting

### Build Fails with Pandas Compilation Errors

**Cause**: Python 3.13 is being used instead of 3.11

**Solution**:
1. Go to Render dashboard → Your service → Settings → Environment
2. Manually set Python version to **3.11.9**
3. Save and redeploy

### Pipeline Not Loading (`pipeline_loaded: false`)

**Check the `/health` endpoint** - it will show:
- File existence status
- Current directory
- Actual error message

**Common causes**:
1. **Scikit-learn version mismatch**: Keep scikit-learn==1.3.2 (don't upgrade!)
2. **Missing artifacts**: Ensure `artifacts/model.pkl` and `artifacts/preprocessor.pkl` are committed to git
3. **Path issues**: The app should handle this automatically, but check logs if needed

### Model Loading Error: `_RemainderColsList`

**Cause**: Scikit-learn version mismatch - model was trained with older version

**Solution**: Keep `scikit-learn==1.3.2` in requirements.txt (already configured)

## Important Notes

- **Artifacts Folder**: Must be committed to git. Files needed:
  - `artifacts/model.pkl`
  - `artifacts/preprocessor.pkl`

- **Python Version**: Always use Python 3.11.9 for best compatibility

- **Scikit-learn**: Never upgrade beyond 1.3.2 - your model depends on it!

- **Health Check**: Visit `/health` endpoint to check pipeline status

## File Structure

```
.
├── app.py                 # Main Flask application
├── requirements.txt       # Dependencies (pinned versions)
├── runtime.txt           # Python 3.11.9
├── Procfile              # Gunicorn command
├── render.yaml           # Blueprint config (optional)
├── build.sh              # Build script (optional)
├── artifacts/            # Model files (must be in git!)
│   ├── model.pkl
│   └── preprocessor.pkl
└── src/                  # Source code
    └── pipeline/
        └── predict_pipeline.py
```

