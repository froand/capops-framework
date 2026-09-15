# AI and GPU capacity

Use this scenario to separate artificial intelligence (AI) experimentation, training, tuning, and inference demand. A graphics processing unit (GPU) count alone is not a complete capacity specification.

## Business context

A fictional equipment-maintenance company wants to train a visual-inspection model while keeping an existing inference service responsive. The research team values shorter experiments; the product owner values stable production response time and validated model quality. The same accelerator pool cannot be promised independently to both.

Numbers and dates are illustrative workload assumptions, not accelerator benchmarks or current provider availability.

## Capacity challenge

Training needs a compatible group of accelerators at the same time, with sufficient device memory, interconnect performance, and data throughput. Inference needs sustained capacity and predictable latency. Spare accelerators with the wrong memory or connectivity may not substitute for the requested group. A managed AI service must be assessed using its own capacity model, not assumed to inherit mechanisms for self-managed compute.

## Demand dimensions

| Demand slice | Resource and timing profile |
| --- | --- |
| Exploration | Up to two accelerators during working hours; jobs can queue and stop at checkpoints |
| Training | Four hosts with four compatible GPUs each, needed concurrently for a five-day run starting 2027-04-12 |
| Tuning | Shorter runs on the validated training configuration; limit parallel trials explicitly |
| Inference | Four GPUs continuously serving production, plus separately tested replacement and scale-out demand |
| Dependencies | Model memory footprint, device type, host memory, interconnect topology, storage-read throughput, image distribution, and dataset location |
| Placement | Approved data region and acceptable failure domains; alternatives constrained by dataset-transfer time |
| Flexibility | Smaller model, fewer parallel experiments, a later training start, or a different accelerator only after quality and throughput tests |

## Important assumptions

- Training can checkpoint and resume; validate this before assigning it interruptible windows.
- A forecast or quota increase does not guarantee the requested accelerator group.
- A catalog listing does not establish simultaneous supply of the required quantity.
- A substitute must meet model quality, memory, numerical behavior, and completion-window requirements, not merely have a similar label.
- Production replacement capacity must not be counted as freely available for research.

## Relevant CapOps capabilities

- **Capacity forecasting:** separate steady inference from bursty experimentation and synchronized training.
- **Capacity allocation:** assign production floors, experiment windows, and reclaim rules.
- **Workload placement:** validate hardware and deployment-model alternatives.
- **Capacity acquisition:** investigate only mechanisms documented for the chosen service and configuration.
- **Capacity optimization:** reduce data stalls and unnecessary trials before seeking more accelerators.

## Recommended actions

1. Benchmark representative data and model versions. Measure useful completed work, memory pressure, input stalls, and inference latency.
2. Publish a time-phased plan with minimum viable and preferred training sizes. Record whether smaller groups lengthen the run beyond its useful business window.
3. Confirm dataset permissions, network path, storage throughput, software compatibility, and deployment-image readiness before the training window.
4. Protect an organization-defined inference allocation. Admit experiments against the remaining pool using a visible queue and maximum holding periods.
5. Compare supported capacity arrangements with scheduling flexibility and model changes. Keep quota status and physical-capacity evidence separate.
6. Test checkpoint restore and the production replacement path. Stop and reclaim unused research allocations, but do not release production headroom without service-owner approval.

## Potential alternatives

Reuse an already validated model, reduce tuning search space, train on a smaller dataset first, or batch non-urgent inference. A managed service can be evaluated as a separate option with its own throughput, quota, data, and commercial conditions. None is a drop-in replacement without validation.

## FinOps considerations

Evaluate cost per useful completed experiment and per accepted inference workload alongside utilization. Include dataset movement, storage, retries, idle reserved time, and engineering effort. High GPU utilization is not valuable if results fail quality checks. A discount commitment may outlast the model or hardware choice; compare that risk with shorter allocation windows.

## Residual risks

A training run may take longer than measured, a checkpoint may be incompatible with a substitute, or production demand may consume the experimental window. Accepted capacity arrangements do not eliminate model-quality, dependency, or deployment risks.

## Common mistakes

- Combining all AI demand into a single annual GPU total.
- Treating accelerator models or memory configurations as interchangeable.
- Holding expensive compute while datasets or software are not ready.
- Extending a compute reservation claim to a managed AI service without service-specific documentation.
- Maximizing utilization by consuming the inference recovery allocation.

## Example decision record

| Field | Illustrative record |
| --- | --- |
| Decision | Permit one 16-GPU training run; keep the four-GPU production allocation separate; queue further experiments |
| Accountable owner | AI product owner; research lead owns training readiness and reliability lead owns inference headroom |
| Decision deadline | 2027-04-05, before confirming the training window |
| Evidence required | Versioned benchmark, dataset-read test, checkpoint-restore result, service-specific quota and capacity evidence, inference replacement test |
| Trade-off | Fewer simultaneous experiments in exchange for a clearer production operating margin |
| Residual risk accepted | Training may be deferred or finish late; no model-release date is protected by CapOps |
| Revisit | After the first run, a model change, or inference demand exceeding the tested envelope |
| Release condition | Reclaim training allocation after artifact validation and data cleanup |

## Related content

- [Capacity allocation](../capabilities/capacity-allocation.md)
- [Capacity optimization](../capabilities/capacity-optimization.md)
- [Workload capacity profile](../templates/workload-capacity-profile.md)
- [Specialized resource dependencies](specialized-resource-dependencies.md)
