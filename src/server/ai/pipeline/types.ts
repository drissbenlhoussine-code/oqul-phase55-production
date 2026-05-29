import type { AgentId, PipelineFlowId } from "./config";

export type PipelineEvent =
  | { event: "start"; runId: string; flow: PipelineFlowId; agents: AgentId[] }
  | { event: "agent_start"; agentId: AgentId; ts: number }
  | { event: "agent_delta"; agentId: AgentId; delta: string }
  | { event: "agent_done"; agentId: AgentId; output: string; durationMs: number }
  | { event: "end"; status: "done"; totalMs: number; finalOutput: string }
  | { event: "error"; message: string };
