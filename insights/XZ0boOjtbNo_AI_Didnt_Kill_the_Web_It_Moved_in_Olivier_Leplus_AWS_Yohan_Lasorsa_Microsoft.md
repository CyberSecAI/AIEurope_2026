# Overview

## Summary
Olivier Leplus and Yohan Lasorsa discuss the integration of AI into the web development lifecycle, covering AI coding agent skills, browser-based AI assistance, on-device AI APIs, and the shift towards agentic web applications.

## Key Takeaway
Embrace AI as a native component of the web by utilizing coding agent skills, browser-integrated debugging tools, and on-device AI APIs to build more efficient and interactive applications.

# Insights

## AI Coding Agent Skills
- Use skills as lightweight plugins to add domain expertise and new capabilities to your AI coding agents.
- Describe skills in simple text formats based on open specifications to ensure compatibility across different agent platforms.
- Skills are loaded dynamically into the agent’s context only when they are relevant to the current task.

## Agentic Web Workflows
- Automate repeatable development workflows like running Playwright tests and recording video previews of new UI features.
- Integrate communication tools like Telegram or Slack into your coding loops to receive real-time updates and test URLs.
- Maintain human-in-the-loop control by requiring explicit confirmation before an agent closes GitHub issues or merges changes.

## Browser-Integrated AI Debugging
- Enable "AI Innovation" flags in browser dev tools to access native AI assistance for explaining console errors.
- Use built-in "Debug with AI" buttons to analyze network failures and get specific hints for fixing CORS issues.
- Leverage AI-powered DOM analysis to explain complex layout problems and suggest immediate CSS fixes directly in the browser.

## On-Device Web AI APIs
- Utilize emerging browser APIs to run summarization, writing, and proofreading tasks directly in the user's browser.
- Implement summarize and proofreader APIs to provide intelligent features without making expensive and slow cloud service calls.
- Run models locally on the user's machine to improve privacy and reduce latency for real-time text analysis tasks.

## Performance Optimization with AI
- Use AI agents to control Chrome DevTools and perform automated performance audits across different network throttling scenarios.
- Analyze LCP and CLS metrics with AI to identify specific causes of delay like oversized images or render-blocking CSS.
- Generate granular performance reports and actionable guidelines to optimize web applications for 3G and slow internet connections.

## Local Model Management
- Manage the storage of large on-device models by allowing the browser to download them once for shared use.
- Monitor model downloads with dedicated functions to provide users with progress feedback during the initial setup phase.
- Be aware that browsers may automatically delete local models to free up system storage if disk space runs low.

## Agentic Web App Era
- Prepare for an era where AI agents use web applications alongside humans, requiring apps to be agent-friendly.
- Apply non-permanent CSS tweaks live in the browser and use "Apply to Workspace" to sync changes back to source code.
- Bridge the gap between visual design in DevTools and permanent source code updates using integrated AI workspace tools.

## Future of AI-First Development
- Move beyond asking "Can I code with AI?" to focusing on how to get the best results from agents.
- Adopt standard files like agents.md to define persistent instructions and preferences for your AI development environment.
- Combine local AI APIs with powerful frontier models to create seamless, intelligent user experiences across the entire web.
