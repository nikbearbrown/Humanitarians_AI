# Super Agent Visualizer
Super Agent Visualizer is an interactive visual tool for exploring and editing agent-based JSON configurations. Built using Next.js + React + TypeScript, it enables users to import JSON files, visualize agent relationships with React Flow, edit metadata via modals, and export updated configurations with ease.

---

## Features
### Initial Setup
- Initialized with Next.js, React, and TypeScript.
- Installed core dependencies:
    - [`react-flow`](https://reactflow.dev/) for graph rendering.
    - [`tailwindcss`](https://tailwindcss.com/) for utility-first styling.
    - [`react-dropzone`](https://react-dropzone.js.org/) for drag-and-drop JSON file imports.

### JSON Parsing & Visualization
- Defined a custom JSON structure for agents and their relationships.
- Enabled drag-and-drop import of JSON files.
- Rendered agents as nodes and relationships as edges using React Flow.
- Sidebar setup to display agent details (non-editable initially).

### UI & UX
- Improved node styling: icons, colors, and spacing for clarity.
- Sidebar enhancements to prepare for agent editing.
- Enabled node click to open a modal for:
    - Editing `system prompt`
    - Editing `task prompt`
    - Editing `metadata`
- All modal edits trigger live updates to the underlying JSON structure.

### Graph & JSON Management
- Added export functionality to download the updated JSON file.
- Supported undo/redo functionality for editing changes.
- Implemented add/remove relationship feature between agents.
- Applied auto layouting to the graph upon JSON import for better readability.

### Advanced Relationships
- Added support for multiple parent-to-child relationships in the graph structure.

---

## Project Structure
```
super-agent-visualizer/
├── public/                   # Static assets (if any)
├── src/
│   ├── app/                  # Main Next.js routes
│   ├── components/           # UI components (Nodes, Sidebar, Modal, etc.)
│   ├── utils/                # JSON parsing, layout, and helpers
│   ├── style.module.css      # Custom styles
│   ├── types.ts              # Shared TypeScript types
├── test-agents.json          # Sample JSON file

```

---

## Getting Started
1. Clone the repository
```
git clone https://github.com/your-username/super-agent-visualizer.git
cd super-agent-visualizer
```

2. Install dependencies
```
npm install
```

3. Run the development server
```
npm run dev
```

Visit `http://localhost:3000` to view the app in your browser.

---

## JSON Structure Example
Here’s an example of the expected input JSON format:
```
{
  "agents": [
    {
      "agent_id": "agent_1",
      "parent_id": null,
      "related_agents": ["agent_2", "agent_3"],
      "role_name": "Market Research Agent",
      "system_prompt": "Conduct market research for new product launches.",
      "task_prompt": "Analyze market trends and customer preferences.",
      "metadata": {
        "creation_timestamp": "2023-10-01T12:00:00Z",
        "llm_used": "Ollama"
      }
    },
    {
      "agent_id": "agent_2",
      "parent_id": "agent_1",
      "related_agents": ["agent_4"],
      "role_name": "Content Creation Agent",
      "system_prompt": "Create marketing content for campaigns.",
      "task_prompt": "Develop blog posts, social media content, and ads.",
      "metadata": {
        "creation_timestamp": "2023-10-01T12:05:00Z",
        "llm_used": "Ollama"
      }
    },
    {
      "agent_id": "agent_3",
      "parent_id": "agent_1",
      "related_agents": [],
      "role_name": "Budget Planning Agent",
      "system_prompt": "Plan marketing budgets for campaigns.",
      "task_prompt": "Allocate budget for different marketing channels.",
      "metadata": {
        "creation_timestamp": "2023-10-01T12:10:00Z",
        "llm_used": "Ollama"
      }
    }
  ]
}
```

---

## Future Improvements
- Editable sidebar with drag-and-drop field customization.
- Save projects in local storage or cloud.
- Collaborator mode for real-time multi-user editing.
- Integration with LangChain or other agent frameworks.
