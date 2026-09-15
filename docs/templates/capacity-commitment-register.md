# Capacity commitment register template

Use this Capacity Operations (CapOps) register to connect financial obligations, technical entitlements, assignments, and actual consumption without treating them as the same thing. Copy the index and detail tables, use stable references, and update them at acquisition, assignment, use, review, and release. Keep confidential terms in an approved system.

## Commitment index

| Commitment identifier | Type and mechanism reference | Business purpose and demand version | Technical owner | Commercial and budget owner | Lifecycle state | Term and next decision deadline | Linked risk or decision |
|---|---|---|---|---|---|---|---|
| Enter identifier | Financial only, capacity entitlement, or combined; validate terms | Consumer need and scenario | Named owner | Named authorities | Proposed, acquired, assigned, consuming, under review, releasing, or closed | Start, end, renewal or cancellation deadline | Record references |

## Scope, conditions, and acquisition

| Field | Entry |
|---|---|
| Commitment identifier and version | Link to index and history |
| Service and resource family | Exact eligible shape and restrictions |
| Quantity and unit | Financial obligation and technical entitlement separately |
| Location and administrative scope | Region, zone, account or other eligible boundary as applicable |
| Required and actual start, ramp, and duration | Demand window versus mechanism term |
| Documented assurance or benefit | Exact applicable conditions; do not infer a capacity right from a discount |
| Evidence references and review dates | Current public mechanism documentation, approved terms, and collection dates |
| Prerequisites and exclusions | Limits, eligibility, configuration, failure scenarios, and outstanding gaps |
| Transfer, sharing, and amendment rules | Allowed changes established by terms, or explicitly not established |
| Release, cancellation, and renewal rules | Deadlines, remaining charges, restrictions, and automatic renewal if applicable |
| Business, technical, and commercial approvals | Separate authorities, decisions, and dates |
| Acquisition outcome | Mechanism creation and configuration result; unresolved conditions |
| Last responsible acquisition decision deadline | Required date minus justified acquisition and validation lead time |

## Assignment ledger

Repeat rows for consumers and time windows. Do not allocate the same non-shareable capacity twice.

| Assignment identifier | Commitment identifier | Consumer and cost owner | Quantity and unit | Eligible scope and period | Priority and allowed use | Peak or recovery protection | Approval and change history |
|---|---|---|---|---|---|---|---|
| Enter assignment | Linked commitment | Named workload and accountable owner | Assigned quantity | Matching family, location, and dates | Local priority and sharing rules | Purpose, scenario, and release authority | Decision reference and date |

## Consumption and reconciliation

| Commitment and period | Entitlement quantity | Assigned quantity | Observed consumption | Charges or remaining obligation | Eligibility or deployment result | Difference and explanation | Evidence date and owner |
|---|---|---|---|---|---|---|---|
| Enter scope and window | Unit and conditions | Compatible units only | Unit and source | Approved reference; distinguish technical release from financial effect | Confirmed, failed, unknown, or not applicable | Idle, unassigned, mismatched, protected, or other cause | Source, observed date, next refresh |

## Review and release

| Review date and trigger | Forecast and recovery check | Recommendation | Authority and decision deadline | Action and executor | Technical verification | Commercial verification | Residual obligation and next review |
|---|---|---|---|---|---|---|---|
| Scheduled, changed demand, idle use, or expiry | Consumer acknowledgments and shared-dependency checks | Retain, assign, reassign, amend, renew, or release | Named authority and latest action date | Specific action and due date | Allocation and resource state evidence | Contract, billing, and continuing-charge evidence | Owner and end or next review date |

Close a record only after technical assignments and remaining commercial obligations are reconciled. If release is not permitted, keep the obligation visible. “Secured” must cite a matching mechanism and its conditions; quota, forecasts, or financial benefits alone do not establish deployable capacity.

## Related content

- [Manage capacity commitments](../implementation/manage-capacity-commitments.md)
- [Integrate CapOps and FinOps](../implementation/integrate-capops-and-finops.md)
- [Decision record](decision-record.md)
