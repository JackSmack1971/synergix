---
title: "Kubernetes Components"
source_url: "https://kubernetes.io/docs/concepts/overview/components/"
host: "kubernetes.io"
depth: 2
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:53.459Z"
---
# Kubernetes Components

An overview of the key components that make up a Kubernetes cluster.

This page provides a high-level overview of the essential components that make up a Kubernetes cluster.

![Components of Kubernetes](https://kubernetes.io/images/docs/components-of-kubernetes.svg)

The components of a Kubernetes cluster

## Core Components[](https://kubernetes.io/docs/concepts/overview/components/#core-components)

A Kubernetes cluster consists of a control plane and one or more worker nodes. Here's a brief overview of the main components:

### Control Plane Components[](https://kubernetes.io/docs/concepts/overview/components/#control-plane-components)

Manage the overall state of the cluster:

[kube-apiserver](https://kubernetes.io/docs/concepts/architecture/#kube-apiserver)

The core component server that exposes the Kubernetes HTTP API.

[etcd](https://kubernetes.io/docs/concepts/architecture/#etcd)

Consistent and highly-available key value store for all API server data.

[kube-scheduler](https://kubernetes.io/docs/concepts/architecture/#kube-scheduler)

Looks for Pods not yet bound to a node, and assigns each Pod to a suitable node.

[kube-controller-manager](https://kubernetes.io/docs/concepts/architecture/#kube-controller-manager)

Runs [controllers](https://kubernetes.io/docs/concepts/architecture/controller/ "A control loop that watches the shared state of the cluster through the apiserver and makes changes attempting to move the current state towards the desired state.") to implement Kubernetes API behavior.

[cloud-controller-manager](https://kubernetes.io/docs/concepts/architecture/#cloud-controller-manager) (optional)

Integrates with underlying cloud provider(s).

### Node Components[](https://kubernetes.io/docs/concepts/overview/components/#node-components)

Run on every node, maintaining running pods and providing the Kubernetes runtime environment:

[kubelet](https://kubernetes.io/docs/concepts/architecture/#kubelet)

Ensures that Pods are running, including their containers.

[kube-proxy](https://kubernetes.io/docs/concepts/architecture/#kube-proxy) (optional)

Maintains network rules on nodes to implement [Services](https://kubernetes.io/docs/concepts/services-networking/service/ "A way to expose an application running on a set of Pods as a network service.").

[Container runtime](https://kubernetes.io/docs/concepts/architecture/#container-runtime)

Software responsible for running containers. Read [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) to learn more.

🛇 This item links to a third party project or product that is not part of Kubernetes itself. [More information](https://kubernetes.io/docs/concepts/overview/components/#third-party-content-disclaimer)

Your cluster may require additional software on each node; for example, you might also run [systemd](https://systemd.io/) on a Linux node to supervise local components.

## Addons[](https://kubernetes.io/docs/concepts/overview/components/#addons)

Addons extend the functionality of Kubernetes. A few important examples include:

[DNS](https://kubernetes.io/docs/concepts/architecture/#dns)

For cluster-wide DNS resolution.

[Web UI](https://kubernetes.io/docs/concepts/architecture/#web-ui-dashboard) (Dashboard)

For cluster management via a web interface.

[Container Resource Monitoring](https://kubernetes.io/docs/concepts/architecture/#container-resource-monitoring)

For collecting and storing container metrics.

[Cluster-level Logging](https://kubernetes.io/docs/concepts/architecture/#cluster-level-logging)

For saving container logs to a central log store.

## Flexibility in Architecture[](https://kubernetes.io/docs/concepts/overview/components/#flexibility-in-architecture)

Kubernetes allows for flexibility in how these components are deployed and managed. The architecture can be adapted to various needs, from small development environments to large-scale production deployments.

For more detailed information about each component and various ways to configure your cluster architecture, see the [Cluster Architecture](https://kubernetes.io/docs/concepts/architecture/) page.

## Feedback

Was this page helpful?

Yes No

Thanks for the feedback. If you have a specific, answerable question about how to use Kubernetes, ask it on [Stack Overflow](https://stackoverflow.com/questions/tagged/kubernetes). Open an issue in the [GitHub Repository](https://www.github.com/kubernetes/website/) if you want to [report a problem](https://github.com/kubernetes/website/issues/new?title=Issue%20with%20k8s.io) or [suggest an improvement](https://github.com/kubernetes/website/issues/new?title=Improvement%20for%20k8s.io).

Last modified May 30, 2026 at 6:09 PM PST: [Add theme\_lock front matter to concepts overview pages (6e5065edcf)](https://github.com/kubernetes/website/commit/6e5065edcfd577d59c7c9ee18b238ecbc91675fe)

Items on this page refer to third party products or projects that provide functionality required by Kubernetes. The Kubernetes project authors aren't responsible for those third-party products or projects. See the [CNCF website guidelines](https://github.com/cncf/foundation/blob/main/policies-guidance/website-guidelines.md) for more details.

You should read the [content guide](https://kubernetes.io/docs/contribute/style/content-guide/#third-party-content) before proposing a change that adds an extra third-party link.
