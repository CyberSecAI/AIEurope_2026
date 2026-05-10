# Overview

## Summary
Garrett Galow from WorkOS presents Cross-App Access for MCP, eliminating repetitive OAuth consent screens through centralized authentication.

## Key Takeaway
XAA uses identity providers to broker trust between MCP clients and servers seamlessly.

# Insights

## Authentication Pain Points
- Users face repetitive OAuth consent screens for each MCP server, creating friction and consent fatigue without understanding why.
- MCP breaks traditional single sign-on by assuming applications don't trust each other, forcing manual consent for every connection.
- IT teams lack visibility into which MCP servers employees connect to, creating security and compliance blind spots.

## Security Vulnerabilities
- OAuth tokens persist after employee offboarding, maintaining standing access for days or weeks beyond termination without IT control.
- Local machine compromises expose unmanaged API keys and MCP credentials that aren't tied to centralized identity providers.
- IT cannot revoke MCP access centrally during security incidents, unlike applications protected by single sign-on sessions.

## Cross-App Access Solution
- XAA uses IDJAG tokens from identity providers to broker trust between MCP clients and servers without user intervention.
- Access tokens are short-lived typically five minutes, automatically refreshing while SSO sessions remain active for better security posture.
- Users authenticate once to their IDP, then all MCP servers connect automatically using the existing trust relationship.

## Implementation for IT Admins
- IT creates managed connection policies in Okta specifying which MCP clients can access which server applications.
- Setup requires only existing SSO applications already configured, no additional infrastructure or major configuration changes needed.
- Policy enforcement happens at the IDP level, giving IT centralized control over which agents access sensitive systems.

## MCP Client Requirements
- Clients need XAA-compatible SSO connections to request IDJAG tokens from identity providers using refresh tokens from login.
- After receiving IDJAG tokens, clients exchange them with MCP servers for standard OAuth access tokens in existing flows.
- WorkOS handles the complete flow for clients like Cursor and Anthropic that use their authentication services.

## MCP Server Requirements
- Servers must announce JWT bearer type support to accept IDJAG tokens from clients connecting through identity providers.
- Token verification involves checking IDJAG signatures with the identity provider URL to ensure authenticity before issuing access.
- Once verified, servers issue standard OAuth access tokens, maintaining compatibility with existing MCP server implementations.

## Ecosystem Adoption Challenges
- Okta supports XAA for OIDC connections today with SAML support coming, but Microsoft Entra lacks implementation currently.
- Client protocol fragmentation exists with different implementations handling resource parameters and scopes inconsistently across platforms.
- Dynamic Client Registration gaps force manual client pre-registration, though newer CIMD standard addresses this with metadata documents.

## Authorization Limitations
- XAA solves authentication but not fine-grained authorization, users get their existing permissions without scope modifications today.
- Scope management extensions are being discussed to allow IDPs to define permission caveats alongside cross-app access grants.
- Audience URLs identify which MCP server applications are requested, configured in IDP to map applications to audiences.