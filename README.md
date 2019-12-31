# API

## Como Executar?

### Instalação das Dependências

* Instale o [Docker-CE](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* Instale o [Docker-Compose](https://docs.docker.com/compose/install/)

### Para Execução:

Com as dependências instaladas execute, no terminal de seu ambiente, os comandos a seguir:

```

$ docker-compose -f docker-compose.yml build

```

O comando criará a imagem docker.

```

$ docker-compose up

```

O comando executará o sistema. Caso tudo ocorra normalmente, será possível acessar a interface da API em:

[https:\\\localhost:8000](https:\\localhost:8000)

## Exemplos de Requisição:

### Cadastro de uma nova classe de EBD:

```

$ curl -d '{"class_name":"Adultos"}' -H "Content-Type: application/json" -X POST http://localhost:8000/ebd-class/

```

### Listagem das classes de EBD:

```

$ curl -X GET http://localhost:8000/ebd-class/

```