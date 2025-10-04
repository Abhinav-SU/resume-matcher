# Resume Matcher# Resume Matcher# Resume Matcher# 🔍 AI Resume Matcher# 🔍 Resume Matcher App



AI-powered resume ranking system that matches candidates to job descriptions using Google Gemini embeddings and machine learning.



## What It DoesAI-powered resume ranking system that matches candidates to job descriptions using Google Gemini embeddings and machine learning.



Upload a job description and multiple resumes. The system ranks candidates by relevance using semantic similarity, showing you the best matches first with AI-generated fit summaries.



## Features## What It DoesAI-powered resume matching application using Google Gemini AI to rank candidates based on job descriptions.



- Supports PDF and DOCX resume formats

- Uses Google Gemini AI for semantic matching

- Ranks candidates by similarity scoreUpload a job description and multiple resumes. The system ranks candidates by relevance using semantic similarity, showing you the best matches first with AI-generated fit summaries.

- Generates AI summaries explaining candidate fit

- Password protected with rate limiting

- Processes multiple resumes in parallel

## Features## FeaturesAI-powered candidate ranking system using Google Gemini AI and machine learning to match resumes with job descriptions.An intelligent AI-powered resume matching application that uses Google Gemini embeddings to find the best candidates for job descriptions. Built with Streamlit for a modern, user-friendly interface.

## Installation




# Resume Matcher

AI-powered resume ranking system that matches candidates to job descriptions using Google Gemini embeddings.

What it does

- Upload a job description and multiple resumes (PDF or DOCX).
- Rank candidates by semantic similarity.
- Show short AI-generated fit summaries for top matches.

Quick start

1. Create and activate a Python 3.11+ virtual environment.
2. Install dependencies: pip install -r requirements.txt
3. Copy .env.example to .env and add your GEMINI_API_KEY.
4. Run the app: streamlit run app.py
5. Open http://localhost:8501 in your browser.

Files

- app.py: Streamlit application (UI, authentication, rate limiting)
- gemini_api.py: Gemini embeddings and summary helpers
- matcher.py: Ranking logic using cosine similarity
- utils.py: PDF and DOCX text extraction
- logger.py: Logging configuration
- requirements.txt: Python dependencies
- .env.example: Environment variable template
- tests/: Unit tests

Security

- Do not commit your .env or API keys.
- Regenerate API key if it was ever exposed.
- .gitignore excludes .env, virtualenv, and cache files.

License

This project is licensed under the MIT License. See the LICENSE file for details.


```toml### Prerequisites

## License

app_password = "your_secure_password"- Python 3.8+

MIT License

```- Google Gemini API key



### 4. Run the App### Local Setup



```bash1. **Clone the repository**

streamlit run app.py   ```bash

```   git clone https://github.com/yourusername/resume-matcher-app.git

   cd resume-matcher-app

Visit: http://localhost:8501   ```



## Deploy to Streamlit Cloud (FREE)2. **Install dependencies**

   ```bash

### 1. Push to GitHub   pip install -r requirements.txt

```bash   ```

git add .

git commit -m "Initial commit"3. **Set up environment variables**

git push origin main   ```bash

```   cp .env.example .env

   # Edit .env and add your Gemini API key

### 2. Deploy   ```

1. Go to https://share.streamlit.io/

2. Sign in with GitHub4. **Get your Gemini API key**

3. Click "New app"   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)

4. Select your repo and `app.py`   - Create a new API key

5. Add secrets in Settings:   - Add it to your `.env` file:

   ```toml     ```

   app_password = "your_password"     GEMINI_API_KEY=your_actual_api_key_here

   GEMINI_API_KEY = "your_api_key"     ```

   ```

6. Click Deploy5. **Run the application**

   ```bash

### 3. Custom Domain (Optional)   streamlit run app.py

   ```

Add a CNAME record in your DNS:

- **Name:** `resume` (or subdomain you want)### Windows (PowerShell) Quick Start

- **Target:** `your-app-name.streamlit.app`

1. **Run the setup script** (creates a venv and installs dependencies):

Access at: `https://resume.yourdomain.com`   ```powershell

   ./setup_windows.ps1

## Tech Stack   ```



- **Python 3.11+**2. **Activate the virtual environment and run the app**:

