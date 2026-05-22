#!/bin/sh
# Run once after cloning: sh scripts/install-hooks.sh
cp scripts/pre-commit .git/hooks/pre-commit
cp scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-commit
chmod +x .git/hooks/pre-push
echo "Git hooks installed."
