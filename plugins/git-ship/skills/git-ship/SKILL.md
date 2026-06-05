---
name: git-ship
description: Stage all changes, sanity-check for suspicious files, commit with a generated message, and push.
---

# git-ship

Stage everything, sanity-check, commit, push. No prompts.

## Steps

1. Run `git add -A`.
2. Run `git diff --cached --stat` to see what's staged. If nothing is staged, say "Nothing to ship." and stop.
3. **Sanity check:** Scan the staged file list for suspicious entries. Abort (with `git reset`) if ANY of these appear:
   - Dependency source/vendor directories (`node_modules/`, `vendor/`, `target/debug/`, `target/release/`, `.venv/`, `venv/`, `site-packages/`)
   - Build artifacts (`*.o`, `*.so`, `*.dylib`, `*.class`, `*.pyc`, `dist/`, `build/`)
   - Secrets or credentials (`.env`, `credentials.json`, `*.pem`, `*.key`, `id_rsa*`)
   - Large binaries (`.tar.gz`, `.zip`, `.jar`, `.whl`)
   - IDE/OS junk (`.DS_Store`, `Thumbs.db`, `.idea/`, `.vscode/`)
   If detected: run `git reset`, list the offending files, and say "Aborted — add these to .gitignore first." Then stop.
4. Run `git diff --cached` to read the actual changes.
5. Run `git log --oneline -5` to match the repo's commit message style.
6. Write a concise commit message (1 sentence, lowercase, no period, imperative mood). Focus on the "why" not the "what". Use a HEREDOC.
7. Run `git commit`.
8. Run `git push origin HEAD`.

## Rules

- Do not ask for confirmation. Just do it.
- Do not amend previous commits.
- Do not force push.
- Push to the current branch (HEAD), not hardcoded to main.