- **Streamlit** - Web framework   ```powershell

- **Google Gemini AI** - Embeddings and text generation   ./run_windows.ps1

- **Scikit-learn** - Cosine similarity matching   ```

- **PyMuPDF** - PDF text extraction

- **python-docx** - DOCX text extraction3. **Run tests** (from project root, venv activated):

   ```powershell

## Security Features   pytest -q

   ```

- **Password Protection** - Only authorized users can access

- **Rate Limiting** - 5 batches/hour, 20/day per user## 🚀 Deployment

- **API Quotas** - Stays within free tier limits

- **Usage Logging** - Track all requests### Streamlit Cloud Deployment



## Project Structure1. **Push to GitHub**

   ```bash

```   git add .

resume-matcher-app/   git commit -m "Initial commit: Resume Matcher App"

├── app.py              # Main Streamlit application   git push origin main

├── gemini_api.py       # Google Gemini API wrapper   ```

├── matcher.py          # Resume ranking logic

├── utils.py            # Text extraction utilities2. **Deploy on Streamlit Cloud**

├── logger.py           # Logging configuration   - Visit [share.streamlit.io](https://share.streamlit.io)

├── requirements.txt    # Python dependencies   - Connect your GitHub account

├── .env               # API keys (create this)   - Select the `resume-matcher-app` repository

├── .streamlit/   - Set the main file path: `app.py`

│   └── secrets.toml   # App password (create this)

└── tests/             # Unit tests3. **Configure Environment Variables**

```   - In Streamlit Cloud dashboard, go to "Settings"

   - Add environment variable:

## Cost     - **Key**: `GEMINI_API_KEY`

     - **Value**: Your Gemini API key

**100% FREE** with:   - Deploy the app

- Streamlit Community Cloud (free tier)

- Google Gemini API (free tier: 1,500 requests/day)### Alternative Deployment Options

- Rate limiting keeps you under quota limits

- **Heroku**: Use the Procfile and requirements.txt

## License- **Docker**: Build with the provided Dockerfile

- **Local Server**: Run with `streamlit run app.py --server.port 8501`

MIT License - Feel free to use for your portfolio!

## 📁 Project Structure

## Author

```

Built by [Your Name]resume-matcher-app/

- Portfolio: https://yourdomain.com├── app.py                 # Main Streamlit application

- GitHub: https://github.com/yourusername├── matcher.py             # Cosine similarity & ranking logic

├── gemini_api.py          # Gemini API wrapper
├── utils.py               # File processing utilities
├── logger.py              # Shared logging configuration
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |

### Supported File Formats

- **PDF**: Full text extraction with PyMuPDF
- **DOCX**: Text extraction with python-docx
- **File Size**: Recommended < 10MB per file

## 📊 Performance

### Optimization Features
- **Parallel Resume Parsing**: ~3x faster with ThreadPoolExecutor
- **Lazy Summary Generation**: Only generates AI summaries when viewing profiles
- **Efficient Embeddings**: Batch processing for multiple resumes
- **Memory Management**: Proper file handling and cleanup

### Expected Performance
- **Small Batch (5-10 resumes)**: 10-30 seconds
- **Medium Batch (10-20 resumes)**: 30-60 seconds
- **Large Batch (20+ resumes)**: 60+ seconds

## 🐛 Troubleshooting

### Common Issues

1. **"GEMINI_API_KEY not found"**
   - Ensure `.env` file exists and contains your API key
   - Check for typos in the environment variable name

2. **PDF not displaying**
   - Verify PDF file is not corrupted
   - Check file size (should be < 10MB)
   - Ensure proper file permissions

3. **Slow performance**
   - Check internet connection (for Gemini API calls)
   - Reduce number of simultaneous uploads
   - Monitor logs for specific bottlenecks

4. **Import errors**
   - Verify all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility (3.8+)

### Logging

The app includes comprehensive logging for debugging:
- Performance timing for each operation
- File processing status
- API call success/failure
- Error details with stack traces

View logs in the terminal where you run the app.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini API** for AI embeddings and summaries
- **Streamlit** for the web framework
- **PyMuPDF** for PDF processing
- **scikit-learn** for similarity calculations

---

**Built for efficient resume matching and candidate evaluation** 🚀
