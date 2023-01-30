from promptpay import qrcode

# generate a payload
id_or_phone_number = "0988253419"
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 30)

# export to PIL image
img = qrcode.to_image(payload)

# export to file
qrcode.to_file(payload_with_amount, "/Users/Onlyjune/Desktop/Yor/image/delicatemode.png")
# qrcode.to_file(payload_with_amount, "CPS/Term1_Final_project/qrcodepic/qrcode-try.png")
