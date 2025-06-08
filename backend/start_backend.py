"""
Backend startup script for JurisAI
Run this to start the Flask development server
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False
    return True

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    os.makedirs("uploads", exist_ok=True)
    print("✅ Directories created!")

def start_server():
    """Start the Flask server"""
    print("🚀 Starting JurisAI Backend Server...")
    print("🌐 Server will be available at: http://localhost:5000")
    print("📚 API Endpoints:")
    print("   • POST /ask - Ask legal questions")
    print("   • POST /summarize - Summarize documents")
    print("   • POST /highlight-terms - Find legal terms")
    print("   • POST /search-cases - Search case studies")
    print("   • GET /health - Health check")
    print("\n" + "="*50)
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped gracefully")
    except Exception as e:
        print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    print("🏛️  JurisAI Backend Initialization")
    print("="*40)
    
    if install_requirements():
        create_directories()
        start_server()
    else:
        print("❌ Failed to initialize backend")
        sys.exit(1)