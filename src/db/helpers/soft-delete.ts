import { timestamp } from "drizzle-orm/pg-core";

export const softDeleteColumn = {
  deletedAt: timestamp("deleted_at"),
};
