sequenceDiagram
    participant User
    participant API
    participant BusinessLogic
    participant Database

    User->>API: List amenities
    API->>BusinessLogic: list()
    BusinessLogic->>Database: Fetch amenities from DB
    Database->>Database: Query all amenities
    Database-->>Database: Return amenities
    Database-->>BusinessLogic: Return amenities
    BusinessLogic-->>API: Return list of amenities
    API-->>User: Show amenities
