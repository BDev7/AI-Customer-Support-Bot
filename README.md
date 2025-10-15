# AI Customer Support Bot

## Overview
An intelligent AI-powered chatbot designed to simulate realistic customer support interactions using an FAQ dataset. It delivers instant, relevant answers and dynamically suggests FAQs as users type. Built with a Flask backend and React frontend, this project supports real-time communication via Socket.IO without external API dependencies.

## Features
- Keyword-based FAQ matching for instant responses
- Real-time chat with Socket.IO integration
- Dynamic question suggestions to enhance user experience
- Clean, responsive React UI featuring chat bubbles and autocomplete dropdown
- Modular architecture enabling future advanced AI (LLM) integration
- Local processing ensures fast responses and easy deployment

## Architecture
- **Backend:** Flask + Socket.IO handling API endpoints and real-time chat  
- **Frontend:** React SPA communicating with backend for chat and suggestions  
- **Data:** Local JSON file storing customer FAQs  
- **Logic:** Simple but effective token overlap similarity for query matching

## Demo Video Link: https://drive.google.com/file/d/1q6hSrfcGbB78fjRSRBFuE08ldZvoDa4q/view?usp=sharing

## Getting Started

### Prerequisites
- Python 3.8+  
- Node.js & npm  
- Git (optional)

### Backend Setup
1. Navigate to the `backend` directory  
2. Create and activate a Python virtual environment  
3. Install dependencies:
4. Ensure `customer_support_faqs.json` is in the backend folder  
5. Run the server:

The backend runs on port 5001.

### Frontend Setup
1. Navigate to the `frontend` directory  
2. Install dependencies:
3. Start the React app:

The frontend runs on `http://localhost:3000`.

## Usage
- Access the React app in your browser  
- Start chatting with the AI, see live question suggestions  
- Receive instant replies matched from local FAQs  

## Future Enhancements
- Integration with advanced LLM APIs like Google Gemini for more contextual conversations  
- Persistent session management and conversation history  
- Multimedia response support and smart escalation mechanisms  
- Cloud deployment using Docker or serverless architectures  

## Deliverables
- Source code on GitHub (backend, frontend, and data)  
- README file with setup and usage details  
- Demo video showcasing features and interactions  

## Contact
For questions or support, contact:  
**Brahm Dev**  
**Email:** your.email@example.com  
**GitHub:** (https://github.com/BDev7)

---

**Thank you for exploring the AI Customer Support Bot!**

