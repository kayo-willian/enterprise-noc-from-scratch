# Asterisk and FreeRADIUS — VoIP and Network Authentication

**English** | [Português (Brasil)](../pt-BR/servicos/asterisk-freeradius.md)

## 1. Overview

The Enterprise NOC — From Scratch laboratory includes a dedicated Linux computer for VoIP and network authentication services.

The server hosts two main applications:

- **Asterisk:** IP telephony management using SIP/PJSIP.
- **FreeRADIUS:** Centralized network authentication using the RADIUS protocol.

The same computer also runs Zabbix Agent for monitoring and OpenSSH for remote administration.

This documentation combines the technical reports and system inventory collected in October and November 2026 with photographs taken on November 6, 2026.

Configuration details are described according to the available records. Features without direct test evidence are identified accordingly.

## 2. Server Infrastructure

The services run on a physical Dell OptiPlex 3020.

| Component | Documented specification |
|---|---|
| Computer | Dell OptiPlex 3020 |
| Processor | Intel Core i5-4590 |
| Memory | Approximately 8 GB |
| Operating system | Debian GNU/Linux forky/sid |
| Kernel | Linux 7.2.12+deb14-amd64 |
| Network interface | enp2s0 |
| IPv4 address | 192.168.50.2/24 |
| Default gateway | 192.168.50.1 |
| VLAN | 50 |
| Root filesystem | ext4, approximately 211.21 GiB |

The hardware and operating system information comes from the Linux system inventory collected on November 6, 2026.

The server belongs to VLAN 50, which contains the laboratory's voice infrastructure and the locally hosted authentication service.

### 2.1 Service Inventory

The service report dated November 6 lists the following daemons as active:

| Service | Function | Documented status |
|---|---|---|
| Asterisk | IP telephony | active (running) |
| FreeRADIUS | Network authentication | active (running) |
| Zabbix Agent | System monitoring | active (running) |
| OpenSSH | Remote administration | active (running) |

These statuses represent the recorded system state, not a continuous availability guarantee.

## 3. Asterisk — IP Telephony

Asterisk provides IP PBX functionality for the laboratory.

The technical documentation identifies **Asterisk 22.10.1** and describes the use of the PJSIP channel driver.

The documented architecture uses:

- SIP/PJSIP for endpoint registration and call signaling.
- RTP for voice traffic.
- Internal extensions for departmental communication.
- A dialplan for routing calls and executing test applications.

### 3.1 Network Services and Ports

| Protocol | Port | Purpose |
|---|---|---|
| SIP/UDP | 5060 | SIP signaling and endpoint registration |
| RTP/UDP | 10000–20000 | Voice media transport |
| AMI/TCP | 5038 | Asterisk management interface, documented as localhost-only |
| IAX2/UDP | 4569 | IAX2 functionality described in the technical documentation |

These ports come from the technical configuration report. Their inclusion does not independently confirm that every interface or protocol was actively used.

### 3.2 Documented Extensions

Two Grandstream IP telephones are associated with the Asterisk server.

| Extension | Department | Documented IP | Device |
|---|---|---|---|
| 1001 | Sales | 192.168.50.10 | Grandstream IP phone |
| 1002 | IT | 192.168.50.11 | Grandstream IP phone |

The Asterisk technical report identifies both extensions as available at the time of its earlier observation.

The photographs taken on November 6 confirm the presence of both physical telephones and their displayed IP addresses.

They do not independently prove successful calls between the extensions.

### 3.3 IT Telephone

![Grandstream IT telephone](../assets/images/voip/20261106_182149.jpg)

The photograph shows a Grandstream IP telephone identified as the IT department's extension.

The device screen displays:

`192.168.50.11`

This address matches the network information documented for extension 1002.

### 3.4 Sales Telephone

![Grandstream Sales telephone](../assets/images/voip/20261106_182236.jpg)

The second Grandstream telephone is identified as the Sales department's extension.

The device screen displays:

`192.168.50.10`

This address matches the documented network information for extension 1001.

The exact telephone models could not be reliably established from the available photographs.

## 4. Dialplan Configuration

The Asterisk documentation describes an internal dialplan implemented through `/etc/asterisk/extensions.conf`.

The following extensions are documented:

| Extension | Application | Purpose |
|---|---|---|
| 1001 | Dial(PJSIP/1001,30,tT) | Calls the Sales extension |
| 1002 | Dial(PJSIP/1002,30,tT) | Calls the IT extension |
| 8888 | Playback(hello-world) | Audio playback test |
| 9999 | Echo() | Interactive audio echo test |

