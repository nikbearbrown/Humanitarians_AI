# Bear Brown &amp; Co. | Stealth Start-Up Federated Chatbot Development Challenge

**Challenge: Bear Brown & Co. | Stealth Start-Up Federated Chatbot Development Challenge**

**Description:** AI is revolutionizing enterprise operations, and the creation of intelligent, adaptable chatbots is becoming essential. This challenge, sponsored by Bear Brown & Co. in collaboration with a Stealth Start-Up, aims to develop a sophisticated chatbot using VoiceFlow, integrating with an external API. The chatbot should utilize advanced VoiceFlow features such as API integration, custom code blocks, state management, NLP, and LLM integration to create a dynamic, user-friendly conversational agent.

This PDF describes the proect in more detail [https://github.com/nikbearbrown/Stealth_Start-Up_Federated_Chatbot_Development_Challenge/blob/main/Stealth_Start_Up_%20Empowering%20Decision-Making%20Through%20Unified%20AI-v7.pdf](https://github.com/nikbearbrown/Stealth_Start-Up_Federated_Chatbot_Development_Challenge/blob/main/Stealth_Start_Up_%20Empowering%20Decision-Making%20Through%20Unified%20AI-v7.pdf)  

**Objective:** Develop a chatbot using VoiceFlow that:
- **Integrates with the ServiceNow API:** Fetch real-time data from a third-party service using API integration.
- **Utilizes Custom Code Blocks:** Use JavaScript within VoiceFlow for complex operations, data manipulation, and extending capabilities beyond built-in functions.
- **Implements State Management:** Use variables and state management to maintain context across sessions, ensuring personalized user experiences.
- **Leverages Advanced NLP/NLU Capabilities:** Define custom intents and entities to handle specific user queries and support natural language commands for better conversational interaction.
- **Integrates LLMs for Unstructured Query Handling:** Use large language models (LLMs) to handle complex or unstructured queries, generating accurate and natural-sounding responses.

**Critical Requirements:**
- **API Integration and External Data Fetching:**
  - **API Blocks:** Utilize VoiceFlow’s API blocks to integrate with external APIs, fetching data dynamically to create personalized experiences.
  - **Webhooks:** Implement webhooks to trigger external services or update databases in real-time based on user interactions.
- **State Management:**
  - **Variables and State Management:** Manage user states and variables across sessions to maintain context and provide personalized experiences, such as remembering user preferences or handling multi-turn conversations.
  - **Global Variables:** Define global variables accessible across different parts of the conversation for consistent data management.
- **Advanced NLP and NLU:**
  - **Custom Intents and Entities:** Define custom intents and entities to handle domain-specific queries accurately.
  - **Natural Language Commands:** Enable natural language commands for more conversational and intuitive user interactions.
- **Integration with LLMs and AI Models:**
  - **AI Model Integration:** Integrate with large language models (LLMs) like OpenAI’s GPT to handle complex queries, generate natural responses, and manage unstructured questions.

**Data and Tools:**
- **Data:**
  - **External API Documentation:** Participants should integrate with the ServiceNow public API and review the API documentation at https://developer.servicenow.com/dev.do#!/reference%23now-platform-apis to understand endpoints and data formats. Establish a “free” developer environment as per Appendix A.
  - **Example Datasets:** Use sample datasets or JSON outputs from the chosen API for testing and validating the chatbot’s functionality.
- **Tools:**
  - **VoiceFlow Platform:** VoiceFlow is used to create the chatbot, design conversational flows, integrate APIs, and deploy across multiple platforms.
  - **OpenAI GPT (or other LLMs):** Utilize large language models (LLMs) like OpenAI GPT for NLP tasks, understanding user intents, and generating responses for unstructured and open-ended questions.
  - **ServiceNow Public API:** Use the ServiceNow API to access and manage data in real-time from ServiceNow services, integrating this functionality into the chatbot.

**Data Flow and Functionality:**
- **User Query:** Users interact with the chatbot by asking domain-relevant questions (e.g., “What services are available?” or “What are the components of a service?” or “Give me the latest status of a business service?”).
- **API Integration:** The chatbot should fetch real-time data from the external API. It must efficiently handle API calls to provide meaningful responses, cover data retrieval, format handling, and manage errors.
- **Expert System Logic:** Implement logic resembling an expert system for analyzing queries and determining responses:
  - Route queries to relevant data sources or endpoints.
  - Apply rules based on conditions or thresholds.
  - Offer recommendations or actions based on retrieved data.
- **LLM-Powered Unstructured Query Handling:** Use LLMs to manage unstructured or complex queries:
  - Employ prompt engineering to refine user queries.
  - Generate detailed explanations for complex questions.
  - Continuously learn from interactions to improve response quality.
- **Feedback Loop and Continuous Learning:** Integrate a feedback loop to refine chatbot accuracy and relevance based on user feedback, enhancing both LLM and expert system performance.

**Challenge Requirements:**
- **Chatbot Design:** Develop a comprehensive conversational flow supporting structured and unstructured queries.
- **API Integration:** Demonstrate integration with at least one external API.
- **State Management:** Implement state management to maintain context and deliver personalized experiences.
- **Advanced NLP and LLM Utilization:** Utilize NLP/NLU capabilities for understanding and responding to user queries.
- **Documentation and Presentation:** Provide comprehensive documentation on chatbot architecture, logic flow, API integration, and LLM usage.
- **Evaluation Criteria:**
  - **Integration and Functionality:** Quality and efficiency of API integration and data utilization.
  - **Custom Logic and Code:** Effective use of JavaScript for extending chatbot capabilities.
  - **State Management:** How well the chatbot manages context and user states.
  - **NLP/LLM Performance:** Effectiveness in handling structured and unstructured queries.
  - **User Experience:** Intuitiveness, error management, and conversational flow quality.
  - **Innovation and Creativity:** Unique approaches to integrating multiple technologies.
  - **Documentation and Presentation:** Clarity, comprehensiveness, and effectiveness in communication.

**Submission Guidelines:** Send your submission to:
- **Primary Contact:** Himanshi Motwani: motwani.hi@northeastern.edu
- **CC:** Prof Nik Bear Brown: ni.brown@northeastern.edu
- **Deadline:** The challenge is open until the position is filled.
- **Please include "Bear Brown & Co. | Stealth Start-Up Chatbot Development Challenge" in the email subject line. Attach all relevant files, including the VoiceFlow project export, documentation, and a presentation file (PDF or PPT).**
- **Opportunity for Winners:** Winners of this challenge will be granted interviews for a Data Scientist position at a Stealth Start-Up. This is an exciting opportunity to join an innovative team and work on cutting-edge conversational AI projects!

**Resources:**
- **VoiceFlow Platform:** VoiceFlow Website
- **API Documentation:** [Link to chosen API Documentation] (to be provided by the participant)
- **OpenAI GPT:** OpenAI Website
- **Sample Datasets:** [Link to Sample Data] (to be provided by the participant)

**For questions regarding the challenge, use the provided emails. We look forward to seeing your innovative solutions that push the boundaries of AI and enterprise decision-making!**

**Appendix A: ServiceNow Free Access**

**To obtain a ServiceNow Developer Instance, follow these steps:**
- **Visit the ServiceNow Developer Site:** Navigate to the ServiceNow Developer Portal at [ServiceNow Developer Portal](https://developer.servicenow.com).
- **Create an Account:** If you don't have a developer account, register by clicking 'Register' and filling out the required information.
- **Accept the Developer Agreement:** Log in to your account, accept the agreement by checking the box, and click 'Submit.'
- **Request a Developer Instance:** Go to the 'Manage' section, select 'Instance,' and click 'Request Instance.' Fill out the form and confirm your request by clicking 'I understand.'
- **Select Instance Version:** Choose the latest version of the ServiceNow platform.
- **Access Your Instance:** After setup, you will receive a URL and login credentials to access your personal developer instance.

**Remember, the Personal Developer Instance is a sandbox environment intended for learning and experimentation, not for business or production use. API information can be found at [ServiceNow API Reference](https://developer.servicenow.com/dev.do#!/reference%23now-platform-apis).**
