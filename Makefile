.PHONY: list push-all pull-all generate publish git-push push-section list-sections sync-sections

TRACKS := $(shell find tracks -mindepth 2 -maxdepth 2 -type d -name 'slb-*' | sort)
SECTIONS := foundations developers sre bi aiops reference

list:
	@echo "SLB Instruqt tracks (by section):"
	@for s in $(SECTIONS); do \
		echo "  $$s:"; \
		for t in tracks/$$s/slb-*; do [ -d "$$t" ] && echo "    $$t"; done; \
	done

list-sections:
	@python3 -c "import yaml; d=yaml.safe_load(open('catalog/sections.yaml')); \
	  [print(f\"{s['id']:12} {s['tag']:28} {s['instruqt_collection'] or '(none)'}\") for s in d['sections']]"

generate:
	python3 scripts/generate-tracks.py

sync-sections:
	python3 scripts/sync-section-tags.py

push-all: sync-sections
	@for t in $(TRACKS); do \
		echo "==> Pushing $$t"; \
		(cd "$$t" && instruqt track push) || exit 1; \
	done

push-section: sync-sections
	@test -n "$(SECTION)" || (echo "Usage: make push-section SECTION=aiops" && exit 1)
	@for t in tracks/$(SECTION)/slb-*; do \
		echo "==> Pushing $$t"; \
		(cd "$$t" && instruqt track push) || exit 1; \
	done

pull-all:
	@for t in $(TRACKS); do \
		echo "==> Pulling $$t"; \
		(cd "$$t" && instruqt track pull) || true; \
	done

git-push:
	@git diff --quiet && git diff --cached --quiet || { \
		echo "==> Committing changes"; \
		git add -A && git commit -m "$${MSG:-Update SLB workshop tracks}"; \
	}
	@echo "==> Pushing to origin"
	@git push origin HEAD

publish: git-push push-all
	@echo "Published to GitHub and Instruqt."