The documented calls use a 30-second timeout and allow call-transfer functionality.

The additional test extensions provide mechanisms for checking audio playback and bidirectional audio behavior.

The available records document these configurations but do not include independent recordings or call-detail records proving successful execution of every test.

## 5. FreeRADIUS — Network Authentication

FreeRADIUS provides centralized authentication functionality for the laboratory's network infrastructure.

The technical documentation identifies **FreeRADIUS 3.2.10** and describes an authentication environment using:

- RADIUS.
- IEEE 802.1X.
- EAP-PEAP.
- MSCHAPv2.
- WPA2/WPA3-Enterprise configurations.

The documented architecture associates the FreeRADIUS server in VLAN 50 with the corporate wireless network in VLAN 60.

### 5.1 Authentication Architecture

```text
Wireless Client
       |
Corporate Wi-Fi / Access Point
       |
RADIUS Authentication Request
       |
Network Routing
       |
FreeRADIUS Server
VLAN 50 — 192.168.50.2
```

This diagram describes the architecture recorded in the project documentation.

The collected files do not contain complete authentication logs proving successful end-to-end authentication from the photographed wireless equipment.

### 5.2 RADIUS Ports

| Protocol | Port | Purpose |
|---|---|---|
| RADIUS/UDP | 1812 | Authentication |
| RADIUS/UDP | 1813 | Accounting |

The FreeRADIUS configuration directory is documented as:

`/etc/freeradius/3.0/`

Relevant configuration components include:

| Component | Function |
|---|---|
| clients.conf | Definition of authorized RADIUS clients |
| users | Local user authentication records |
| EAP configuration | Authentication method configuration |
| freeradius.service | Service management through systemd |

The original configuration documentation contains authentication secrets and user passwords. These values are deliberately excluded from this public document.

### 5.3 Authentication Security

The recorded PEAP/MSCHAPv2 architecture requires clients to validate a trusted CA certificate and the expected authentication-server identity. Disabling certificate validation would weaken protection against rogue servers.

## 6. Operational Architecture and Design Considerations

### Asterisk: How a Departmental Call Is Routed

The documented topology pairs two Grandstream phones on the voice network with the Asterisk server at `192.168.50.2`. The following is a **protocol-level explanation of the configured design**, not a claim that a call was captured:

1. An IP telephone registers its SIP identity through **PJSIP**, using SIP signaling over UDP `5060` in the documented configuration.
2. A user dials `1001` (Sales) or `1002` (IT); the internal dialplan in `/etc/asterisk/extensions.conf` selects `Dial(PJSIP/<extension>,30,tT)`.
3. Asterisk attempts the destination for up to **30 seconds**. The `tT` flags enable the documented transfer capabilities for the two call legs.
4. Once a call is established, **RTP** carries voice media; the technical report lists UDP `10000–20000` for media. SIP registration status, call routing and audio quality are **different tests**.

The `8888` playback application checks audio delivery from the PBX, while `9999` uses `Echo()` to help assess bidirectional media. These tests would produce useful evidence only if their results were actually recorded.

### FreeRADIUS: How Enterprise Wireless Authentication Is Intended to Work

The documented network design places corporate Wi-Fi in **VLAN 60**, the authentication server in **VLAN 50**, and RADIUS authentication/accounting on **UDP 1812/1813**.

1. A wireless client requests access through an **802.1X authenticator** (the access equipment).
2. The authenticator relays EAP authentication information to FreeRADIUS using RADIUS.
3. In the recorded **PEAP/MSCHAPv2** design, the client must verify the trusted authentication server certificate and identity before submitting credentials.
4. The result of authentication determines whether access is permitted under the actual device policy.

This is the **intended interaction**, not a captured authentication exchange. In particular, the corporate [Wi-Fi VLAN 60 record](../networking/corporate-wifi-vlan60.md) does **not** confirm that the photographed TP-Link Archer AX53 was configured as a RADIUS client or supports/used the recorded enterprise authentication design. A VLAN assignment or an active `freeradius` daemon cannot establish that missing evidence.

### Separation of Services and Security Boundaries

Running telephony and network authentication on a dedicated Linux computer separates those daemons from the Docker monitoring/application host. It also introduces an explicit **cross-VLAN dependency**: monitoring from the infrastructure network and enterprise wireless authentication must reach the server only through permitted routes and access controls. Actual ACL enforcement and end-to-end Wi-Fi authentication were not verified in the collected material.

