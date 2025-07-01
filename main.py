import qrcode

upi_id=input("Enter UPI Id=  ")

qr_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
# paytm_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
# google_pay_url=f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

qr_code_qr=qrcode.make(qr_url)
# paytm_qr=qrcode.make(paytm_url)
# google_pay_qr=qrcode.make(google_pay_url)

qr_code_qr.save('qr_code_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')

qr_code_qr.show()
# paytm_qr.show()
# google_pay_qr.show()