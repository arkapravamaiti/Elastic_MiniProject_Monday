# Git Workflow Guide

This document explains the branching strategy and workflow for the Elastic_MiniProject_Monday repository.

## 🌳 Branching Strategy

We follow a **Git Flow** model with three main branches:

```
dev (Development) → stage (Staging/Testing) → main (Production)
```

### Branch Purposes

| Branch | Purpose | Stability | Deploy To |
|--------|---------|-----------|-----------|
| **dev** | Active development and feature integration | 🔴 Unstable | Development environment |
| **stage** | Pre-production testing and validation | 🟡 Testing | Staging environment |
| **main** | Production-ready stable code | 🟢 Stable | Production environment |

## 📦 Version Control

We use **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Incompatible API changes (1.0.0 → 2.0.0)
- **MINOR**: New functionality, backward compatible (1.0.0 → 1.1.0)
- **PATCH**: Bug fixes, backward compatible (1.0.0 → 1.0.1)

### Pre-release Versions

- **0.x.x**: Development/beta versions (not production-ready)
- **1.x.x**: First stable production release

## 🔄 Development Workflow

### Step 1: Feature Development (dev branch)

```bash
# Switch to dev branch
git checkout dev

# Create a feature branch (optional for small changes)
git checkout -b feature/new-feature

# Make changes and commit
git add <files>
git commit -m "feat: Description of feature"

# Merge back to dev (if using feature branch)
git checkout dev
git merge feature/new-feature

# Push to remote
git push origin dev
```

### Step 2: Tagging Versions in Dev

```bash
# After completing a feature, tag it
git tag -a v0.X.0 -m "Version 0.X.0: Feature description"
git push origin v0.X.0
```

### Step 3: Promote to Stage

```bash
# Switch to stage branch
git checkout stage

# Merge from dev
git merge dev

# Push to remote
git push origin stage

# Create pull request: dev → stage (on GitHub)
```

### Step 4: Testing in Stage

- Run all tests
- Perform integration testing
- Validate with staging data
- Get approval from stakeholders

### Step 5: Promote to Production (main)

```bash
# Switch to main branch
git checkout main

# Merge from stage
git merge stage

# Tag production release
git tag -a v1.X.0 -m "Version 1.X.0: Production release description"

# Push to remote
git push origin main
git push origin v1.X.0

# Create pull request: stage → main (on GitHub)
```

## 📝 Commit Message Convention

We follow **Conventional Commits** format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat: Add SLA breach detection` |
| `fix` | Bug fix | `fix: Handle NaN values in upload` |
| `docs` | Documentation changes | `docs: Update README with new features` |
| `refactor` | Code refactoring | `refactor: Optimize data cleaning logic` |
| `test` | Adding tests | `test: Add unit tests for utils` |
| `chore` | Maintenance tasks | `chore: Update dependencies` |
| `style` | Code style changes | `style: Format code with black` |
| `perf` | Performance improvements | `perf: Optimize bulk indexing` |

### Example Commit

```bash
git commit -m "feat(enrichment): Add temporal feature extraction

- Add opened_weekday field
- Add opened_hour field
- Add opened_month and quarter fields
- Update documentation

Closes #123"
```

## 🏷️ Tagging Strategy

### Development Tags (0.x.x)

```bash
# v0.1.0 - Initial setup
git tag -a v0.1.0 -m "Version 0.1.0: Initial project setup"

# v0.2.0 - Data cleaning feature
git tag -a v0.2.0 -m "Version 0.2.0: Data cleaning pipeline"

# v0.3.0 - Upload feature
git tag -a v0.3.0 -m "Version 0.3.0: Elasticsearch upload"

# v0.4.0 - Verification tools
git tag -a v0.4.0 -m "Version 0.4.0: Data verification"
```

### Production Tags (1.x.x)

```bash
# v1.0.0 - First production release
git tag -a v1.0.0 -m "Version 1.0.0: Production release"

# v1.1.0 - New features
git tag -a v1.1.0 -m "Version 1.1.0: Add new enrichment features"

