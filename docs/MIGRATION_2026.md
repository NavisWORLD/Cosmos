# 2026 Repository Reconstruction

The public repository had accumulated a large unrelated Farnsworth codebase and packaging layer. The cleanup removed it from the current tree while preserving the complete prior state in Git history and the backup branch `backup/pre-cosmos-cleanup-2026-08-12`.

Removed categories included:

- `farnsworth/` and Farnsworth `.egg-info` packages
- Farnsworth wheel/sdist artifacts
- Farnsworth root Python/Node launchers and MCP proxy
- Farnsworth network relay/config/docs/tests
- the Farnsworth/Timothy White license text
- tracked `node_modules`
- compiled `__pycache__`/`.pyc` trees that had no corresponding public source
- generated logs/scanner/test outputs
- runtime archival conversation/state dumps from the public tree
- local agent/tool state

The new COSMOS source was rebuilt as a small dependency-free core plus explicit optional integration boundaries. This does not claim to reconstruct every historical private/local module byte-for-byte; it establishes a readable, testable public foundation that matches the documented COSMOS architecture and can accept further modules as separate reviewed updates.
