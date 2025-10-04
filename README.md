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



Install dependencies:

- Supports PDF and DOCX resume formats

pip install -r requirements.txt

- Uses Google Gemini AI for semantic matching

Create .env file with your Gemini API key:

- Ranks candidates by similarity score- Upload multiple resumes (PDF/DOCX format)

GEMINI_API_KEY=your_key_here

- Generates AI summaries explaining candidate fit

Get API key from: https://aistudio.google.com/app/apikey

- Password protected with rate limiting- AI-powered semantic matching using Google Gemini

## Usage

- Processes multiple resumes in parallel

Run the app:

- Automatic candidate ranking by relevance## Features## ✨ Features

streamlit run app.py

## Installation

Open browser to http://localhost:8501

- AI-generated fit summaries for each candidate

## How It Works

Install dependencies:

1. Extracts text from PDF/DOCX files

2. Generates embeddings using Gemini API- Password-protected access

3. Calculates cosine similarity between job description and resumes

4. Ranks candidates by similarity scorepip install -r requirements.txt

5. Generates AI summaries for top candidates on-demand

- Rate limiting (5 batches/hour, 20/day per user)

## Tech Stack

Create .env file with your Gemini API key:

- Streamlit - Web interface

- Google Gemini AI - Embeddings and text generation- 📄 Upload multiple resumes (PDF/DOCX)### 🎯 Core Functionality

- Scikit-learn - Cosine similarity calculation

- PyMuPDF - PDF text extractionGEMINI_API_KEY=your_key_here

- python-docx - DOCX text extraction

## Installation

## Security

Get API key from: https://aistudio.google.com/app/apikey

- Password authentication

- Rate limiting: 5 batches per hour, 20 per day- 🤖 AI-powered similarity matching with Google Gemini- **Multi-format Support**: Upload PDF and DOCX resume files

- Usage logging

- API quota protection## Usage



## Project Structure1. Clone the repository



app.py - Main application with password protection and rate limitingRun the app:

gemini_api.py - Gemini API integration for embeddings and summaries

matcher.py - Resume ranking logic using cosine similarity```bash- 📊 Ranked candidate results with match scores- **AI-Powered Matching**: Uses Gemini embeddings for semantic similarity

utils.py - PDF and DOCX text extraction

logger.py - Logging configurationstreamlit run app.py

tests/ - Unit tests

git clone https://github.com/Abhinav-SU/resume-matcher-app.git

## License

Open browser to http://localhost:8501

MIT

cd resume-matcher-app- 💡 AI-generated summaries explaining candidate fit- **Smart Ranking**: Cosine similarity algorithm ranks candidates by relevance

## How It Works

```

1. Extracts text from PDF/DOCX files

2. Generates embeddings using Gemini API- 🔒 Password-protected access- **Top 10 Results**: Displays the most relevant candidates with similarity scores

3. Calculates cosine similarity between job description and resumes

4. Ranks candidates by similarity score2. Install dependencies

5. Generates AI summaries for top candidates on-demand

```bash- ⏱️ Rate limiting to prevent abuse

## Tech Stack

pip install -r requirements.txt

- Streamlit - Web interface

- Google Gemini AI - Embeddings and text generation```### 🚀 Performance Optimizations

- Scikit-learn - Cosine similarity calculation

- PyMuPDF - PDF text extraction

- python-docx - DOCX text extraction

3. Set up environment variables## Quick Start- **Parallel Processing**: ThreadPoolExecutor for faster resume parsing

## Security

```bash

- Password authentication

- Rate limiting: 5 batches per hour, 20 per day# Create .env file- **Lazy Loading**: AI summaries generated only when viewing candidate profiles

- Usage logging

- API quota protectionGEMINI_API_KEY=your_api_key_here



## Project Structure```### 1. Install Dependencies- **Efficient File Handling**: Optimized text extraction and caching



app.py - Main application with password protection and rate limiting

gemini_api.py - Gemini API integration for embeddings and summaries

matcher.py - Resume ranking logic using cosine similarityGet your API key from: https://aistudio.google.com/app/apikey- **Comprehensive Logging**: Performance monitoring and debugging

utils.py - PDF and DOCX text extraction

logger.py - Logging configuration

tests/ - Unit tests

4. Configure password (optional)```bash

## License

```bash

MIT

# Edit .streamlit/secrets.tomlpython -m venv .venv### 🎨 User Experience

app_password = "your_password"

```.venv\Scripts\activate  # Windows- **Clean Table Layout**: Professional ranking display with clear metrics



## Usagepip install -r requirements.txt- **Interactive Profiles**: Click-to-view detailed candidate information



Run the application:```- **File Preview**: PDF embedding + DOCX text view

```bash

streamlit run app.py- **Download Functionality**: Easy access to original resume files

```

### 2. Set Up API Key- **Responsive Design**: Wide layout optimized for better viewing

Open your browser to `http://localhost:8501`



## Tech Stack

Create a `.env` file:## 🛠️ Tech Stack

- **Python 3.11+**

- **Streamlit** - Web framework```

- **Google Gemini AI** - Embeddings and summaries

- **Scikit-learn** - Similarity scoringGEMINI_API_KEY=your_gemini_api_key_here- **Frontend**: Streamlit 1.35.0

- **PyMuPDF** - PDF processing

- **python-docx** - DOCX processing```- **AI/ML**: Google Gemini API (embeddings + summaries)



## Project Structure- **Similarity**: scikit-learn (cosine similarity)



```Get your free API key from: https://aistudio.google.com/app/apikey- **File Processing**: PyMuPDF (PDF), python-docx (DOCX)

resume-matcher-app/

├── app.py              # Main application- **Configuration**: python-dotenv

├── gemini_api.py       # Gemini API integration

├── matcher.py          # Resume ranking logic### 3. Configure Password

├── utils.py            # File processing utilities

├── logger.py           # Logging configuration## 📦 Installation

├── requirements.txt    # Dependencies

└── tests/              # Unit testsEdit `.streamlit/secrets.toml`:

```

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
