---
name: git-ship
description: Commit staged changes with a generated message and push to the current branch.
---

# git-ship

Commit whatever is staged and push. No prompts, no questions.

## Steps

1. Run `git diff --cached --stat` to see what's staged. If nothing is staged, say so and stop.
2. Run `git diff --cached` to read the actual changes.
3. Run `git log --oneline -5` to match the repo's commit message style.
4. Write a concise commit message (1 sentence, lowercase, no period, imperative mood). Focus on the "why" not the "what". Use a HEREDOC.
5. Run `git commit`.
6. Run `git push origin HEAD`.

## Rules

- NEVER stage files yourself. Only commit what the user has already staged.
- If nothing is staged, tell the user and stop. Do not `git add` anything.
- Do not ask for confirmation. Just do it.
- Do not amend previous commits.
- Do not force push.
- Push to the current branch (HEAD), not hardcoded to main.
