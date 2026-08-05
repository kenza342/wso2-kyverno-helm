# Kyverno Tests

## Negative tests

The files inside `bad/` contain Kubernetes resources that should be rejected by Kyverno policies.

Examples:

- bad-privileged.yaml → blocked by disallow-privileged-containers
- bad-root.yaml → blocked by require-run-as-non-root
- bad-latest.yaml → blocked by disallow-latest-tag
- bad-registry.yaml → blocked by allowed-image-registries


## Positive tests

The files inside `good/` contain compliant resources accepted by Kyverno.

Examples:

- good-probe.yaml
- good-resources.yaml
- good-label.yaml
