# Ruhulla Sheik

**AI Platform Engineer | Senior Software Engineer | Platform Engineer | Integration Engineer**

**Email:** sk.ruhulla@gmail.com | **Phone:** +91 9035786999
**LinkedIn:** linkedin.com/in/ruhullasheik | **GitHub:** github.com/ruhullasheik

---

## Professional Summary

Curious engineer with 12+ years of experience at the intersection of supply chain, cloud, and AI. Started by connecting customer data to planning systems — ERP integrations, data pipelines, supply chain modelling — and grew into modernising legacy platforms into multi-tenant cloud solutions that reduce cost and improve operational efficiency at scale.

Today, the mission is different: partner with teams on their AI journey. That means embedding AI agents into enterprise platforms, building the infrastructure that lets those agents act on real business data, and accelerating adoption in organisations where the gap between AI potential and practical impact is still wide open.

The through-line across all of it: take complex, messy system boundaries and make them work cleanly together — whether that's ERP data, cloud services, or AI tools talking to enterprise APIs.

---

## Technical Skills

| Category | Technologies |
|---|---|
| **Languages** | C#, Python, Java, TypeScript, PowerShell, SQL |
| **Frameworks** | ASP.NET Core, FastMCP / FastAPI, Vue 3 / Vite, IdentityServer4, Entity Framework Core, Quarkus, Apache Airflow |
| **Databases** | PostgreSQL, SQL Server / Azure SQL, MongoDB / Azure Cosmos DB, Redis, HSQLDB |
| **Cloud (Azure)** | AKS, Bicep IaC, Key Vault, App Configuration, Container Registry, Service Bus, Application Insights, Container Instances, Azure Database for PostgreSQL |
| **DevOps** | Docker, Kubernetes (Helm, HPA), Azure Pipelines, Jenkins, GitHub Actions, uv, GitVersion |
| **Auth / Security** | OAuth2, OIDC, SAML2, JWT / JWKS, IdentityServer4 (Skoruba), Bandit (SAST), pip-audit (SCA), Veracode |
| **Observability** | OpenTelemetry (traces/metrics/logs), Grafana, Loki, Azure Application Insights |
| **Testing** | xUnit, pytest, Vitest, JUnit 4/5, JMeter, FakeItEasy, pytest-asyncio, Mockito |
| **Messaging / Events** | Apache Kafka, Azure Service Bus, RabbitMQ |
| **AI & Dev Tools** | Claude Code, Langflow (AIS), Azure OpenAI, MCP (Model Context Protocol) — authored custom MCP servers/tools, Spec-Driven Development (Polaris), AI-assisted implementation |
| **Other** | gRPC / Protocol Buffers, HashiCorp Consul, Ory Keto (Google Zanzibar), SAP JCo, Eclipse RCP / OSGi |

---

## Professional Experience

### Aptean *(formerly Logility Solutions, formerly AdapChain Solutions)* — Bangalore, India
**March 2014 – Present (12+ years)**

*AdapChain was acquired by Logility in 2019. Logility was subsequently acquired by Aptean.*

---

#### Senior Software Engineer / Tech Lead — Cloud Platform & AI Infrastructure
**August 2024 – Present**

**MCP Gateway** *(Jan 2026 – May 2026 | Python, FastMCP, FastAPI, PostgreSQL, Redis, OpenTelemetry, AKS)*
Tech lead and primary contributor (36 of 135 commits; mandatory PR reviewer) for a production AI gateway that auto-discovers OpenAPI specs and exposes them as MCP tools for AI agents and intelligence studio clients.

- Designed and built **instance-aware multi-tenant URL lookup** — MCP tools dynamically resolve per-tenant backend API URLs at runtime via the Client Catalog service, enabling a single gateway to serve multiple tenants with isolated routing
- Implemented **IAM-to-IDG token translation** auth strategy, distributed Redis token cache with hybrid local/Redis fallback, and COID-scoped tenant isolation across all cache keys
- Built the **Tool Catalogue discovery API** exposing all registered MCP servers and tools, enabling AI agents to enumerate gateway capabilities without manual configuration
- Owned end-to-end delivery of the **Logility Atlas Catalog Discovery Agent** — a conversational AI agent (Langflow / Azure OpenAI) that lets developers discover and compare MCP tools using plain-language queries; authored the Polaris spec, built the `logility_atlas` MCP server exposing the Catalogue API as MCP tools, configured the Langflow agent in AIS, and wired full gateway routing using Claude Code-assisted implementation
- Integrated **Bandit (SAST) + pip-audit (SCA)** into the CI/CD pre-build gate; remediated 6+ CVEs (urllib3, python-multipart, requests) — builds block on high/medium severity findings before image creation
- Served as **mandatory PR reviewer** enforcing architecture constraints, Ruff linting standards, NumPy docstrings, and 90%+ test coverage across 8 contributors
- Owns the full release pipeline: sbox → dev → qa → stg → prod across all five environments

