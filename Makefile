PORT=8000

.PHONY: post
post:
	@curl --header "Content-Type: application/json" \
  		--request POST \
  		--data '{"name":"user", "email": "user@email.com", "password":"h4rdT0gu3sS"}' \
  		http://localhost:${PORT}/sign_up

.PHONY: server
server:
	@export API_PORT=${PORT}
	@python3 -m src.api

.PHONY: cli
cli:
	@python3 -m src.cli


.PHONY: shell
shell:
	@python3 -i shell.py