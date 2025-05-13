import React from 'react';
import { Music, Clock, ChevronRight } from 'lucide-react';

const RhythmMethodVisualization = () => {
  return (
    <div className="bg-gray-50 rounded-lg shadow-md p-6">
      <h3 className="text-xl font-semibold text-center mb-6">The Rhythm Method</h3>
      
      <div className="flex flex-col items-center">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl mb-8">
          {/* Active Music Engagement */}
          <div className="bg-indigo-50 p-4 rounded-lg relative">
            <div className="absolute -top-4 left-4 bg-indigo-600 text-white rounded-full w-8 h-8 flex items-center justify-center shadow-md">
              <Music size={18} />
            </div>
            <h4 className="text-lg font-medium text-indigo-900 mt-2 mb-4">Active Engagement</h4>
            
            <div className="flex items-start mb-3">
              <div className="bg-indigo-200 rounded p-2 mr-3">
                <Music size={20} className="text-indigo-700" />
              </div>
              <div>
                <p className="text-sm text-gray-700">Instrumental Training</p>
                <div className="w-full bg-gray-200 rounded-full h-2 mt-1">
                  <div className="bg-indigo-600 h-2 rounded-full w-4/5"></div>
                </div>
              </div>
            </div>
            
            <div className="border-l-2 border-indigo-200 pl-3 ml-2 mt-3">
              <p className="text-sm text-gray-600">Substantial & long-lasting benefits</p>
              <p className="text-xs text-gray-500 mt-1">Enhanced pattern recognition, structural analysis, executive function</p>
            </div>
          </div>
          
          {/* Passive Music Exposure */}
          <div className="bg-blue-50 p-4 rounded-lg relative">
            <div className="absolute -top-4 left-4 bg-blue-600 text-white rounded-full w-8 h-8 flex items-center justify-center shadow-md">
              <Clock size={18} />
            </div>
            <h4 className="text-lg font-medium text-blue-900 mt-2 mb-4">Passive Listening</h4>
            
            <div className="flex items-start mb-3">
              <div className="bg-blue-200 rounded p-2 mr-3">
                <Clock size={20} className="text-blue-700" />
              </div>
              <div>
                <p className="text-sm text-gray-700">"Mozart Effect"</p>
                <div className="w-full bg-gray-200 rounded-full h-2 mt-1">
                  <div className="bg-blue-600 h-2 rounded-full w-2/5"></div>
                </div>
              </div>
            </div>
            
            <div className="border-l-2 border-blue-200 pl-3 ml-2 mt-3">
              <p className="text-sm text-gray-600">Temporary enhancement</p>
              <p className="text-xs text-gray-500 mt-1">Brief improvement in spatial-temporal reasoning</p>
            </div>
          </div>
        </div>
        
        <div className="bg-gradient-to-r from-indigo-50 to-yellow-50 p-4 rounded-lg w-full max-w-4xl">
          <h4 className="text-lg font-medium text-gray-800 mb-3">Application Examples</h4>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            <div className="bg-white bg-opacity-70 p-3 rounded shadow-sm">
              <div className="flex items-center mb-2">
                <div className="w-2 h-2 bg-indigo-500 rounded-full mr-2"></div>
                <h5 className="text-sm font-medium">Rhythmic Training</h5>
              </div>
              <p className="text-xs text-gray-600">Fraction relationships through rhythmic notation</p>
            </div>
            
            <div className="bg-white bg-opacity-70 p-3 rounded shadow-sm">
              <div className="flex items-center mb-2">
                <div className="w-2 h-2 bg-purple-500 rounded-full mr-2"></div>
                <h5 className="text-sm font-medium">Melodic Patterns</h5>
              </div>
              <p className="text-xs text-gray-600">Algebraic thinking through musical sequences</p>
            </div>
            
            <div className="bg-white bg-opacity-70 p-3 rounded shadow-sm">
              <div className="flex items-center mb-2">
                <div className="w-2 h-2 bg-yellow-500 rounded-full mr-2"></div>
                <h5 className="text-sm font-medium">Movement-Based</h5>
              </div>
              <p className="text-xs text-gray-600">Geometry through spatial positioning in music</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default RhythmMethodVisualization;