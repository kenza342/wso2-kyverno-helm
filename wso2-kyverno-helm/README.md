# WSO2 API Manager Helm Deployment & Kyverno Policies

## WSO2 API Manager

Déploiement de WSO2 API Manager 4.7.0 avec Helm sur Kubernetes.

### Components
- WSO2 API Manager Helm Chart
- Kubernetes Gateway API / Envoy Gateway
- TLS configuration
- Custom Helm values

## Kyverno Policy Engine

Installation de Kyverno 3.8.2 (APP v1.18.2).

### Security policies
- Validation des Secrets Kubernetes
- Blocage des credentials admin en clair
- Policy as Code avec Kyverno

## Environment

- Kubernetes
- Minikube
- Helm
- Kyverno
