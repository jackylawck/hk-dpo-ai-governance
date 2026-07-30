# Human Oversight & Escalation Protocol (人工監督與申訴機制)

**Document Control:** V1.0
**Framework Alignment:** ISO/IEC 42001:2023 (Annex A.8.3), EU AI Act (Article 14)
**Scope:** HK DPO GenAI Governance Sandbox (Deterministic Tier Classifier)

## 1. Human-in-the-Loop (HITL) Philosophy (人機協同理念)

This AI governance sandbox is designed exclusively as a **Decision Support System (決策支援系統)**. The final accountability for compliance assessment, risk tiering, and strategic deployment rests entirely with the designated human executive, AI Governance Professional, or legal counsel.

## 2. Operational Oversight Mechanisms (營運監督機制)

* **Pre-Execution Input:** Users must manually input organizational parameters and use cases accurately before any algorithmic routing begins.
* **Executive Verification:** All system-generated risk scorecards must be reviewed and cross-verified against official legal advice before board-level alignment or organizational implementation.
* **Override Capability:** Human operators (e.g., DPO, Lead Auditors) possess the absolute authority to override the system's generated risk tier based on nuanced corporate context or unprogrammed legal exceptions.

## 3. Escalation & Feedback Process (申訴與回饋流程)

In the event of a suspected logic error or conflicting compliance output:
1. **Immediate Cessation:** Cease utilizing the specific generated scorecard for official reporting.
2. **Log & Report:** Capture the specific input parameters and report to the AI Governance Lead.
3. **Manual Code Audit:** The AI Governance Lead will conduct a manual review of the deterministic `if-else` logic matrix to identify the routing failure.
4. **Logic Patch:** If a logical contradiction is verified, a code patch will be deployed, and an incident report will be logged in the risk register.