**Platform Entitlements** *(Aug 2024 – Aug 2025 | C#, Vue 3, ASP.NET Core, Ory Keto, Kafka, PostgreSQL, MongoDB, AKS)*
Tech Lead for a universal authorization service implementing Google Zanzibar's relationship-based access control (ReBAC) via Ory Keto.

- Led overall technical direction across backend services, Vue.js SPA, Kubernetes infra, and CI/CD
- Designed **MetadataWorkerService** with delta-processing logic (toBeAdded / toBeDeleted diffs), minimizing redundant writes to the Keto authorization store at scale
- Built Groups management UI, Group Edit screen with unsaved-changes protection, User Details screen, and roles data population — all from scratch in Vue 3 / TypeScript
- Split monolithic Helm chart into modular `entitlements-service` + `keto` charts with a parent umbrella chart; configured memory-based HPA and tuned resource limits for production
- Stood up end-to-end **Grafana + Loki** structured log dashboards from scratch for on-call visibility

**IdentityGateway (Aptean IAM Integration)** *(Mar 2024 – Apr 2026 | C#, ASP.NET Core, IdentityServer4, EF Core, SQL Server, Docker, AKS)*
Lead engineer for the post-acquisition integration connecting Aptean's IAM system with Logility's Identity Gateway (IDG), enabling all Logility cloud products to authenticate through Aptean's corporate identity infrastructure.

- **Built the Token Translation endpoint from scratch** — exchanges Aptean IAM access tokens for IDG tokens, with automatic user provisioning on first login and full IAM configuration validation
- Extended the user model with `ApteanCoid` / `ApteanUoid` properties; mapped Aptean UOID/COID claims to `UserIdentity`; built tenant provisioning automation for Aptean IAM with schema validation
- Authored and implemented 3 Polaris specs: **.NET 10 migration**, **AutoMapper → Mapperly** (compile-time zero-reflection mapping), and ClaimTypes endpoint fix
- Fixed critical auth bugs: duplicate-username during token translation, user deletion missing `sub` claim, IAM config gaps

**Platform.ClientCatalog** *(Feb 2026 – Apr 2026 | C#, ASP.NET Core, .NET 10, MongoDB / CosmosDB, AKS)*
Key contributor (34 of ~134 commits) to the central tenant service URL registry consumed by the MCP Gateway.

- Designed and implemented **multi-instance service URL support** — MCP Gateway resolves the correct backend instance per tenant request, enabling non-multi-tenanted services to coexist without routing ambiguity
- Built **tenant-specific GET endpoints** enabling MCP Gateway to resolve all service URLs per tenant at runtime
- Fixed HTTPS `Location` header bug behind Traefik reverse proxy and Swagger OAuth2 flow in Kubernetes

**Infrastructure.Cloud.Params** *(Aug 2024 – May 2026 | Azure Bicep, Helm, Azure Pipelines, PowerShell)*
Key contributor to the LCR platform's configuration-as-code repo spanning dev/sbox/qa/stg/prod.

- Owned **MCP Gateway Helm configuration rollout** across all environments as part of the service launch
- Designed and implemented the **tenant services registry** (`services` section in `tenantinfo.json` + `new-tenant.ps1`) — the platform-wide single source of truth for tenant backend URLs consumed by both Client Catalog and MCP Gateway

---

#### Software Engineer / R&D Developer — Integration Platform & Workflow
**September 2020 – August 2024**

**Platform.Airflow / PAM (Process Automation Manager)** *(Sep 2021 – Aug 2023 | Python, Apache Airflow, Docker, Azure Pipelines, Azure Bicep)*
Primary owner and lead developer (162 of ~205 commits — 79%) of Logility's customized Apache Airflow deployment for authoring, scheduling, and monitoring platform DAGs.

- **Drove three consecutive Airflow version upgrades**: 2.2.4 → 2.3.3 → 2.4.3 → 2.6.1 — updating Dockerfile, Python security layer, Jinja2 HTML templates, and config templates for each release
- **Integrated IDG Single Sign-On** — enabled PAM operators to authenticate using the same OAuth2/OIDC identity as the rest of the LCR platform, with role assignment driven by IDG group membership
- Set up **Azure Pipelines CI/CD from scratch** and authored **Azure Bicep IaC** to deploy the PAM scheduler and worker as Azure Container Instance container groups
- Added **Azure Service Bus provider** enabling DAGs to publish messages to the platform message bus; hardened security with CSP headers, `X-Frame-Options: DENY`, and disabled Swagger UI

**AdapLink / LOG-RD-AL** *(Oct 2020 – Jan 2024 | Java 17, Quarkus, C# .NET 8, MSSQL, RabbitMQ, Redis, HashiCorp Consul)*
Key contributor (355 commits) to Logility's enterprise Java integration middleware and its Quarkus-based LOM microservice.

- **Built LOM batch reporting infrastructure** — Total Report, Detail Report Processor (configurable parallelism), PM Error reporting, and SVR_RESULT persistence across BatchGenerator and BatchProcess services
- **Implemented CommonAdd integration** — writes processed supply chain records into PM staging tables with Redis AtomicLong sequential numbering and multi-level (up to 9 levels) data support
- **Extended Consul service discovery for LOM** — dynamic endpoint resolution for CommonAdd, reporting service, and PDC at runtime
- **Built UserManager CLI tool** (standalone Java app) and **AdapLinkEncryption .NET 8 utility** (C# console app with unit tests) to fill developer tooling gaps
- **Responded to Log4Shell (CVE-2021-44228)** — patched Log4j2 across 160+ modules through 5 version upgrades; also upgraded MSSQL JDBC, Guava, RabbitMQ, and Apache CXF
- Managed 8 platform releases (21.02.1 through 24.01.1); authored and maintained Azure DevOps CI/CD pipelines

**AdapLink Templates** *(Sep 2020 – Aug 2023 | Python, XML, PowerShell, Azure Pipelines)*
Integration Engineer / Key Contributor (2nd highest commit volume) building configuration-as-code ERP integration templates deployed to supply chain customers.

- **Created Azure Pipelines CI/CD from scratch** — two-stage Build → Publish pipeline with pytest, versioned artifact generation, and Azure Blob Storage upload
- **Built IBP-ATP/CTP integration template** with batch-wise processing for high-volume order flows that timed out under single-pass approach
- **Created MPO and VOYAGER IO Cloud Sync templates**; extended SAP/HANA templates with ObjectStore and VBFA support; migrated deprecated SQL `text` type to `varchar(max)` across 4 template families
- **Introduced pytest** and wrote the project's first automated test suite for the `al_deploy` build tooling

**Identity.ProviderConfiguration** *(Nov 2023 – Jan 2024 | C#, TypeScript, Vue 3, ASP.NET Core, Redis, Docker, AKS)*
Full-stack contribution (32 of ~191 commits) to the admin UI for managing OIDC/SAML identity provider configurations.

- Implemented read-only UI mode for provider forms end-to-end (Vue 3 components, validation refactor, xUnit + Vitest tests, Azure Pipelines CI, Bicep IaC)

---

#### Integration Engineer — ERP Data Integration
**March 2014 – September 2020**

*AdapChain Solutions → Logility Solutions, Bangalore, India*

- **Owned end-to-end integration projects** for enterprise customers including SEI (7-Eleven), ATK, and VISTA — integrated SAP HANA and Oracle EBS systems alongside **daily delta file feeds** (incremental data exchange) into Logility's supply chain planning platform; owned the full pipeline: ERP extraction → automated cleansing and transformation → data modelling → planning system ingestion → planning outcomes back to customer
- Developed ERP integration templates and data extraction programs for supply chain planning applications (SAP, Oracle, JDE) using the AdapLink integration toolset
- Wrote rules-based transformation programs and built supply/demand data models for Logility Voyager (demand planning, supply planning, replenishment, production planning, inventory optimization)
- Designed standard integration templates for SAP, Oracle, and JDE ERP systems used across multiple customer deployments
- Handled Change Control board responsibilities; provided project and post-implementation customer support
- Worked as **Release Master** for the integration tool — performing regression tests, updating documentation, and coordinating versioned releases

---

## Personal Project

**Skill of Money** *(In development | Full-stack)*
A full-stack accounting application enabling users to track and manage financial transactions. *[Private repository — in active development]*

---

## Recommendation

> *"Ruhulla has been a vital contributor to several of our most critical technical initiatives. He has been instrumental in developing our new MCP (Model Context Protocol) Gateway, helping to securely bridge our enterprise SaaS APIs with autonomous AI agents. His ability to seamlessly pivot into complex AI engineering patterns while maintaining his established backend expertise is a testament to his versatility as a quick, action-oriented learner."*
>
> — **Robert Durell**, Senior Software Architect, Aptean *(direct manager, May 2026)*

---

## Certifications

- **Apache Airflow Fundamentals** — Astronomer (Credly badge)

---

## Education

| Degree | Institution | Year | Score |
|---|---|---|---|
| M.Tech | JNTU Kakinada | 2013 | 91% |
| B.Tech | JNTU Kakinada | 2011 | 71% |

---

## Contact

- **Email:** sk.ruhulla@gmail.com
- **Phone:** +91 9035786999
- **LinkedIn:** https://www.linkedin.com/in/ruhullasheik/
- **GitHub:** https://github.com/ruhullasheik/
