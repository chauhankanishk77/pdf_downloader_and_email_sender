from urllib.parse import urlparse, parse_qs
from flask import Flask, render_template, request, Response, jsonify
import requests
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.message import EmailMessage
import os

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/send-pdf', methods=['POST'])
# def send_pdf():
#     google_link = request.form.get('googleLink')
#     user_email = request.form.get('userEmail')

#     # Extract PDF link from the Google search link
#     pdf_link = extract_pdf_link(google_link)
#     print(google_link)
#     # Download the PDF
#     #pdf_data = requests.get(pdf_link).content

#     # Send email with PDF attachment
#     #send_email(user_email, pdf_data)

#     return jsonify({'message': 'Email sent successfully'})

# @app.route('/download-pdf', methods=['POST'])
# def download_pdf():
#     google_link = request.form.get('googleLink')

#     # Extract PDF link from the Google search link
#     pdf_link = extract_pdf_link(google_link)

#     # Download the PDF
#     pdf_data = requests.get(pdf_link).content

#     # Create a Flask response with the PDF content
#     response = Response(pdf_data, content_type='application/pdf')
#     response.headers['Content-Disposition'] = 'attachment; filename=downloaded_file.pdf'

#     return response

# def extract_pdf_link(google_link):
#     # Implement logic to extract PDF link from the Google search link
#     # This might involve scraping the Google search results or using an API
#     # Return the extracted PDF link
#     # Example: Assume the PDF link is directly in the Google search link (not realistic)
#     try:
#         # Parse the Google link
#         parsed_url = urlparse(google_link)

#         # Extract the 'url' parameter from the query string
#         url_param = parse_qs(parsed_url.query).get('url', None)

#         if url_param:
#             return url_param[0]
#         else:
#             return None
#     except Exception as e:
#         print(f"Error extracting URL: {e}")
#         return None

# def send_email(user_email, pdf_data):
#     # Setup email configuration
#     port = 465  # For SSL
#     smtp_server = "smtp.gmail.com"
#     sender_email = "testing.for.dev99@gmail.com"  # Enter your address
#     password = "ewdngdttpbaglcje"

#     # Create message
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = user_email
#     message['Subject'] = 'PDF Attachment'

#     # Attach PDF
#     pdf_attachment = MIMEApplication(pdf_data, 'pdf')
#     pdf_attachment.add_header('Content-Disposition', 'attachment', filename='file.pdf')
#     message.attach(pdf_attachment)

#     context = ssl.create_default_context()
#     with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#         server.login(sender_email, password)
#         server.sendmail(sender_email, user_email, message.as_string())

# if __name__ == '__main__':
#     app.run(debug=True)


@app.route('/')
def index():
    return render_template('index.html')

def send_pdf():
    google_link = request.form.get('googleLink')
    user_email = request.form.get('userEmail')

    # Extract PDF link from the Google search link
    pdf_link = extract_pdf_link(google_link)
    # Download the PDF
    pdf_data = requests.get(pdf_link).content

    # Send email with PDF attachment
    send_email(user_email, pdf_data)

    return jsonify({'message': 'Email sent successfully'})

def download_pdf():
    google_link = request.form.get('googleLink')

    # Extract PDF link from the Google search link
    pdf_link = extract_pdf_link(google_link)

    # Download the PDF
    pdf_data = requests.get(pdf_link).content

    # Create a Flask response with the PDF content
    response = Response(pdf_data, content_type='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename=downloaded_file.pdf'

    return response

def extract_pdf_link(google_link):
    # Implement logic to extract PDF link from the Google search link
    # This might involve scraping the Google search results or using an API
    # Return the extracted PDF link
    # Example: Assume the PDF link is directly in the Google search link (not realistic)
    try:
        # Parse the Google link
        parsed_url = urlparse(google_link)

        # Extract the 'url' parameter from the query string
        url_param = parse_qs(parsed_url.query).get('url', None)

        if url_param:
            return url_param[0]
        else:
            return None
    except Exception as e:
        print(f"Error extracting URL: {e}")
        return None

def send_email(user_email, pdf_data):
    # Setup email configuration
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "testing.for.dev99@gmail.com"  # Enter your address
    password = "ewdngdttpbaglcje"

    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = user_email
    message['Subject'] = 'PDF File'

    # Attach PDF
    pdf_attachment = MIMEApplication(pdf_data, 'pdf')
    pdf_attachment.add_header('Content-Disposition', 'attachment', filename='file.pdf')
    message.attach(pdf_attachment)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, user_email, message.as_string())

@app.route('/process-pdf', methods=['POST'])
def process_pdf():
    google_link = request.form['googleLink']
    pdf_option = request.form['pdfOption']

    # Implement your logic to generate the PDF from the Google link

    # Placeholder logic to simulate PDF generation
    #pdf_content = f"PDF content generated from {google_link}"

    if pdf_option == 'download':
        return download_pdf()

    elif pdf_option == 'sendEmail':
        send_pdf()
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=False)
