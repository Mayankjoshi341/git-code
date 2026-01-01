def Email_sender(receiver_gmail, sym_1, sym_2, sym_3,
                 disease, description, precaution_1, precaution_2, precaution_3, precaution_4, home_remedy):
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    sender_gmail = "mediscan.report25@gmail.com"
    password = "ydwu jrlk ufcf dqcw"

    msg = MIMEMultipart("alternative")
    msg["From"] = sender_gmail
    msg["To"] = receiver_gmail
    msg["Subject"] = "🩺 MediScan – Your Health Insights Based on Symptoms"

    body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; color:#333;">
        <div style="max-width:600px; margin:auto; padding:20px; border:1px solid #ddd; border-radius:10px;">
          <div style="text-align:center;">
            <img src="https://yourdomain.com/mediscan-logo.png" alt="MediScan" width="150" style="margin-bottom:20px;"/>
            <h2 style="color:#2E86C1;">Welcome to MediScan</h2>
          </div>
          <p>Hi there 👋,</p>
          <p>Based on the <b>symptoms you provided</b>, MediScan has analyzed possible conditions 
             that might be affecting your health. Our AI-powered system ensures you get 
             <b>personalized and reliable health insights</b>.</p>

          <h3 style="color:#117A65;">Your Submitted Symptoms:</h3>
          <ul>
            <li>{sym_1}</li>
            <li>{sym_2 or "-"}</li>
            <li>{sym_3 or "-"}</li>
          </ul>

          <h3 style="color:#CB4335;">Possible Health Condition:</h3>
          <p><b>{disease}</b></p>

          <h3 style="color:#6C3483;">Condition Overview:</h3>
          <p>{description}</p>

          <h3 style="color:#AF601A;">Recommended Precautions:</h3>
          <ul>
            <li>{precaution_1}</li>
            <li>{precaution_2}</li>
            <li>{precaution_3}</li>
            <li>{precaution_4}</li>
          </ul>

          <h3 style="color:#1F618D;">Suggested Home Remedy:</h3>
          <p>{home_remedy}</p>

          <p>📷 You can also <b>upload photos</b> of visible symptoms (e.g., skin rashes, throat) directly in the app for a more accurate analysis.</p>
          <p>🔗 Learn more on our website: 
            <a href="https://yourdomain.com/learn-more" style="color:#2E86C1;">MediScan Health Portal</a>
          </p>
          <div style="margin-top:30px; text-align:center;">
            <a href="https://yourdomain.com/app-download" 
               style="background-color:#2E86C1; color:white; padding:12px 20px; 
                      border-radius:5px; text-decoration:none; font-weight:bold;">
              Download MediScan App
            </a>
          </div>
          <p style="margin-top:30px; font-size:12px; color:#888; text-align:center;">
            ⚠️ Note: MediScan provides health suggestions based on AI analysis. 
            Always consult a doctor for a professional diagnosis.
          </p>
        </div>
      </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

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
