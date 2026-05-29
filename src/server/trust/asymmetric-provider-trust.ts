import {
  createPrivateKey,
  createPublicKey,
  generateKeyPairSync,
  sign,
  verify,
} from "node:crypto";

export function generateEd25519ProviderKeyPair() {
  const pair = generateKeyPairSync("ed25519");

  return {
    publicKey: pair.publicKey.export({ format: "pem", type: "spki" }).toString(),
    privateKey: pair.privateKey.export({ format: "pem", type: "pkcs8" }).toString(),
  };
}

export function signProviderReceiptAsymmetric(input: {
  privateKeyPem: string;
  deliveryId: string;
  providerMessageId: string;
}) {
  const privateKey = createPrivateKey(input.privateKeyPem);
  const payload = Buffer.from(
    [input.deliveryId, input.providerMessageId].join(":"),
    "utf-8"
  );

  return sign(null, payload, privateKey).toString("base64");
}

export function verifyProviderReceiptAsymmetric(input: {
  publicKeyPem: string;
  deliveryId: string;
  providerMessageId: string;
  signature: string;
}) {
  const publicKey = createPublicKey(input.publicKeyPem);
  const payload = Buffer.from(
    [input.deliveryId, input.providerMessageId].join(":"),
    "utf-8"
  );

  return verify(null, payload, publicKey, Buffer.from(input.signature, "base64"));
}
