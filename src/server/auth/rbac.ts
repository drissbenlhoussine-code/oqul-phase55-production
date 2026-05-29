export const ROLES = {
  USER: "user",
  ADMIN: "admin",
  PARENT: "parent",
} as const;

export function hasRole(
  currentRole: string,
  requiredRoles: string[]
) {
  return requiredRoles.includes(currentRole);
}
