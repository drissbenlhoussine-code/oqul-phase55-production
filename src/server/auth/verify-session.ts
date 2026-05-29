/**
 * verify-session.ts — compatibility shim for Phase 26 modules.
 * Delegates to COMPANION's JWT implementation.
 */
export { verifyToken as verifySessionToken } from "./jwt";
export type { JWTPayload as SessionPayload } from "./jwt";
