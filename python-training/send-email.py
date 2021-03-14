# 寄送Email 的程式
# 準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="paece860226a@gmai.com"
msg["To"]="peace860226a@gmail.com"
msg["Subject"]="你好，其龍"
#寄送純文字
#msg.set_content("測試看看")
#寄送多樣式的內容(html)
msg.add_alternative("<h3>優惠券</h3>滿五百送一百", subtype="html")
# 連線到 SMTP Server 驗證寄件人身分發送郵件
import smtplib
# 網路上搜尋 gmail smtp server 或是 yahoo server
server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("peace860226a@gmail.com", "Easy123123")
server.send_message(msg)
server.close()