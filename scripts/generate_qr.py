import qrcode

def generate_qr(cert_id, short_url):
    qr = qrcode.make(short_url)
    qr.save(f"{cert_id}/qrcode.png")
