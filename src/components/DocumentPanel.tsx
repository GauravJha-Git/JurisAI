import React, { useRef } from 'react';
import { Upload, FileText, Eye, Search, Download, File } from 'lucide-react';

const DocumentPanel = ({ onFileUpload, onDocumentAction, uploadedFile, documentPreview, isLoading }) => {
  const fileInputRef = useRef(null);

  const handleFileSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      onFileUpload(file);
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const file = e.dataTransfer.files[0];
    if (file) {
      onFileUpload(file);
    }
  };

  return (
    <div className="h-full flex flex-col bg-navy-950">
      {/* Panel Header */}
      <div className="bg-navy-900 px-4 py-3 border-b border-navy-800 flex-shrink-0">
        <div className="flex items-center space-x-3">
          <FileText className="w-4 h-4 text-primary-400" />
          <h2 className="text-base font-semibold text-white">Document Analysis</h2>
        </div>
      </div>

      {/* Upload Area */}
      <div className="p-4 flex-shrink-0">
        <div
          className="border-2 border-dashed border-navy-700 hover:border-primary-600 rounded-xl p-4 text-center transition-colors duration-200 cursor-pointer"
          onClick={() => fileInputRef.current?.click()}
          onDragOver={handleDragOver}
          onDrop={handleDrop}
        >
          <input
            ref={fileInputRef}
            type="file"
            onChange={handleFileSelect}
            accept=".pdf,.docx,.txt"
            className="hidden"
          />
          
          {uploadedFile ? (
            <div className="space-y-2">
              <div className="flex items-center justify-center w-10 h-10 bg-primary-600 rounded-lg mx-auto">
                <File className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="text-white font-medium text-sm">{uploadedFile.name}</p>
                <p className="text-gray-400 text-xs">
                  {(uploadedFile.size / 1024).toFixed(1)} KB • {uploadedFile.type}
                </p>
              </div>
            </div>
          ) : (
            <div className="space-y-2">
              <div className="flex items-center justify-center w-10 h-10 bg-navy-800 rounded-lg mx-auto">
                <Upload className="w-5 h-5 text-gray-400" />
              </div>
              <div>
                <p className="text-white font-medium text-sm">Upload Document</p>
                <p className="text-gray-400 text-xs">
                  Drag & drop or click to select
                </p>
                <p className="text-gray-500 text-xs mt-1">
                  Supports PDF, DOCX, TXT
                </p>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Action Buttons */}
      {uploadedFile && (
        <div className="px-4 space-y-2 flex-shrink-0">
          <button
            onClick={() => onDocumentAction('summarize')}
            disabled={isLoading}
            className="w-full bg-gradient-to-r from-primary-600 to-primary-700 hover:from-primary-700 hover:to-primary-800 disabled:from-gray-600 disabled:to-gray-700 text-white rounded-lg px-3 py-2 transition-all duration-200 disabled:opacity-50 flex items-center justify-center space-x-2 text-sm"
          >
            <Eye className="w-4 h-4" />
            <span>Summarize Document</span>
          </button>
          
          <button
            onClick={() => onDocumentAction('highlight')}
            disabled={isLoading}
            className="w-full bg-navy-800 hover:bg-navy-700 border border-navy-700 hover:border-primary-600 text-white rounded-lg px-3 py-2 transition-all duration-200 disabled:opacity-50 flex items-center justify-center space-x-2 text-sm"
          >
            <Search className="w-4 h-4" />
            <span>Explore Legal Terms</span>
          </button>
        </div>
      )}

      {/* Document Preview */}
      {documentPreview && (
        <div className="flex-1 p-4 pt-3 min-h-20">
          <div className="bg-navy-900 border border-navy-800 rounded-lg h-100 flex flex-col">
            <div className="p-3 border-b border-navy-800 flex-shrink-0">
              <h3 className="text-sm font-semibold text-white flex items-center space-x-2">
                <FileText className="w-4 h-4" />
                <span>Document Preview</span>
              </h3>
            </div>
            <div className="p-3 flex-1 overflow-y-auto min-h-10">
              <pre className="text-xs text-gray-300 whitespace-pre-wrap font-mono leading-relaxed">
                {documentPreview}
              </pre>
            </div>
          </div>
        </div>
      )}

      {/* Tips */}
      <div className="p-4 pt-3 flex-shrink-0">
        <div className="bg-navy-900 border border-navy-800 rounded-lg p-3">
          <h4 className="text-sm font-semibold text-white mb-2">💡 Tips</h4>
          <ul className="text-xs text-gray-400 space-y-1">
            <li>• Upload legal documents for analysis</li>
            <li>• Get plain-language summaries</li>
            <li>• Identify key legal terms</li>
            <li>• Find relevant law sections</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default DocumentPanel;