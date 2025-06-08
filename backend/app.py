from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os
import json
from datetime import datetime
import PyPDF2
import docx
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
def init_db():
    conn = sqlite3.connect('jurisai.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            summary TEXT,
            legal_terms TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# Sample Indian law data
INDIAN_LAWS = {
    "IPC 302": "Section 302 of the Indian Penal Code deals with punishment for murder. Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.",
    "IPC 420": "Section 420 of the Indian Penal Code deals with cheating and dishonestly inducing delivery of property. The punishment is imprisonment up to seven years and fine.",
    "IPC 376": "Section 376 of the Indian Penal Code deals with punishment for rape. The punishment is rigorous imprisonment for not less than ten years which may extend to imprisonment for life, and fine.",
    "cybercrime": "Cybercrime in India is primarily governed by the Information Technology Act, 2000. It includes computer-related offenses, data theft, hacking, and online fraud.",
    "theft": "Theft under IPC Section 378 is defined as dishonestly taking movable property out of the possession of another person without consent. Punishment includes imprisonment up to three years or fine or both.",
    "consumer rights": "Consumer rights in India are protected under the Consumer Protection Act, 2019. Consumers have rights to safety, information, choice, representation, and redressal of grievances."
}

MOCK_CASES = [
    {
        "case_name": "State v. Ram Kumar",
        "section": "IPC 302",
        "summary": "Murder case involving domestic violence. Court emphasized the importance of circumstantial evidence.",
        "year": "2023"
    },
    {
        "case_name": "Cyber Cell v. Tech Fraudster",
        "section": "IT Act Section 66",
        "summary": "Online fraud case involving fake investment schemes. Highlights cybercrime investigation procedures.",
        "year": "2022"
    }
]

def extract_text_from_pdf(file_path):
    """Extract text from PDF file"""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_docx(file_path):
    """Extract text from DOCX file"""
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

def extract_text_from_file(file_path, filename):
    """Extract text from uploaded file based on extension"""
    if filename.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif filename.lower().endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif filename.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    else:
        return "Unsupported file format"

@app.route('/ask', methods=['POST'])
def ask_question():
    """Handle legal questions from users"""
    try:
        data = request.get_json()
        question = data.get('question', '').lower()
        
        # Simple keyword matching for legal questions
        answer = "I understand you're asking about a legal matter. "
        
        if any(keyword in question for keyword in ['ipc 302', 'murder', 'section 302']):
            answer += INDIAN_LAWS['IPC 302']
        elif any(keyword in question for keyword in ['ipc 420', 'cheating', 'fraud']):
            answer += INDIAN_LAWS['IPC 420']
        elif any(keyword in question for keyword in ['cybercrime', 'cyber', 'online fraud', 'hacking']):
            answer += INDIAN_LAWS['cybercrime']
        elif any(keyword in question for keyword in ['theft', 'stealing', 'ipc 378']):
            answer += INDIAN_LAWS['theft']
        elif any(keyword in question for keyword in ['consumer', 'complaint', 'consumer rights']):
            answer += INDIAN_LAWS['consumer rights']
        elif any(keyword in question for keyword in ['rape', 'ipc 376', 'sexual assault']):
            answer += INDIAN_LAWS['IPC 376']
        else:
            answer += "Based on your question, I'd recommend consulting with a qualified legal professional for specific advice. However, I can provide general information about Indian laws. Could you please be more specific about which legal area you're interested in? For example: criminal law (IPC sections), cybercrime, consumer protection, or property law."
        
        # Store query in database
        conn = sqlite3.connect('jurisai.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO queries (question, answer) VALUES (?, ?)', 
                      (question, answer))
        conn.commit()
        conn.close()
        
        return jsonify({'answer': answer})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/summarize', methods=['POST'])
def summarize_document():
    """Summarize uploaded legal document"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text from file
        extracted_text = extract_text_from_file(file_path, filename)
        
        # Generate simple summary (in a real app, you'd use more sophisticated NLP)
        text_length = len(extracted_text.split())
        
        if text_length < 100:
            summary = f"This is a short document with approximately {text_length} words. The document appears to contain: {extracted_text[:200]}..."
        else:
            # Simple extractive summarization
            sentences = extracted_text.split('.')[:3]  # Take first 3 sentences
            summary = f"Document Summary ({text_length} words):\n\n" + '. '.join(sentences[:3]) + ".\n\nThis document contains legal text that may require professional interpretation. Key themes appear to relate to legal procedures, rights, or obligations as outlined in the content."
        
        # Store in database
        conn = sqlite3.connect('jurisai.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO documents (filename, summary) VALUES (?, ?)', 
                      (filename, summary))
        conn.commit()
        conn.close()
        
        # Clean up uploaded file
        os.remove(file_path)
        
        return jsonify({'summary': summary})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/highlight-terms', methods=['POST'])
def highlight_legal_terms():
    """Identify and explain legal terms in uploaded document"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Extract text from file
        extracted_text = extract_text_from_file(file_path, filename).lower()
        
        # Legal terms dictionary
        legal_terms = {
            'plaintiff': 'The person who brings a case against another in a court of law',
            'defendant': 'An individual, company, or institution sued or accused in a court of law',
            'affidavit': 'A written statement confirmed by oath or affirmation, for use as evidence in court',
            'bail': 'The temporary release of an accused person awaiting trial, sometimes on condition that a sum of money be lodged as security',
            'petition': 'A formal written request, typically one signed by many people, appealing to authority with respect to a particular cause',
            'jurisdiction': 'The official power to make legal decisions and judgments',
            'summons': 'An order to appear before a judge or magistrate, or the writ containing it',
            'warrant': 'A document issued by a legal or government official authorizing the police or some other body to make an arrest, search premises, or carry out some other action relating to the administration of justice',
            'constitution': 'A body of fundamental principles or established precedents according to which a state or other organization is acknowledged to be governed',
            'amendment': 'A minor change or addition designed to improve a text, piece of legislation, etc.'
        }
        
        # Find legal terms in document
        found_terms = []
        for term, definition in legal_terms.items():
            if term in extracted_text:
                found_terms.append(f"• **{term.title()}**: {definition}")
        
        if not found_terms:
            result = "No common legal terms were identified in this document. The document may contain specialized legal language that requires expert interpretation.\n\nCommon legal concepts to look for include: contracts, agreements, rights, obligations, penalties, jurisdiction, and procedural terms."
        else:
            result = f"**Legal Terms Found in Document:**\n\n" + "\n\n".join(found_terms)
            result += f"\n\n**Relevant Indian Laws:**\nBased on the content, you may want to research:\n• Indian Contract Act, 1872\n• Indian Evidence Act, 1872\n• Code of Civil Procedure, 1908\n• Indian Penal Code, 1860"
        
        # Store in database
        conn = sqlite3.connect('jurisai.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO documents (filename, legal_terms) VALUES (?, ?)', 
                      (filename, result))
        conn.commit()
        conn.close()
        
        # Clean up uploaded file
        os.remove(file_path)
        
        return jsonify({'highlighted_terms': result})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search-cases', methods=['POST'])
def search_cases():
    """Search for relevant legal cases"""
    try:
        data = request.get_json()
        keyword = data.get('keyword', '').lower()
        
        # Simple keyword matching
        relevant_cases = []
        for case in MOCK_CASES:
            if (keyword in case['case_name'].lower() or 
                keyword in case['section'].lower() or 
                keyword in case['summary'].lower()):
                relevant_cases.append(case)
        
        if not relevant_cases:
            relevant_cases = MOCK_CASES  # Return all cases if no matches
        
        return jsonify({'cases': relevant_cases})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'JurisAI backend is running'})

if __name__ == '__main__':
    init_db()
    print("🏛️  JurisAI Backend Server Starting...")
    print("📚 Legal database initialized")
    print("🚀 Server running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)