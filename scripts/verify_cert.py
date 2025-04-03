import hashlib
import gnupg
import json

def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        h.update(f.read())
    return f"SHA256:{h.hexdigest()}"

def verify_signature(cert_folder):
    with open(f"{cert_folder}/{cert_folder}.json") as f:
        data = json.load(f)

    gpg = gnupg.GPG()
    gpg.import_keys(open(f"{cert_folder}/{data['public_key_file']}").read())
    verified = gpg.verify_file(
        open(f"{cert_folder}/{data['signature_file']}", 'rb'),
        f"{cert_folder}/{data['pdf_file']}"
    )
    if verified:
        print("✅ Signature verified")
    else:
        print("❌ Signature invalid")

    for file, expected_hash in data['hashes'].items():
        actual = sha256sum(f"{cert_folder}/{file}")
        if actual != expected_hash:
            print(f"❌ Hash mismatch for {file}")
        else:
            print(f"✅ Hash OK: {file}")
