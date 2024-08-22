### Postmortem: API Service Outage on August 10, 2024

#### Issue Summary

**Duration:** The outage lasted for 2 hours, from 14:00 to 16:00 UTC on August 10, 2024.

**Impact:** The outage caused our university management system’s API to become unresponsive. Approximately 70% of the users were unable to access course schedules, grades, or attendance records. Professors were unable to upload or modify student grades during this period.

**Root Cause:** A misconfigured load balancer in front of our API services led to uneven traffic distribution, resulting in server overload and eventual service unavailability.

---

### Timeline

- **14:00 UTC:** Monitoring system detected a significant increase in API response times, triggering an alert.
- **14:05 UTC:** Engineers began investigating the issue, initially suspecting a database bottleneck due to high traffic.
- **14:20 UTC:** Database queries and performance metrics appeared normal, leading the team to investigate the API servers themselves.
- **14:35 UTC:** The issue was escalated to the DevOps team after it was noted that only certain API servers were experiencing high load.
- **14:45 UTC:** DevOps identified a configuration error in the load balancer that was routing most of the traffic to only two out of five available servers.
- **15:00 UTC:** The team attempted to rebalance traffic manually but faced difficulties as the traffic had already caused some servers to become unresponsive.
- **15:20 UTC:** After restarting the affected servers and correcting the load balancer configuration, traffic was successfully distributed evenly across all servers.
- **16:00 UTC:** All services were fully restored, and the API was confirmed to be functioning normally.

---

### Root Cause and Resolution

**Root Cause:** The primary cause of the outage was a configuration error in our load balancer, which was inadvertently set to route traffic primarily to two API servers instead of evenly distributing it across all five servers. This resulted in those two servers becoming overloaded, leading to a rapid degradation in performance and eventually causing the API service to become unresponsive.

**Resolution:** The load balancer configuration was corrected to ensure proper distribution of incoming traffic across all available servers. After this change, the overloaded servers were restarted, and normal operation was restored. Additionally, monitoring checks were enhanced to detect uneven load distribution earlier.

---

### Corrective and Preventative Measures

**Improvements/Fixes:**
1. **Load Balancer Configuration Review:** Implement automated checks to verify load balancer configurations after any changes.
2. **Enhanced Monitoring:** Develop and deploy new monitoring alerts specifically targeting traffic distribution and server load balance.
3. **Stress Testing:** Regularly perform stress tests on the system to ensure that all components can handle unexpected traffic patterns.

**TODO:**
1. **Patch Load Balancer:** Update the load balancer configuration script to prevent similar misconfigurations in the future.
2. **Implement Traffic Monitoring:** Add monitoring tools that specifically track the distribution of traffic across servers.
3. **Server Health Checks:** Set up automated health checks that can temporarily remove overloaded servers from the load balancer pool until they recover.
4. **Incident Response Training:** Conduct training sessions for the engineering and DevOps teams to improve response times and decision-making during similar incidents.

This incident highlighted the importance of rigorous configuration management and proactive monitoring. By implementing the outlined corrective measures, we aim to prevent similar outages in the future and improve the resilience of our services.
