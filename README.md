# Gmail Automation with Gemini AI

## Description

This Python project integrates Google Gemini 2.5 AI model with Gmail to automate drafting and sending emails. The system uses:

- **Gemini AI (via LangChain)** to generate professional email content.
- **Gmail API** for creating drafts and sending messages securely.
- **OAuth2 authentication** for secure access to your Gmail account.

## Features

- Draft emails automatically based on a simple prompt.
- Create Gmail drafts and optionally send them.
- Supports multiple recipients.
- Persistent token storage (`token.pkl`) to avoid repeated authentication.

## Requirements

- Python 3.11+
- Google Cloud credentials for Gmail API access
- Internet connection for API requests

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Gulsherkha/gmail-automation.git
   cd gmail-automation
