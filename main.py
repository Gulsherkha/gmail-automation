import os
import pickle
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Gemini Chat Model ---
from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

# --- Gmail Toolkit ---
from langchain_google_community import GmailToolkit
from langchain_google_community.gmail.utils import build_gmail_service  # ✅ updated

# Google Auth
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://mail.google.com/"]

def get_credentials():
    creds = None
    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pkl", "wb") as token:
            pickle.dump(creds, token)
    return creds

# Build Gmail service
credentials = get_credentials()
api_resource = build_gmail_service(credentials=credentials)  # ✅ updated
toolkit = GmailToolkit(api_resource=api_resource)

# Get tools
tools = toolkit.get_tools()
draft_tool = [t for t in tools if t.name == "create_gmail_draft"][0]
send_tool = [t for t in tools if t.name == "send_gmail_message"][0]

print("✅ Available Gmail tools:")
for t in tools:
    print("-", t.name)

# --- Draft email with Gemini ---
prompt = """
Write a professional but short email to boss@example.com.
Subject: Assignment Submission
Content: Inform that I’ll submit my assignment by tonight.
Return only the email body (no greetings needed).
"""
draft = llm.invoke(prompt)
email_body = draft.content

print("\n✅ Drafted email body:")
print(email_body)

# --- Create draft in Gmail ---
draft_result = draft_tool.run({
    "to": ["boss@example.com"],
    "subject": "Assignment Submission",
    "message": email_body   # ✅ fixed key
})

print("\n📄 Draft created successfully!")
print("Draft Result:", draft_result)  # ✅ print raw result safely

# --- Ask user if they want to send ---
choice = input("\nDo you want to send this email now? (y/n): ").strip().lower()

if choice == "y":
    send_result = send_tool.run({
        "to": ["boss@example.com"],
        "subject": "Assignment Submission",
        "message": email_body   # ✅ fixed key
    })
    print("\n📨 Email sent successfully!")
    print("Send Result:", send_result)  # ✅ print raw result safely
else:
    print("\n🚫 Email not sent. You can review it in Gmail drafts.")
