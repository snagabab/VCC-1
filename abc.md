# Cluster information - Non Production

OpenShift supports both clusters hosted in Azure cloud and On-Prem (VMware) platform.

Dedicated clusters are also set up for applications like `PIE`, `Car services`, `Maximo`, and `CIL`.

!!! tip "Visit [OCP Report](https://ocpreport-ocpreport-prod.apps.ocp-shared-v1-nonprod.volvocars.biz/ocpreport/ocr/index.html) to view complete list of clusters and other metrics"

## OpenShift Cluster general information - Clusters hosted in Azure (Vanilla OpenShift and ARO)

| Cluster Name           | Platform    | Site/Region | Environments | Compute Subnet    | Ingress IP    | Console URL                                                                 | API URL                                                | Vault Auth Backend  |
|------------------------|-------------|-------------|--------------|-------------------|---------------|---------------------------------------------------------------------------|--------------------------------------------------------|---------------------|
| `cil-azureocp-nonprod` | `Azure-ARO` | `WEU`       | `Non Prod`   | `10.55.27.64/26`  | `10.55.27.126`| [Console](https://console-openshift-console.apps.cil-azureocp-nonprod.volvocars.biz/) | `https://api.cil-azureocp-nonprod.volvocars.biz:6443` | `cil-aro-np-weu`    |

!!! note

    - `Compute Subnet` to be used for firewall requests as source subnet.
    - `Ingress IP` to be used for LB backend pool IPs for custom URLs VIP, which is the default IP for all Ingress to the cluster.
    - `API URL` is needed for accessing API cluster or for `oc` login.
    - `Vault Auth Backend` is used for onboarding namespace into `Central Vault`. For more details please refer to [Namespace Onboard](https://backstage.volvocars.biz/docs/default/component/ocp-admin-documentation/instructions/vault-namespace-onboard/)
