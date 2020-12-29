.PHONY: build
build:
	docker build -t eay/practice-mate .


.PHONY: buildNoCache
buildNoCache:
	docker build --no-cache -t eay/practice-mate .


.PHONY: buildDev
buildDev: build
	docker build -f Dockerfile.dev --build-arg IMAGE=eay/practice-mate -t eay/practice-mate.dev .


.PHONY: run
run: build
	docker run -it \
		-t eay/practice-mate practice-mate


.PHONY: runUnitTests
runUnitTests: buildDev
	docker run -it -t eay/practice-mate.dev py.test -s .
