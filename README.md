# Agency Finance Automation Toolkit 🚀

## Overview
This repository contains a suite of financial tools designed specifically for **High-Growth Marketing Agencies**. It addresses the core challenges of scaling an agency finance function:

1.  **Media Buying Reconciliation:** Automating the matching of ad spend invoices against client liability accounts to prevent margin erosion.
2.  **Squad Unit Economics:** Breaking down P&L by "Growth Squad" to measure true efficiency.
3.  **Cash Flow "Float" Management:** Forecasting liquidity risks associated with funding client ad spend.

## The Data Flow Architecture

```mermaid
graph TD
    A[Data Sources] -->|Export| B(Processing Engine - Python)
    
    subgraph Sources
    A1[Facebook/Google Ads API]
    A2[Xero - Client Fund Ledger]
    A3[Deel/Payroll Data]
    end
    
    B -->|Reconcile| C{Ad Spend<br/>Match?}
    C -->|Yes| D[Clear Liability<br/>(No Risk)]
    C -->|No| E[Flag Variance<br/>Report]
    
    B -->|Allocate| F[Squad P&L Model]
    
    F -->|Output| G[Executive Dashboard]
    G --> H[Profitability<br/>per Squad]
    G --> I[Cash Flow<br/>'Float' Risk]
