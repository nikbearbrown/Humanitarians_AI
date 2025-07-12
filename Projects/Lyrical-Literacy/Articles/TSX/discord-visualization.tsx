import React from 'react';
import { AlertTriangle, LineChart, Users, BarChart } from 'lucide-react';

const DiscordVisualization = () => {
  return (
    <div className="bg-gray-50 rounded-lg shadow-md p-6">
      <h3 className="text-xl font-semibold text-center mb-6">Discord in the Data</h3>
      
      <div className="flex flex-col items-center">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 w-full max-w-4xl mb-6">
          {/* Correlation vs. Causation */}
          <div className="bg-white p-4 rounded-lg border border-red-200">
            <div className="flex items-center mb-3">
              <AlertTriangle size={20} className="text-red-500 mr-2" />
              <h4 className="text-lg font-medium text-gray-800">Correlation vs. Causation</h4>
            </div>
            
            <div className="relative h-32 mb-3">
              {/* Visualization of correlation vs causation */}
              <svg className="w-full h-full" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
                {/* Correlation lines */}
                <line x1="30" y1="80" x2="170" y2="20" stroke="#9333ea" strokeWidth="2" strokeDasharray="5,5" />
                
                {/* Musical ability dots */}
                <g className="musical-ability-dots">
                  <circle cx="40" cy="70" r="4" fill="#818cf8" />
                  <circle cx="60" cy="65" r="4" fill="#818cf8" />
                  <circle cx="80" cy="55" r="4" fill="#818cf8" />
                  <circle cx="100" cy="50" r="4" fill="#818cf8" />
                  <circle cx="120" cy="40" r="4" fill="#818cf8" />
                  <circle cx="140" cy="30" r="4" fill="#818cf8" />
                  <circle cx="160" cy="25" r="4" fill="#818cf8" />
                </g>
                
                {/* Question marks showing uncertainty about causation */}
                <text x="50" y="40" fill="#ef4444" fontSize="12" fontWeight="bold">?</text>
                <text x="90" y="35" fill="#ef4444" fontSize="12" fontWeight="bold">?</text>
                <text x="130" y="20" fill="#ef4444" fontSize="12" fontWeight="bold">?</text>
                
                {/* Labels */}
                <text x="20" y="95" fill="#6b7280" fontSize="8">Musical Ability</text>
                <text x="140" y="95" fill="#6b7280" fontSize="8">Math Performance</text>
              </svg>
            </div>
            
            <p className="text-sm text-gray-600">
              Studies show correlation between music training and math skills, but causation remains unproven.
            </p>
          </div>
          
          {/* Self-Selection Bias */}
          <div className="bg-white p-4 rounded-lg border border-amber-200">
            <div className="flex items-center mb-3">
              <Users size={20} className="text-amber-500 mr-2" />
              <h4 className="text-lg font-medium text-gray-800">Self-Selection Bias</h4>
            </div>
            
            <div className="relative h-32 mb-3">
              {/* Visualization of self-selection bias */}
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="relative w-full max-w-xs">
                  <div className="absolute top-0 left-1/2 transform -translate-x-1/2 w-24 h-24 rounded-full border-2 border-dashed border-amber-300 flex items-center justify-center">
                    <div className="text-xs text-center text-gray-500">Pre-existing<br/>Advantages</div>
                  </div>
                  
                  <div className="absolute top-6 left-6 w-20 h-20 rounded-full bg-blue-100 border border-blue-200 flex items-center justify-center">
                    <div className="text-xs text-center text-blue-800">Music<br/>Students</div>
                  </div>
                  
                  <div className="absolute top-10 right-6 w-16 h-16 rounded-full bg-amber-100 border border-amber-200 flex items-center justify-center">
                    <div className="text-xs text-center text-amber-800">Math<br/>Performance</div>
                  </div>
                  
                  <svg className="absolute inset-0" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">
                    <path d="M70,40 C80,30 100,30 110,40" stroke="#9333ea" strokeWidth="1.5" fill="none" />
                    <text x="80" y="25" fill="#9333ea" fontSize="8">?</text>
                  </svg>
                </div>
              </div>
            </div>
            
            <p className="text-sm text-gray-600">
              Students who pursue music may already have cognitive advantages or supportive environments.
            </p>
          </div>
        </div>
        
        <div className="bg-white p-4 rounded-lg border border-blue-200 w-full max-w-4xl">
          <div className="flex items-center mb-3">
            <BarChart size={20} className="text-blue-500 mr-2" />
            <h4 className="text-lg font-medium text-gray-800">Methodological Limitations</h4>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="bg-blue-50 p-3 rounded-lg">
              <h5 className="text-sm font-medium text-blue-900 mb-2">Cross-Sectional Design</h5>
              <div className="flex justify-center mb-2">
                <svg width="80" height="40" xmlns="http://www.w3.org/2000/svg">
                  <line x1="10" y1="20" x2="70" y2="20" stroke="#3b82f6" strokeWidth="2" />
                  <circle cx="40" cy="20" r="8" fill="#93c5fd" stroke="#3b82f6" strokeWidth="1.5" />
                  <text x="36" y="23" fill="#1e40af" fontSize="10">?</text>
                </svg>
              </div>
              <p className="text-xs text-gray-600">Cannot establish causality with single timepoint measurements</p>
            </div>
            
            <div className="bg-blue-50 p-3 rounded-lg">
              <h5 className="text-sm font-medium text-blue-900 mb-2">Sample Size</h5>
              <div className="flex justify-center mb-2">
                <svg width="80" height="40" xmlns="http://www.w3.org/2000/svg">
                  <rect x="10" y="10" width="15" height="25" fill="#93c5fd" />
                  <rect x="33" y="15" width="15" height="20" fill="#93c5fd" />
                  <rect x="56" y="20" width="15" height="15" fill="#93c5fd" />
                  <text x="13" y="25" fill="#1e40af" fontSize="10">n=?</text>
                </svg>
              </div>
              <p className="text-xs text-gray-600">Many studies have relatively small sample sizes</p>
            </div>
            
            <div className="bg-blue-50 p-3 rounded-lg">
              <h5 className="text-sm font-medium text-blue-900 mb-2">Control Variables</h5>
              <div className="flex justify-center mb-2">
                <svg width="80" height="40" xmlns="http://www.w3.org/2000/svg">
                  <circle cx="20" cy="20" r="5" fill="#93c5fd" />
                  <circle cx="40" cy="20" r="5" fill="#93c5fd" />
                  <circle cx="60" cy="20" r="5" fill="#93c5fd" />
                  <text x="18" y="35" fill="#1e40af" fontSize="6">SES</text>
                  <text x="35" y="35" fill="#1e40af" fontSize="6">Education</text>
                  <text x="56" y="35" fill="#1e40af" fontSize="6">Cognition</text>
                </svg>
              </div>
              <p className="text-xs text-gray-600">Confounding variables not always adequately controlled</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DiscordVisualization;