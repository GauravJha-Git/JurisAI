import React, { useState, useRef, useEffect } from 'react';
import { Send, MessageSquare, Scale, FileText, Gavel, Shield } from 'lucide-react';

const ChatInterface = ({ messages, onSendMessage, isLoading }) => {
  const [inputMessage, setInputMessage] = useState('');
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const presetQuestions = [
    {
      icon: Shield,
      text: "What are my rights in a cybercrime case?",
      category: "Cybercrime"
    },
    {
      icon: Gavel,
      text: "Explain IPC Section 302",
      category: "Criminal Law"
    },
    {
      icon: FileText,
      text: "What law applies in a theft case?",
      category: "Property Law"
    },
    {
      icon: Scale,
      text: "How to file a consumer complaint?",
      category: "Consumer Law"
    }
  ];

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputMessage.trim() && !isLoading) {
      onSendMessage(inputMessage.trim());
      setInputMessage('');
    }
  };

  const handlePresetQuestion = (question) => {
    if (!isLoading) {
      onSendMessage(question);
    }
  };

  return (
    <div className="flex flex-col h-full bg-navy-950">
      {/* Chat Header */}
      <div className="bg-navy-900 px-4 py-3 border-b border-navy-800 flex-shrink-0">
        <div className="flex items-center space-x-3">
          <MessageSquare className="w-4 h-4 text-primary-400" />
          <h2 className="text-base font-semibold text-white">Legal Assistant Chat</h2>
        </div>
      </div>

      {/* Messages Area - Expanded */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4 min-h-0">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[85%] rounded-2xl px-4 py-3 ${
                message.type === 'user'
                  ? 'bg-gradient-to-r from-primary-600 to-primary-700 text-white'
                  : 'bg-navy-800 text-gray-100 border border-navy-700'
              }`}
            >
              <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
              <p className={`text-xs mt-2 ${
                message.type === 'user' ? 'text-primary-100' : 'text-gray-400'
              }`}>
                {message.timestamp}
              </p>
            </div>
          </div>
        ))}
        
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-navy-800 border border-navy-700 rounded-2xl px-4 py-3">
              <div className="flex items-center space-x-2">
                <div className="flex space-x-1">
                  <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce"></div>
                  <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                  <div className="w-2 h-2 bg-primary-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                </div>
                <span className="text-sm text-gray-400">JurisAI is thinking...</span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Preset Questions - Minimized */}
      <div className="px-4 py-2 border-t border-navy-800 flex-shrink-0">
        <p className="text-xs text-gray-400 mb-2">Quick questions:</p>
        <div className="grid grid-cols-2 gap-2">
          {presetQuestions.map((question, index) => {
            const IconComponent = question.icon;
            return (
              <button
                key={index}
                onClick={() => handlePresetQuestion(question.text)}
                disabled={isLoading}
                className="text-left p-2 bg-navy-800 hover:bg-navy-700 border border-navy-700 hover:border-primary-600 rounded-lg transition-all duration-200 disabled:opacity-50 group"
              >
                <div className="flex items-center space-x-2 mb-1">
                  <IconComponent className="w-3 h-3 text-primary-400 group-hover:text-primary-300" />
                  <span className="text-xs text-primary-400 font-medium">{question.category}</span>
                </div>
                <p className="text-xs text-gray-200 group-hover:text-white line-clamp-2">{question.text}</p>
              </button>
            );
          })}
        </div>
      </div>

      {/* Input Area */}
      <div className="p-4 border-t border-navy-800 flex-shrink-0">
        <form onSubmit={handleSubmit} className="flex space-x-3">
          <input
            ref={inputRef}
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Ask your legal question..."
            disabled={isLoading}
            className="flex-1 bg-navy-800 border border-navy-700 rounded-xl px-4 py-3 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent disabled:opacity-50"
          />
          <button
            type="submit"
            disabled={!inputMessage.trim() || isLoading}
            className="bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 disabled:from-gray-600 disabled:to-gray-700 text-white rounded-xl px-6 py-3 transition-all duration-200 disabled:opacity-50 flex items-center space-x-2"
          >
            <Send className="w-4 h-4" />
            <span>Send</span>
          </button>
        </form>
      </div>
    </div>
  );
};

export default ChatInterface;