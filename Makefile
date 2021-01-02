user_id:=$(shell echo `id -u $(USER)`)
user_group:=$(shell echo `id -g $(USER)`)

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
    --user=${user_id}:${user_group} \
    --env="DISPLAY" \
    --volume="/etc/group:/etc/group:ro" \
    --volume="/etc/passwd:/etc/passwd:ro" \
    --volume="/etc/shadow:/etc/shadow:ro" \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    -t eay/practice-mate practice-mate


.PHONY: devInstall
devInstall:
	pip3 install -e .


.PHONY: runUnitTests
runUnitTests: devInstall
	coverage run --rcfile=./rcfile -m pytest -s ./test/ && coverage report


.PHONY: runUnitTestsDocker
runUnitTestsDocker: buildDev
	docker run -it -t eay/practice-mate.dev coverage run --rcfile=./rcfile -m pytest -s ./test/ && coverage report
