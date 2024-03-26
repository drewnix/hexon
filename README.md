# Hexon 

Experimental data structures and algorithms space

## Commands

### Build and install
```bash
poetry run build; poetry run install
```

### Initialize database and load stored questions
```bash
poe initdb
```

### Run service / ui local
```bash
poe run
```

### Run storybook
```bash
cd src/ui; yarn storybook
```

### Build docker

```bash
docker build -t hexon .
```