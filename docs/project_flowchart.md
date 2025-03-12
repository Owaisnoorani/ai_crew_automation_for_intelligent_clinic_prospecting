# AI Crew Automation for Intelligent Clinic Prospecting - Flow Diagram

```mermaid
graph TD
    A[Start] --> B[Clinic Lead Finder]
    B -->|Search Results| C[Clinic Web Scraper]
    C -->|Extracted Data| D[Clinic Data Classifier]
    D -->|Classified Data| E[Clinic Data Validator]
    E -->|Validated Data| F[Clinic Data Integrator]
    F -->|Integrated Data| G[Clinic Task Scheduler]

    subgraph Lead Finder Process
        B --> B1[Search Internet]
        B1 --> B2[Process Search Results]
        B2 --> B3[Filter Clinic URLs]
    end

    subgraph Web Scraping Process
        C --> C1[Extract Website Content]
        C1 --> C2[Parse Clinic Details]
        C2 --> C3[Extract Contact Info]
    end

    subgraph Data Classification
        D --> D1[Classify by Specialty]
        D1 --> D2[Classify by Location]
        D2 --> D3[Classify by Provider Type]
    end

    subgraph Data Validation
        E --> E1[Remove Duplicates]
        E1 --> E2[Validate Data Fields]
        E2 --> E3[Cross-reference Sources]
    end

    subgraph Data Integration
        F --> F1[Format Data]
        F1 --> F2[Generate Reports]
        F2 --> F3[CRM Integration]
    end

    subgraph Task Automation
        G --> G1[Schedule Tasks]
        G1 --> G2[Monitor Execution]
        G2 --> G3[Generate Reports]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bbf,stroke:#333,stroke-width:2px
    style D fill:#bbf,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px
    style G fill:#bbf,stroke:#333,stroke-width:2px
</code_block_to_apply_changes_from> 