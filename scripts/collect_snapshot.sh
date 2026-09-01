#!/bin/sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
workspace_root=$(CDPATH= cd -- "$script_dir/../.." && pwd)

repositories="
Telescan-iOS
Telescan-api
Telescan-bot-app
Telescan-admin-bot
Telescan-nginx
Telescan-relay
Telescan-db
Telescan-monitoring
Telescan-info
Telescan-internal-docs
"

printf '# Telescan Frozen Baseline\n\n'
printf '**Captured (UTC):** %s  \n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
printf '**Workspace:** local operator checkout  \n\n'
printf '| Repository | Branch | Commit SHA | Tree | Remote |\n'
printf '| --- | --- | --- | --- | --- |\n'

has_dirty_tree=false
for repository in $repositories; do
    repository_path="$workspace_root/$repository"
    if [ ! -d "$repository_path/.git" ]; then
        printf '| `%s` | MISSING | MISSING | MISSING | MISSING |\n' "$repository"
        has_dirty_tree=true
        continue
    fi

    branch=$(git -C "$repository_path" branch --show-current)
    commit=$(git -C "$repository_path" rev-parse HEAD)
    remote=$(git -C "$repository_path" remote get-url origin 2>/dev/null || printf 'unavailable')
    if [ -n "$(git -C "$repository_path" status --porcelain=v1)" ]; then
        tree=MODIFIED
        has_dirty_tree=true
    else
        tree=CLEAN
    fi
    printf '| `%s` | `%s` | `%s` | %s | `%s` |\n' \
        "$repository" "$branch" "$commit" "$tree" "$remote"
done

printf '\n'
if [ "$has_dirty_tree" = true ]; then
    printf '**Baseline result:** INVALID — missing or modified repository detected.\n'
    exit 1
fi

printf '**Baseline result:** VALID — every listed repository is present and clean.\n'

