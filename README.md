# 🌟 CertMagi.cc: Blockchain Magic For Your Business

**Website:** [certmagi.cc](https://certmagi.cc)  
**ENS Domain:** `certmagic.eth`  
**Author:** Sean O'Brien, Ivy Cyber Education LLC  
**License:** AGPLv3

We deliver **Magic Certificates** – documents and web pages stored on verified blockchain infrastructure. CertMagi.cc harnesses the power of IPFS, ENS, and the Tor Dark Web to ensure resistance to censorship, while still being **easy to update or remove** – something most blockchain solutions can't do.

---

## 🔐 Core Features

- ✅ Signed PDFs with embedded GPG verification ([Public Key](https://keys.openpgp.org/vks/v1/by-fingerprint/2E12848899B2F463409B95A82C83959AD748331E))
- ✅ Uploaded to IPFS
- ✅ Linked through IPNS and ENS (`certmagic.eth`)
- ✅ Auto-generated Tor `.onion` mirrors for redundancy and privacy
- ✅ GS1-compatible QR codes
- ✅ Short URL redirector (`certmagi.cc/sGsg1` → ENS/IPNS)
- ✅ Fully verifiable via CLI
- ✅ Dockerized deployment for reproducible use

---

## 📆 Directory Structure

```
certmagi/
├── certs/
│   └── cert123/
│       ├── cert123.pdf
│       ├── cert123.sig
│       ├── cert123.json
│       ├── publickey.asc
│       ├── qrcode.png
│       └── onion.txt
├── scripts/
│   ├── sign_pdf.py
│   ├── upload_to_ipfs.py
│   ├── verify_cert.py
│   ├── generate_qr.py
│   ├── setup_onion_service.sh
│   ├── update_ipns.py
│   └── create_github_repo.sh
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Dependencies
- Python 3.8+
- GPG (with key: `2E12848899B2F463409B95A82C83959AD748331E`)
- IPFS daemon
- Tor
- Docker (optional)
- ENS configured for `certmagic.eth`
- [GitHub CLI](https://cli.github.com/) (`gh`)
- (Optional) Ethereum wallet + Infura for ENS automation

---

## 🚀 Quickstart

```bash
git clone https://github.com/ivycyber/certmagicc.git
cd certmagicc

# Sign the PDF
python3 scripts/sign_pdf.py certs/cert123/cert123.pdf

# Upload to IPFS and generate metadata
python3 scripts/upload_to_ipfs.py cert123

# Generate QR code
python3 scripts/generate_qr.py cert123

# Auto-generate .onion mirror
sudo bash scripts/setup_onion_service.sh cert123

# Publish or update IPNS record
python3 scripts/update_ipns.py certs/cert123/cert123.json

# Create GitHub repo (optional)
bash scripts/create_github_repo.sh certmagicc

# Verify
python3 scripts/verify_cert.py cert123
```

---

## 🌐 IPNS + ENS Updater Script

**File:** `scripts/update_ipns.py`

```python
import subprocess
import json
import argparse


def publish_to_ipns(ipfs_hash, key="self"):
    print(f"🛁 Publishing to IPNS using key: {key}...")
    result = subprocess.run(
        ["ipfs", "name", "publish", f"/ipfs/{ipfs_hash}", "--key", key],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print("❌ IPNS publish failed:", result.stderr)
        return None
    print("✅ IPNS published:", result.stdout)
    return result.stdout


def update_ens(domain, ipns_path, private_key):
    from web3 import Web3
    from ens import ENS

    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"))
    w3.eth.default_account = w3.eth.account.from_key(private_key).address

    ns = ENS.fromWeb3(w3)
    if not ns.name(domain):
        print("❌ ENS domain not found.")
        return

    contenthash = ns.setup_address(domain, ipns_path)
    print(f"✅ ENS contenthash updated for {domain}: {contenthash}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata", help="Path to JSON metadata file with IPFS hash")
    parser.add_argument("--key", default="self", help="IPNS key name (default is 'self')")
    parser.add_argument("--ens", help="ENS name to update (e.g. certmagic.eth)")
    parser.add_argument("--pk", help="Private key for ENS update (hex format)")
    args = parser.parse_args()

    with open(args.metadata) as f:
        metadata = json.load(f)
        ipfs_hash = metadata["ipfs_hash"]

    ipns_result = publish_to_ipns(ipfs_hash, key=args.key)

    if args.ens and args.pk:
        update_ens(args.ens, f"/ipfs/{ipfs_hash}", args.pk)
```

---

## 🧐 Philosophy

CertMagi.cc is designed for **resilience** and **verifiability**, while avoiding the rigid permanence of most blockchain-based document solutions. You can change or remove data via IPNS, yet retain full traceability and authenticity.

---

## 📍 Scripts For This Project

- `sign_pdf.py` — Signs PDFs with your GPG private key
- `upload_to_ipfs.py` — Uploads files to IPFS and generates hash-linked metadata
- `update_ipns.py` — Updates your IPNS record to point to the latest IPFS hash, and optionally updates ENS
- `create_github_repo.sh` — Creates and optionally pushes a GitHub repo with setup files
- `setup_onion_service.sh` — Auto-generates a .onion service with Tor
- `generate_qr.py` — Creates GS1-compatible QR code for each cert
- `verify_cert.py` — Verifies signature, file hash, and metadata

---

## 📜 License

```text
AGPLv3
Copyright (C) 2025 Sean O'Brien and Ivy Cyber Education LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```
