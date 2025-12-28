# User Story

**As a** service user  
**I need** the ability to manage customer accounts  
**So that** I can create, read, update, and delete account information efficiently.

---

## Acceptance Criteria

```gherkin
Given a running account service
When I make a request to create an account
Then the account should be created successfully

Given an existing account
When I request to read the account
Then the account details should be returned

Given an existing account
When I update account information
Then the account should be updated successfully

Given an existing account
When I delete the account
Then the account should be removed successfully


