# JurisAI - Decode Law, The Smart Way

A full-stack AI-powered legal assistant web application designed to help users understand Indian laws, analyze legal documents, and get answers to legal questions.

## 🏛️ Features

### Frontend (React + Tailwind CSS)
- **Split Layout Design**: 70% chat interface, 30% document panel
- **AI Chat Interface**: Interactive legal Q&A with preset questions
- **Document Upload**: Support for PDF, DOCX, and TXT files
- **Document Analysis**: Summarization and legal term highlighting
- **Dark Theme**: Professional navy blue color scheme
- **Responsive Design**: Mobile-friendly interface

### Backend (Flask + Python)
- **RESTful API**: Comprehensive endpoints for legal assistance
- **Document Processing**: PDF and DOCX text extraction
- **SQLite Database**: Storage for queries and document summaries
- **Legal Knowledge Base**: Indian Penal Code, IT Act, Consumer Protection Act
- **Mock Case Studies**: Sample legal precedents and judgments

## 🚀 Quick Start

### Prerequisites
- Node.js (v16 or higher)
- Python (v3.8 or higher)
- pip (Python package manager)

### Frontend Setup
```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Start Flask server
python app.py
```

Or use the automated startup script:
```bash
cd backend
python start_backend.py
```

## 📚 API Documentation

### Endpoints

#### `POST /ask`
Ask legal questions and get AI-powered answers.
```json
{
  "question": "What are my rights in a cybercrime case?"
}
```

#### `POST /summarize`
Upload and summarize legal documents.
- **Content-Type**: `multipart/form-data`
- **File**: PDF, DOCX, or TXT document

#### `POST /highlight-terms`
Identify and explain legal terms in documents.
- **Content-Type**: `multipart/form-data`
- **File**: PDF, DOCX, or TXT document

#### `POST /search-cases`
Search for relevant legal case studies.
```json
{
  "keyword": "murder"
}
```

#### `GET /health`
Health check endpoint for server status.

## 🎨 Design System

### Colors
- **Primary**: Navy Blue (#1e293b)
- **Background**: Dark Navy (#0f172a, #020617)
- **Accent**: Blue (#0ea5e9)
- **Text**: White/Gray spectrum

### Typography
- **Font**: Inter (Google Fonts)
- **Weights**: 300, 400, 500, 600, 700

### Components
- **Cards**: Rounded corners with subtle shadows
- **Buttons**: Gradient backgrounds with hover effects
- **Inputs**: Dark theme with focus states
- **Icons**: Lucide React icon library

## 🏗️ Architecture

### Frontend Structure
```
src/
├── components/
│   ├── Header.tsx          # App header with branding
│   ├── ChatInterface.tsx   # Main chat UI component
│   └── DocumentPanel.tsx   # Document upload and preview
├── App.tsx                 # Main application component
└── main.tsx               # React entry point
```

### Backend Structure
```
backend/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── sample_data.py     # Legal knowledge base
├── start_backend.py   # Automated startup script
└── uploads/           # Temporary file storage
```

## 📖 Legal Knowledge Base

### Covered Laws
- **Indian Penal Code (IPC)**: Sections 302, 376, 378, 420, 498A
- **Information Technology Act**: Sections 66, 66C
- **Consumer Protection Act 2019**: Rights and procedures
- **Criminal Procedure Code**: Investigation procedures

### Sample Cases
- Criminal law precedents
- Cybercrime prosecutions
- Consumer dispute resolutions
- Domestic violence cases

## 🔧 Development

### Adding New Legal Content
1. Update `INDIAN_LAWS` dictionary in `app.py`
2. Add new cases to `MOCK_CASES` array
3. Extend legal terms in document analysis

### Frontend Customization
1. Modify color scheme in `tailwind.config.js`
2. Update components in `src/components/`
3. Add new preset questions in `ChatInterface.tsx`

### Backend Extensions
1. Add new API endpoints in `app.py`
2. Extend database schema for additional features
3. Integrate external legal APIs

## 🚢 Deployment

### Frontend (Vercel)
```bash
npm run build
# Deploy dist/ folder to Vercel
```

### Backend (Render/Railway)
```bash
# Ensure requirements.txt is up to date
pip freeze > requirements.txt
# Deploy to Render or Railway
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Legal Disclaimer

This application provides general legal information and should not be considered as professional legal advice. Always consult with qualified legal professionals for specific legal matters.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the documentation
- Review API endpoints for integration

---

**JurisAI** - Making legal knowledge accessible to everyone 🏛️✨