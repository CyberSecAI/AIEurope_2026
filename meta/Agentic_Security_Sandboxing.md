# Agentic Security & Sandboxing

## Summary
Securing autonomous agents requires a "default deny" model, lightweight sandboxing, and identity-aware proxies to ensure safe, traceable, and trusted execution.

## Key Takeaway
Harden agent environments with capability-based security and sandboxing to ensure safe autonomous operation.

# Insights

## Default Deny Security
- Capability-based security enforces a "default deny" model, granting agents minimal, explicit permissions for files, network, and system access.
- Restricting agent permissions to the absolute minimum necessary for a task reduces the potential impact of malicious or erroneous behavior.
- Explicitly defining and monitoring agent capabilities ensures that autonomous actions are both predictable and safe for the overall system.

## Safe Runtime Execution
- Lightweight V8 isolates and containers ensure that untrusted AI-generated code executes in safe, isolated, and fully traceable environments.
- Running agentic code in a sandbox provides an extra layer of protection against unauthorized access and system-level vulnerabilities.
- Real-time monitoring and logging of sandboxed activities allow for the rapid identification and triaging of any security issues that arise.

## Trusted Control Planes
- Real-world agent security requires hardening control planes with trusted proxies to eliminate brittle token management and unauthorized tool execution.
- Decoupling authentication from the application logic allows for more flexible and robust security policies across the entire agentic network.
- Identity-aware proxies ensure that only authorized users and agents can access sensitive organizational tools and data sources at all times.

## Enterprise Identity and Access
- Plain text access tokens where agents can access them are biggest security vulnerability currently.
- OAuth with step-up challenges enables clean installs with minimal permissions, expanding scope only when needed.
- Context needs security scanning: credentials, prompt injections, third-party risks detected before agent loads files.
- Delegated identity for users and agents becomes critical with role-based access scoping per team.

# Related Talks

- **[Why and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare](../insights/AHtGAgQ0Q_Q_Why_and_how_you_need_to_sandbox_AI_Generated_Code_Harshil_Agrawal_Cloudflare.md)**
- **[Your Insecure MCP Server Won't Survive Production — Tun Shwe, Lenses](../insights/BurJvbqFr4c_Your_Insecure_MCP_Server_Won_t_Survive_Production_Tun_Shwe_Lenses.md)**
- **[Building Your Own Secure AI Workflows: Human-in-the-Loop Automation with n8n — Liam McGarrigle](../insights/tDArkCqjA-c_Liam_McGarrigle_Building_Your_Own_Secure_AI_Workflows_Human_in_the_Loop_Automation_with_n8n.md)**
- **[Lobster Trap: OpenClaw in Containers — Sally Ann O'Malley](../insights/F1DYkY1BlfM_Lobster_Trap_OpenClaw_in_Containers_Sally_Ann_OMalley.md)**
- **[Lessons from Scaling GitHub's Remote MCP Server — Sam Morrow, GitHub](../insights/0n3MKk7r60w_Lessons_from_Scaling_GitHubs_Remote_MCP_Server_Sam_Morrow_GitHub.md)**
- **[What we learned scaling MCPs to Enterprise — Karan Sampath, Anthropic](../insights/CD6R4Wf3jnY_What_we_learned_scaling_MCPs_to_Enterprise_Karan_Sampath_Anthropic.md)**
- **[One Login to Rule Them All: Cross-App Access for MCP — Garrett Galow, WorkOS](../insights/EmhRyw6xeT0_One_Login_to_Rule_Them_All_Cross-App_Access_for_MCP_Garrett_Galow_WorkOS.md)**
- **[Context Is the New Code — Patrick Debois, Tessl](../insights/bSG9wUYaHWU_Context_Is_the_New_Code_Patrick_Debois_Tessl.md)**
