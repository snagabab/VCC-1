# Cluster information - Non Production

OpenShift supports both clusters hosted in Azure cloud and On-Prem (VMware) platform.

Dedicated clusters are also set up for applications like `PIE`, `Car services`, `Maximo`, and `CIL`.

!!! tip "Visit [OCP Report](https://ocpreport-ocpreport-prod.apps.ocp-shared-v1-nonprod.volvocars.biz/ocpreport/ocr/index.html) to view complete list of clusters and other metrics"

## OpenShift Cluster general information - Clusters hosted in Azure (Vanilla OpenShift and ARO)

| Cluster Name                      | Platform    | Site/Region | Environments | Compute Subnet       | Ingress IP    | Console URL                                                                                   | API URL                                                 | Vault Auth Backend   |
|----------------------------------|-------------|-------------|--------------|---------------------|---------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|----------------------|
| `SANDBOX`                        | `Azure`     | `WEU`       | `NA`         |                     | `10.41.159.42`| [Console](https://console.openshift-console.apps.sandbox-net.sandbox.volvocars.net)            | `https://api.sandbox-net.sandbox.volvocars.net:6443`     | `NA`                 |
| `PIE-NON PROD_VANILLA_AZURE`    | `Azure`     | `WEU`       | `Non Prod`   | `10.48.66.160/27`   | `10.48.66.172`| [Console](https://console-openshift-console.apps.pie-nonprod.volvocars.biz/)                   | `https://api.pie-nonprod.volvocars.biz:6443`             | `pie-nonprod-weu`     |
| `PIE-PROD_VANILLA_AZURE`        | `Azure`     | `WEU`       | `Prod`       | `10.48.67.32/27`    | `10.48.67.44` | [Console](https://console-openshift-console.apps.pie-prod.volvocars.biz)                       | `https://api.pie-prod.volvocars.biz:6443`                 | `pie-prod-weu`        |
| `OCP NON PROD Vanilla Shared Cluster` | `Azure`     | `WEU`       | `Non Prod`   | `10.48.129.128/26`  | `10.48.129.135`| [Console](https://console-openshift-console.apps.ocp-shared-v1-nonprod.volvocars.biz)          | `https://api.ocp-shared-v1-nonprod.volvocars.biz:6443`   | `shared-v1-np-weu`    |
| `OCP PROD Vanilla Shared Cluster`| `Azure`     | `WEU`       | `Prod`       | `10.48.128.128/26`  | `10.48.128.141`| [Console](https://console-openshift-console.apps.ocp-shared-v1-prod.volvocars.biz/)            | `https://api.ocp-shared-v1-prod.volvocars.biz:6443/`     | `shared-v1-prod-weu`  |
| `CARSERVICE-QA_VANILLA_AZURE`   | `Azure`     | `WEU`       | `Non Prod`   | `10.49.202.192/26`  | `10.49.202.205`| [Console](https://console-openshift-console.apps.carservice-nonprod.volvocars.biz/)            | `https://api.carservice-nonprod.volvocars.biz:6443`      | `carservice-np-weu`   |
| `CARSERVICE-PROD_VANILLA_AZURE` | `Azure`     | `WEU`       | `Prod`       | `10.49.201.64/26`   | `10.49.201.77` | [Console](https://console-openshift-console.apps.carservice-prod.volvocars.biz/)               | `https://api.carservice-prod.volvocars.biz:6443`         | `carservice-prod-weu` |
| `ARO SHARED NON PROD`            | `Azure-ARO` | `WEU`       | `Non Prod`   | `10.50.114.64/26`   | `10.50.114.126`| [Console](https://console-openshift-console.apps.shared-azureocp-nonprod.volvocars.biz/)       | `https://api.shared-azureocp-nonprod.volvocars.biz:6443` | `shared-aro-np-weu`   |
| `ARO SHARED PROD`                | `Azure-ARO` | `WEU`       | `Prod`       | `10.50.113.64/26`   | `10.50.113.126`| [Console](https://console-openshift-console.apps.shared-azureocp-prod.volvocars.biz/)          | `https://api.shared-azureocp-prod.volvocars.biz:6443`    | `shared-aro-pr-weu`   |
| `ACS PROD AZURE`                 | `Azure`     | `WEU`       | `Prod`       | `10.50.100.64/26`   | `10.50.100.76` | [Console](https://console-openshift-console.apps.ocplus-prod.ocp-mgmt.volvocars.net/)          | `https://api.ocplus-prod.ocp-mgmt.volvocars.net:6443`    | `ocplus-prod-weu`     |
| `MQ-AZUREOCP-NONPROD CLUSTER`   | `Azure-ARO` | `WEU`       | `Prod`       | `10.50.144.64/26`   | `10.50.145.126`| [Console](https://console-openshift-console.apps.mq-azureocp-nonprod.volvocars.net/)           | `https://api.mq-azureocp-nonprod.volvocars.net`          | `mq-aro-np-weu`       |
| `MQ-AZUREOCP-PROD CLUSTER`      | `Azure-ARO` | `WEU`       | `Non Prod`   | `10.50.145.64/26`   | `10.50.144.126`| [Console](https://console-openshift-console.apps.mq-azureocp-prod.volvocars.net/)              | `https://api.mq-azureocp-prod.volvocars.net`             | `mq-aro-prod-weu`      |
| `MAXIMO NON-PROD`                | `Azure`     | `WEU`       | `Non Prod`   | `10.50.176.0/24`    | `10.50.176.48` | [Console](https://console-openshift-console.apps.maximo-nonprod.volvocars.net)                | `https://api.maximo-nonprod.volvocars.net:6443`          | `NA`                  |
| `MAXIMO-PROD`                   | `Azure`     | `WEU`       | `Prod`       | `10.50.175.64/27`   | `10.50.175.76` | [Console](https://console-openshift-console.apps.maximo-prod.volvocars.net/)                   | `https://api.maximo-prod.volvocars.net:6443`             | `NA`                  |
| `MAXIMO -TRAINING`               | `Azure`     | `WEU`       | `Non Prod`   | `10.50.176.96/27`   | `10.50.176.108`| [Console](https://console-openshift-console.apps.maximo-training.volvocars.net/)               | `https://api.maximo-training.volvocars.net:6443`         | `NA`                  |
| `MAXIMO-QA`                     | `Azure`     | `WEU`       | `Non Prod`   | `10.50.176.64/27`   | `10.50.176.76` | [Console](https://console-openshift-console.apps.maximo-qa.volvocars.net/)                     | `https://api.maximo-qa.volvocars.net:6443`                | `NA`                  |
| `MAXIMO-DEV`                    | `Azure`     | `WEU`       | `Non Prod`   | `10.50.176.128/27`  | `10.50.176.137`| [Console](https://console-openshift-console.apps.maximo-dev.volvocars.net)                     | `https://api.maximo-dev.volvocars.net:6443`               | `NA`                  |
| `ARO-CIL-NONPROD`               | `Azure-ARO` | `WEU`       | `Non Prod`   | `10.55.27.64/26`    | `10.55.27.126`| [Console](https://console-openshift-console.apps.cil-azureocp-nonprod.volvocars.biz/)          | `https://api.cil-azureocp-nonprod.volvocars.biz:6443`    | `cil-aro-np-weu`      |
| `ARO CIL-PROD`                 | `Azure-ARO` | `WEU`       | `Prod`       |                     | `10.46.41.126`| [Console](https://console-openshift-console.apps.cil-azureocp-prod.volvocars.biz/)             | `https://api.cil-azureocp-prod.volvocars.biz:6443`       | `cil-aro-prod-weu`    |
| `OBSERVABILITY NONPROD`          | `Azure`     |             | `Non Prod`   |                     | `10.46.21.126`| [Console](https://console-openshift-console.apps.observability-nonprod.volvocars.biz)         |                                                         | `observability-nonprod-weu` |
| `OBSERVABILITY PROD`             | `Azure`     |             | `Prod`       |                     | `10.46.24.126`| [Console](https://console-openshift-console.apps.observability-prod.volvocars.biz/)            |                                                         | `NA`                  |
| `TURBONOMIC PROD`                | `Azure`     |             | `Prod`       |                     | `10.46.32.126`| [Console](https://console-openshift-console.apps.turbonomic-prod.volvocars.biz/)               |                                                         | `NA`                  |


!!! note

    - `Compute Subnet` to be used for firewall requests as source subnet.
    - `Ingress IP` to be used for LB backend pool IPs for custom URLs VIP, which is the default IP for all Ingress to the cluster.
    - `API URL` is needed for accessing API cluster or for `oc` login.
    - `Vault Auth Backend` is used for onboarding namespace into `Central Vault`. For more details please refer to [Namespace Onboard](https://backstage.volvocars.biz/docs/default/component/ocp-admin-documentation/instructions/vault-namespace-onboard/)
