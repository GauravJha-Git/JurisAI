import React, { useState, useRef, useEffect } from 'react';
import ChatInterface from './components/ChatInterface';
import DocumentPanel from './components/DocumentPanel';
import Header from './components/Header';

function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'bot',
      content: 'Hello! I\'m JurisAI, your legal assistant. I can help you understand Indian laws, analyze legal documents, and answer your legal questions. How can I assist you today?',
      timestamp: new Date().toLocaleTimeString()
    }
  ]);
  const [uploadedFile, setUploadedFile] = useState(null);
  const [documentPreview, setDocumentPreview] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (message) => {
    const newMessage = {
      id: Date.now(),
      type: 'user',
      content: message,
      timestamp: new Date().toLocaleTimeString()
    };
    
    setMessages(prev => [...prev, newMessage]);
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question: message }),
      });

      const data = await response.json();
      
      const botMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: data.answer || 'I apologize, but I\'m having trouble processing your request right now. Please try again.',
        timestamp: new Date().toLocaleTimeString()
      };
      
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        type: 'bot',
        content: 'I\'m currently unable to connect to the backend. Please ensure the Flask server is running on port 5000.',
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFileUpload = (file) => {
    setUploadedFile(file);
    // Create a preview of the file
    const reader = new FileReader();
    reader.onload = (e) => {
      if (file.type === 'text/plain') {
        setDocumentPreview(e.target.result);
      } else {
        setDocumentPreview(`File uploaded: ${file.name} (${file.type})`);
      }
    };
    reader.readAsText(file);
  };

  const handleDocumentAction = async (action) => {
    if (!uploadedFile) return;

    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', uploadedFile);

    try {
      const endpoint = action === 'summarize' ? '/summarize' : '/highlight-terms';
      const response = await fetch(`http://localhost:5000${endpoint}`, {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      
      const resultMessage = {
        id: Date.now(),
        type: 'bot',
        content: action === 'summarize' ? data.summary : data.highlighted_terms,
        timestamp: new Date().toLocaleTimeString()
      };
      
      setMessages(prev => [...prev, resultMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now(),
        type: 'bot',
        content: 'Error processing document. Please ensure the Flask server is running.',
        timestamp: new Date().toLocaleTimeString()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="h-screen w-screen bg-navy-950 text-white overflow-hidden">
      <Header />
      <div className="flex h-[calc(100vh-60px)]">
        <div className="w-[70%] border-r border-navy-800">
          <ChatInterface
            messages={messages}
            onSendMessage={handleSendMessage}
            isLoading={isLoading}
          />
        </div>
        <div className="w-[30%]">
          <DocumentPanel
            onFileUpload={handleFileUpload}
            onDocumentAction={handleDocumentAction}
            uploadedFile={uploadedFile}
            documentPreview={documentPreview}
            isLoading={isLoading}
          />
        </div>
      </div>
    </div>
  );
}

export default App;