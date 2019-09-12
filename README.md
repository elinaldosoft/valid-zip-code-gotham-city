### Creating Environment
`virtualenv venv -p $(which python3.6)`

### Enable Environment
`source venv/bin/activate`

### Install Packages
`pip install -r requirements/dev.txt`

### Running tests
`pytest`

O sistema dos correios de Gotham City tiveram um problema e perderam seu validador de CEPs.

- O CEP é um número maior que 100.000 e menor que 999999
- O CEP não pode conter nenhum nenhum dígito repetitivo alternado em pares

```
121426 # Aqui, 1 é um dígito repetitivo alternado em par.
523563 # Aqui nenhum digito é alternado.
552523 # Aqui os números 2 e 5 são dígitos alternados repetitivos em par.
```