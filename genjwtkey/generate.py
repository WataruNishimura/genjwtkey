from pathlib import Path
from jwcrypto import jwk
import os
import json


#key = jwk.JWK.generate(kty="RSA", alg="RS256", use="sig", size=2048)

#private_key = key.export_private()
#public_key = key.export_public()

#print("=== private key ===\n" + json.dumps(json.loads(private_key), indent=2))
#print("=== public key ===\n" + json.dumps(json.loads(public_key), indent=2))

def generate():
  path = Path(os.getcwd())
  key = jwk.JWK.generate(kty="RSA", alg="RS256", use="sig", size=2048)
  private_key = key.export_private()
  public_key = key.export_public()
  with open(path / "private_key.json", mode="wt", encoding="utf-8") as private_key_file:
      private_key_file.write(json.dumps(json.loads(private_key),indent=2))
  with open(path / "public_key.json", mode="wt", encoding="utf-8") as public_key_file:
      public_key_file.write(json.dumps(json.loads(public_key),indent=2))