The reported AMI port `5038` is documented as **localhost-only**; do not infer remote exposure from the port inventory. PJSIP identities, RADIUS shared secrets, user passwords and certificate private keys are intentionally absent from the public repository. Availability monitoring of this Linux host does not validate access-control correctness, SIP registration or media flow.


## 7. Monitoring Integration

The Asterisk/FreeRADIUS host (`192.168.50.2`) is monitored through Zabbix Agent; the main Zabbix server was recorded at `192.168.10.12`. The Grafana dashboard shows historical resource and availability metrics:

![Grafana monitoring of Asterisk and Linux servers](../assets/images/monitoring/grafana/grafana_dashboard_asterisk.png)

These host metrics do not verify SIP calls or RADIUS authentication. See [Grafana](../monitoring/grafana-monitoring.md) and [Zabbix](../monitoring/zabbix-monitoring.md).

## 8. Diagnostic Procedures

The following read-only commands are useful for inspecting the documented services on the Linux host.

### Service Status

```bash
systemctl status asterisk --no-pager
systemctl status freeradius --no-pager
systemctl status zabbix-agent --no-pager
```

### Asterisk Extensions

```bash
asterisk -rx "pjsip show endpoints"
asterisk -rx "core show channels"
asterisk -rx "dialplan show interno"
```

### Network Listening Ports

```bash
sudo ss -tulnp
```

These commands are examples of local diagnostic procedures. Their outputs were not independently collected for every validation step in this documentation.

Before publishing diagnostic output, authentication details, internal identities, and other sensitive information must be reviewed.

## 9. Evidence, Gaps and Next Validation Steps

The following matrix preserves the distinction between **implementation records**, **observations** and **still-missing tests**:

| Area | Available evidence | What a future validation would need |
|---|---|---|
| Linux host | November 6 system report: Debian, kernel, IPv4, storage and four running services | New dated `systemctl` output and relevant service logs |
| Telephony | October 30 Asterisk configuration report; dialplan `1001`/`1002`; two phone photographs | Dated PJSIP registration output, successful bidirectional call, audio check and (if approved) sanitized call records |
| Enterprise Wi-Fi authentication | FreeRADIUS report: configuration directories, methods and ports | Confirm authenticator support/configuration, trusted client CA/server identity, successful/failed RADIUS exchange and permitted VLAN path |
| Host monitoring | Historical Zabbix/Grafana metrics for the server | Distinct checks of SIP reachability, registration and RADIUS authentication, not just CPU/RAM |

**Operational failure points to consider:** incorrect SIP endpoint credentials or registration, routing/firewall restrictions between voice devices and services, RTP audio-path issues, incorrect RADIUS client definition or shared secret, and unsafe PEAP certificate validation. These are **diagnostic possibilities**, not incidents proven to have occurred.

For a future authorized investigation, start with the read-only `systemctl`, `asterisk -rx` and `ss` commands already listed above, record time-stamped results, and avoid publishing identities or secrets. Do not label authentication or call flows as operationally validated until they have corresponding test evidence.


## 10. Evidence Scope

| Evidence | What it establishes |
|---|---|
| Linux system inventory — November 6 | Server hardware, operating system, network interface, and storage information |
| Asterisk technical document — October 30 | Documented PJSIP architecture, extensions, dialplan, and ports |
| FreeRADIUS technical document | Documented authentication architecture and service configuration |
| Service report — November 6 | Recorded daemon status and service roles |
| IT telephone photograph | Physical Grandstream device displaying 192.168.50.11 |
| Sales telephone photograph | Physical Grandstream device displaying 192.168.50.10 |
| Grafana dashboard | Historical monitoring information for the Linux server |

The collected records do not contain independent results for:

- Successful voice calls between the two Grandstream devices.
- Successful end-to-end 802.1X authentication from the corporate wireless equipment.
- Exact models of the Grandstream telephones.
- Continuous availability of Asterisk and FreeRADIUS.
- Current service configuration after November 6, 2026.

The original technical PDFs and service report are not published directly because they contain authentication secrets and internal configuration details.

## 11. Related Documentation

- [Workstation and Server Inventory](../endpoints/workstation-inventory.md)
- [Zabbix Monitoring](../monitoring/zabbix-monitoring.md)
- [Grafana Monitoring](../monitoring/grafana-monitoring.md)
- [Docker Infrastructure and Services](../containers/docker-services.md)

