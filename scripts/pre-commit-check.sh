#!/bin/bash
# Pre-commit validation for marketing-playbook
# Ensures version consistency across plugin.json, marketplace.json, and CHANGELOG.md

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Running version consistency check...${NC}"

# Get versions from both files
PLUGIN_VERSION=$(jq -r '.version' .claude-plugin/plugin.json 2>/dev/null)
MARKETPLACE_VERSION=$(jq -r '.plugins[0].version' .claude-plugin/marketplace.json 2>/dev/null)

# Check if jq succeeded
if [ -z "$PLUGIN_VERSION" ] || [ "$PLUGIN_VERSION" == "null" ]; then
    echo -e "${RED}ERROR: Could not read version from .claude-plugin/plugin.json${NC}"
    exit 1
fi

if [ -z "$MARKETPLACE_VERSION" ] || [ "$MARKETPLACE_VERSION" == "null" ]; then
    echo -e "${RED}ERROR: Could not read version from .claude-plugin/marketplace.json${NC}"
    exit 1
fi

# Compare versions
if [ "$PLUGIN_VERSION" != "$MARKETPLACE_VERSION" ]; then
    echo -e "${RED}VERSION MISMATCH DETECTED!${NC}"
    echo ""
    echo -e "  plugin.json:      ${YELLOW}$PLUGIN_VERSION${NC}"
    echo -e "  marketplace.json: ${YELLOW}$MARKETPLACE_VERSION${NC}"
    echo ""
    echo -e "Fix by running:"
    echo -e "  ${GREEN}jq '.plugins[0].version = \"$PLUGIN_VERSION\"' .claude-plugin/marketplace.json > tmp.json && mv tmp.json .claude-plugin/marketplace.json${NC}"
    echo ""
    exit 1
fi

# Check if version exists in CHANGELOG.md
if ! grep -q "\[$PLUGIN_VERSION\]" CHANGELOG.md; then
    echo -e "${RED}VERSION NOT FOUND IN CHANGELOG!${NC}"
    echo ""
    echo -e "  Version ${YELLOW}$PLUGIN_VERSION${NC} is not documented in CHANGELOG.md"
    echo ""
    echo -e "Add a section like:"
    echo -e "  ${GREEN}## [$PLUGIN_VERSION] - $(date +%Y-%m-%d)${NC}"
    echo ""
    exit 1
fi

echo -e "${GREEN}Version check passed: v$PLUGIN_VERSION${NC}"
exit 0
