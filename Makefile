.PHONY: list push-all pull-all generate publish git-push

TRACKS := $(wildcard tracks/slb-*)

list:
	@echo "SLB Instruqt tracks:"
	@for t in $(TRACKS); do echo "  $$t"; done

generate:
	python3 scripts/generate-tracks.py

push-all:
	@for t in $(TRACKS); do \
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

# Default workflow after any track change: commit/push git, then publish all tracks to Instruqt.
publish: git-push push-all
	@echo "Published to GitHub and Instruqt."
