from datetime import datetime
import pdfkit
import os
from email.mime.application import MIMEApplication

def generate_html_report(student_name, recommendation):
    strengths_html = "".join(
        f"<li>✅ {k.replace('_', ' ').title()}</li>"
        for k in recommendation["strengths"]
    )

    focus_html = "".join(
        f"<li>🎯 {k.replace('_', ' ').title()}</li>"
        for k in recommendation["focus_areas"]
    )

    trajectory_html = "".join(
        f"<li>📈 {step}</li>"
        for step in recommendation["growth_trajectory"]
    )

    impact_html = "".join(
        f"<li><b>{k.replace('_', ' ').title()}</b>: {v}</li>"
        for k, v in recommendation["estimated_impact"].items()
    )

    html = f"""
    <html>
    <head>
        <title>Placement Readiness Report</title>
        <style>
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 30px;
            }}
            .container {{
                background: #ffffff;
                max-width: 800px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                text-align: center;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #ecf0f1;
                padding-bottom: 5px;
            }}
            .badge {{
                display: inline-block;
                padding: 8px 15px;
                border-radius: 20px;
                background-color: #3498db;
                color: white;
                font-weight: bold;
            }}
            .box {{
                background: #f9fafb;
                padding: 20px;
                margin-top: 20px;
                border-radius: 10px;
            }}
            ul {{
                padding-left: 20px;
            }}
            footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #7f8c8d;
                text-align: center;
            }}
        </style>
    </head>
    <body>

        <div class="container">
            <h1>🎓 Placement Readiness Report</h1>

            <p><b>Student:</b> {student_name}</p>
            <p><b>Date:</b> {datetime.now().strftime('%d %b %Y')}</p>

            <div class="box">
                <h2>📊 Readiness Level</h2>
                <span class="badge">{recommendation['readiness_level']}</span>
            </div>

            <div class="box">
                <h2>💰 Expected Salary Range</h2>
                <p><b>₹ {recommendation['expected_salary_lpa']} LPA</b></p>
            </div>

            <div class="box">
                <h2>💪 Your Strengths</h2>
                <ul>{strengths_html}</ul>
            </div>

            <div class="box">
                <h2>🎯 Focus Areas (Next 8–12 Weeks)</h2>
                <ul>{focus_html}</ul>
            </div>

            <div class="box">
                <h2>🚀 Estimated Impact</h2>
                <ul>{impact_html}</ul>
            </div>

            <div class="box">
                <h2>📈 Career Growth Trajectory</h2>
                <ul>{trajectory_html}</ul>
            </div>

            <footer>
                This report provides guidance based on peer comparison and does not guarantee placement or salary.
            </footer>
        </div>

    </body>
    </html>
    """

    return html

def pdf_convert(html_content):
    options = {
        'page-size': 'A4',
        'encoding': 'UTF-8',
        'no-outline': None
    }
    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    pdf_bytes = pdfkit.from_string(html_content, options=options , configuration=config)
    return pdf_bytes

def mail_generate(receiver_gmail, student_name, recommendation):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sender_gmail = os.getenv("SENDER_GMAIL")
    password = os.getenv("GMAIL_APP_PASSWORD")

    msg = MIMEMultipart("alternative")
    msg["From"] = sender_gmail
    msg["To"] = receiver_gmail
    msg["Subject"] = "📊 Placement Readiness Report for " + student_name
    body = generate_html_report(student_name, recommendation)
    msg.attach(MIMEText(body, "html"))
    
    pdf_report = pdf_convert(body)

    if pdf_report is not None:
        attachment = MIMEApplication(pdf_report, _subtype="pdf")
        attachment.add_header(
            "Content-Disposition",
            "attachment",
            filename="Placement_Readiness_Report.pdf"
        )
        msg.attach(attachment)
    server = None
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_gmail, password)
        server.sendmail(sender_gmail, receiver_gmail, msg.as_string())
        print(f"Email sent successfully to {receiver_gmail}")
    except Exception as e:
        print("Error:", e)
    finally:
        if server:
            server.quit()
