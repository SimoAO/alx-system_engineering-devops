SSH Access Outage


Issue Summary:
Duration:
January 18, 2024, 11:30 PM - January 19, 2024, 1:15 AM (GMT+1)
Impact:
Users experienced a denial of SSH access to the web server, affecting 100% of users attempting to connect during the outage.
Root Cause:
The root cause of the outage was identified as an incorrect public key associated with the SSH access to the web server. The public key discrepancy arose due to a recent creation of a new public key during work on the school's virtual machine, leading to an unauthorized key being used for authentication.
Timeline:
11:30 PM: Issue detected when attempts to access the web server via SSH were consistently denied.
11:35 PM: Investigation initiated to identify the cause. Monitoring alerts did not indicate any system-wide issues.
11:45 PM: Engineer noticed discrepancies in the SSH authentication logs, prompting a closer examination.
11:55 PM: Assumed the issue might be related to a misconfiguration or a compromised private key.
00:15 AM: Explored potential misleading paths, including server misconfigurations and network issues.
00:40 AM: Discovered that the public key on the server did not match the expected key for the user account.
00:55 AM: Identified the recent creation of a new public key during work on the school's virtual machine.
01:15 AM: Resolved the issue by updating the authorized_keys file with the correct public key.

Root Cause and Resolution:
The incorrect public key caused the SSH authentication failure. During work on the school's virtual machine, a new public key was inadvertently created, leading to the discrepancy. To address the issue, the authorized_keys file on the web server was updated with the correct public key associated with the user account, restoring SSH access.
Corrective and Preventative Measures:
To prevent a recurrence and improve the overall system:
- Investigate Key Management Processes: Review the process of managing SSH keys, ensuring that changes made on external systems are well-documented and communicated.
- Regular Audits: Implement regular audits of SSH configurations to detect unauthorized changes promptly.
- Documentation Enhancement: Update documentation to include a comprehensive guide on SSH key management and potential pitfalls.
- Automation of Key Deployment: Consider automating the deployment of SSH keys to minimize the risk of manual errors.
- Monitoring Enhancements: Enhance monitoring systems to provide real-time alerts for key-related anomalies.
Conclusion:
The SSH access outage was promptly addressed by identifying and correcting the incorrect public key. Moving forward, the implementation of preventative measures and process improvements will fortify the system against similar incidents, ensuring the integrity and security of SSH access.

