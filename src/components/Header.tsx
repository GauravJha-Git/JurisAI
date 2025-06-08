import React from 'react';
import { Scale, Brain, Shield } from 'lucide-react';

const Header = () => {
  return (
    <header className="bg-navy-900 border-b border-navy-800 px-6 py-3 h-[60px] flex items-center">
      <div className="flex items-center justify-between w-full">
        <div className="flex items-center space-x-3">
          <div className="flex items-center justify-center w-8 h-8 bg-gradient-to-br from-primary-600 to-primary-800 rounded-lg">
            <Scale className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="text-lg font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
              JurisAI
            </h1>
            <p className="text-xs text-gray-400">Decode law, the smart way</p>
          </div>
        </div>
        <div className="flex items-center space-x-6">
          <div className="flex items-center space-x-2 text-gray-300">
            <Brain className="w-4 h-4" />
            <span className="text-sm">AI-Powered</span>
          </div>
          <div className="flex items-center space-x-2 text-gray-300">
            <Shield className="w-4 h-4" />
            <span className="text-sm">Secure</span>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;