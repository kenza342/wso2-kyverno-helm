# Kyverno

Kyverno is installed using Helm OCI chart.

Installation:

```bash
helm install kyverno oci://ghcr.io/kyverno/charts/kyverno \
--version 3.8.2 \
-n kyverno \
--create-namespace
