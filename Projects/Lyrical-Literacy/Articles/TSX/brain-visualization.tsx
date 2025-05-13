import React from 'react';
import { Brain, Activity } from 'lucide-react';

const BrainVisualization = () => {
  return (
    <div className="bg-gray-50 rounded-lg shadow-md p-6">
      <h3 className="text-xl font-semibold text-center mb-6">Harmonious Brains</h3>
      
      <div className="flex flex-col items-center">
        <div className="relative w-64 h-64 mb-6">
          {/* Brain silhouette background */}
          <div className="absolute inset-0 flex justify-center">
            <Brain size={200} className="text-gray-200" />
          </div>
          
          {/* Highlighted brain regions */}
          <div className="absolute top-1/4 left-1/4 w-12 h-12 rounded-full bg-indigo-500 opacity-60 animate-pulse"></div>
          <div className="absolute top-1/3 right-1/4 w-10 h-10 rounded-full bg-purple-500 opacity-60 animate-pulse" style={{animationDelay: '0.5s'}}></div>
          <div className="absolute bottom-1/4 left-1/3 w-14 h-14 rounded-full bg-blue-500 opacity-60 animate-pulse" style={{animationDelay: '1s'}}></div>
          
          {/* Connection lines */}
          <svg className="absolute inset-0" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
            <path d="M100,80 C120,100 140,90 160,110" stroke="#818cf8" strokeWidth="2" fill="none" className="opacity-70" />
            <path d="M160,110 C180,130 160,140 140,160" stroke="#8b5cf6" strokeWidth="2" fill="none" className="opacity-70" />
            <path d="M100,80 C80,100 100,120 110,150" stroke="#3b82f6" strokeWidth="2" fill="none" className="opacity-70" />
          </svg>
        </div>
        
        <div className="grid grid-cols-2 gap-4 w-full max-w-md">
          <div className="flex items-center bg-indigo-100 p-3 rounded">
            <div className="w-3 h-3 bg-indigo-500 rounded-full mr-2"></div>
            <span className="text-sm">Left Inferior Parietal</span>
          </div>
          
          <div className="flex items-center bg-purple-100 p-3 rounded">
            <div className="w-3 h-3 bg-purple-500 rounded-full mr-2"></div>
            <span className="text-sm">Prefrontal Cortex</span>
          </div>
          
          <div className="flex items-center bg-blue-100 p-3 rounded">
            <div className="w-3 h-3 bg-blue-500 rounded-full mr-2"></div>
            <span className="text-sm">Temporal Regions</span>
          </div>
          
          <div className="flex items-center bg-gray-100 p-3 rounded">
            <Activity size={16} className="text-gray-500 mr-2" />
            <span className="text-sm">Stronger Connectivity</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BrainVisualization;