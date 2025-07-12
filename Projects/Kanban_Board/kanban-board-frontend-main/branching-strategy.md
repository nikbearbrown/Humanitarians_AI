# Branching Strategy

## Branches

- **`main`**: The production branch. Only code that has been tested and approved should be merged here.
- **`develop`**: The integration branch where all features are merged before they are deployed to production.
- **Feature branches**: These branches are created from `develop` and used to work on specific features or fixes. They should follow the naming convention `feature/<feature-name>` or `fix/<issue-name>`.

## Workflow

1. **Creating a Feature Branch**: 
   ```bash
   git checkout develop
   git checkout -b feature/<feature-name>
   ```
2. **Merging a Feature Branch**:
   - Ensure all tests pass and code is reviewed.
   - Merge into `develop`:
     ```bash
     git checkout develop
     git merge feature/<feature-name>
     ```
3. **Deploying to Production**:
   - Merge `develop` into `main` after all features for the release are complete and tested:
     ```bash
     git checkout main
     git merge develop
     ```

## Branch Naming Conventions

- Feature branches: `feature/<feature-name>`
- Bugfix branches: `fix/<issue-name>`
