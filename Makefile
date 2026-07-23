# Codegen tasks for the General Liquidity Python SDK.
.PHONY: generate verify-codegen

generate:
	bash scripts/generate.sh

verify-codegen: generate
	git diff --exit-code -- src/general_liquidity docs test
