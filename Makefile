debug:
	docker compose up db --build -d
	python main.py

deploy:
	docker compose up --build -d
