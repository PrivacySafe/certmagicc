import subprocess
import json
import hashlib

def ipfs_add(file_path):
    result = subprocess.run(["ipfs", "add", "-Q", file_path], capture_output=True, text=True)
    return result.stdout.strip()

def sha256sum(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as f:
        h.update(f.read())
    return f"SHA256:{h.hexdigest()}"

def generate_metadata(cert_id):
    metadata = {
        "cert_id": cert_id,
        "issued_at": "2025-03-26T00:00:00Z",
        "pdf_file": f"{cert_id}.pdf",
        "signature_file": f"{cert_id}.sig",
        "public_key_file": "publickey.asc",
        "hashes": {
            f"{cert_id}.pdf": sha256sum(f"{cert_id}.pdf"),
            f"{cert_id}.sig": sha256sum(f"{cert_id}.sig"),
            "publickey.asc": sha256sum("publickey.asc")
        }
    }

    metadata["ipfs_hash"] = ipfs_add(cert_id)
    with open(f"{cert_id}/{cert_id}.json", "w") as f:
        json.dump(metadata, f, indent=2)