# v1.0.1 - Bug fix
git tag -a v1.0.1 -m "Version 1.0.1: Fix data validation bug"
```

## 🔀 Pull Request Process

### Creating a Pull Request

1. **Push your branch** to GitHub
2. **Go to GitHub repository**
3. **Click "Pull requests" → "New pull request"**
4. **Select branches**:
   - Base: `stage` (for dev → stage)
   - Compare: `dev`
5. **Fill in PR template**:
   - Title: Clear, concise description
   - Description: What changed and why
   - Checklist: Tests passed, docs updated
6. **Request review** from team members
7. **Address feedback** if any
8. **Merge** after approval

### PR Naming Convention

```
[TYPE] Brief description of changes

Examples:
[FEATURE] Add SLA breach detection
[BUGFIX] Fix NaN handling in upload
[DOCS] Update installation guide
[RELEASE] Prepare v1.0.0 release
```

### PR Description Template

```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] New feature
- [ ] Bug fix
- [ ] Documentation update
- [ ] Refactoring
- [ ] Release

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Unit tests passed
- [ ] Integration tests passed
- [ ] Manual testing completed

## Checklist
- [ ] Code follows project style guidelines
- [ ] Documentation updated
- [ ] All tests passing
- [ ] Version number updated (if applicable)
- [ ] CHANGELOG updated (if applicable)

## Related Issues
Closes #123
```

## 🚀 Release Process

### 1. Prepare Release

```bash
# Update version in files
# Update CHANGELOG.md
# Update README.md if needed
git commit -m "chore: Prepare for v1.X.0 release"
```

### 2. Create Release Tag

```bash
git tag -a v1.X.0 -m "Version 1.X.0: Release description"
git push origin v1.X.0
```

### 3. Create GitHub Release

1. Go to **Releases** on GitHub
2. Click **"Draft a new release"**
3. Select tag: `v1.X.0`
4. Release title: `Version 1.X.0`
5. Description: Copy from CHANGELOG
6. Click **"Publish release"**

## 🔧 Useful Git Commands

### View Branches

```bash
# List all branches
git branch -a

# Show current branch
git branch --show-current
```

### View Tags

```bash
# List all tags
git tag -l

# Show tag details
git show v1.0.0
```

### Sync with Remote

```bash
# Fetch all branches and tags
git fetch --all --tags

# Pull latest changes
git pull origin <branch>
```

### Branch Management

```bash
# Create new branch
git checkout -b <branch-name>

# Switch branches
git checkout <branch-name>

# Delete branch
git branch -d <branch-name>
```

### Merge Strategies

```bash
# Merge with commit
git merge <branch>

# Squash merge (combine all commits)
git merge --squash <branch>

# Rebase (rewrite history)
git rebase <branch>
```

## 📊 Current Repository State

### Branches

- **dev**: Latest development code (v0.4.0)
- **stage**: Staging/testing code (v0.4.0)
- **main**: Production code (v1.0.0)

### Tags

- `v0.1.0`: Initial project setup
- `v0.2.0`: Data cleaning pipeline
- `v0.3.0`: Elasticsearch upload
- `v0.4.0`: Data verification
- `v1.0.0`: First production release

### Files by Version

| Version | Files Added | Description |
|---------|-------------|-------------|
| v0.1.0 | .gitignore, README.md, .env.sample, requirements.txt, utils.py | Initial setup |
| v0.2.0 | dataClean.py | Data cleaning |
| v0.3.0 | upload_to_es.py | ES upload |
| v0.4.0 | verify_es.py | Verification |

## 🎯 Best Practices

1. **Always work in dev branch** for new features
2. **Never commit directly to main** - always use PRs
3. **Tag every significant version** in dev before promoting
4. **Write clear commit messages** following convention
5. **Test thoroughly in stage** before production
6. **Keep branches in sync** - regularly merge dev → stage → main
7. **Document all changes** in commit messages and PRs
8. **Use semantic versioning** consistently

## 🔄 Regular Maintenance

### Weekly Tasks

- Merge dev → stage for testing
- Review and close stale PRs
- Update dependencies if needed

### Monthly Tasks

- Tag stable releases in main
- Create GitHub releases
- Update documentation
- Review and archive old branches

---

For questions or issues with the Git workflow, please open an issue on GitHub.

**Repository**: https://github.com/arkapravamaiti/Elastic_MiniProject_Monday

Made with ❤️ for best practices in version control
