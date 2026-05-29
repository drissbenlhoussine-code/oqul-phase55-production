export type OrderedEvent = {
  id: string;
  aggregate_id: string;
  sequence: number;
};

export function assertAggregateOrdering(events: OrderedEvent[]) {
  const byAggregate = new Map<string, OrderedEvent[]>();

  for (const event of events) {
    const list = byAggregate.get(event.aggregate_id) ?? [];
    list.push(event);
    byAggregate.set(event.aggregate_id, list);
  }

  for (const [aggregateId, aggregateEvents] of byAggregate.entries()) {
    const sorted = [...aggregateEvents].sort((a, b) => a.sequence - b.sequence);

    for (let index = 0; index < aggregateEvents.length; index++) {
      if (aggregateEvents[index].id !== sorted[index].id) {
        throw new Error(`Ordering invariant violated for aggregate ${aggregateId}`);
      }
    }
  }

  return true;
}
