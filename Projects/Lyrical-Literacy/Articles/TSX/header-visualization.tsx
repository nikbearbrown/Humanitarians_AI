import React from 'react';
import { Music, Calculator, Brain } from 'lucide-react';

const HeaderVisualization = () => {
  return (
    <div className="flex flex-col items-center justify-center w-full bg-gradient-to-r from-indigo-100 to-purple-100 p-6 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold text-gray-800 mb-6">The Sound of Numbers</h2>
      
      <div className="flex items-center justify-center space-x-4 md:space-x-8 mb-4">
        <div className="flex flex-col items-center">
          <Music size={48} className="text-indigo-600 mb-2" />
          <span className="text-sm text-gray-700">Music</span>
        </div>
        
        <div className="w-20 h-0.5 bg-gradient-to-r from-indigo-500 to-purple-500"></div>
        
        <div className="flex flex-col items-center">
          <Brain size={48} className="text-purple-600 mb-2" />
          <span className="text-sm text-gray-700">Neural Networks</span>
        </div>
        
        <div className="w-20 h-0.5 bg-gradient-to-r from-purple-500 to-blue-500"></div>
        
        <div className="flex flex-col items-center">
          <Calculator size={48} className="text-blue-600 mb-2" />
          <span className="text-sm text-gray-700">Mathematics</span>
        </div>
      </div>
      
      <p className="text-center text-gray-600 max-w-2xl">
        Exploring the cognitive connections between musical training and mathematical ability,
        and the complex relationship that could reshape education
      </p>
    </div>
  );
};

export default HeaderVisualization;