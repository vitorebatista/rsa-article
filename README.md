# RSA
O RSA é um algoritmo de criptografia assimétrica amplamente utilizado que permite garantir o estabelecimento de comunicações seguras em ambientes abertos como a internet. O objetivo desse artigo é descrever conceitualmente o funcionamento do algotirmo RSA e alguns pontos de seu embasamento matemático, a implementação realizada e sua complexidade, com o foco especial na análise de performance dos processos de geração e de quebra de chave. Dentro dos resultados atingidos é possível identificar que a segurança de sistemas de criptografia está baseada primordialmente na garantia de que a fatoração de grandes chaves demanda um tempo relativamente alto, mesmo para grande capacidade computacional. Nota-se também que a utilização de testes probabilísticos como os de Fermat e Miller-Rabin, assim como heurísticas como Pollard-Rho, permitem que se tenha ganho de performance, mas sem comprometer a segurança do sistema de criptografia.

O artigo completo no formato SBC está disponível [neste link](./article/RSA.pdf).

### Instalação
Necessário ter [Pipenv](https://github.com/pypa/pipenv#installation) e executar:
```shell
$ pipenv install 
```

### Utilização

Para gerar os arquivos de chave pública, privada e os gráficos:
```shell
$ pipenv shell
$ python main.py
```

Para realizar testes simples de criptografia de 512 bits:
```shell
$ pipenv shell
$ python test_simple.py
```

Para realizar a análise de primalidade com as funções `is_prime`, `is_prime_fermat` e `is_prime_miller`:
```shell
$ pipenv shell
$ python test_prime.py
``` 

### Integrantes do projeto:

* [Felipe Nathan Welter](https://github.com/felipenwelter)
* [Vitor Emanuel Batista](https://github.com/vitorebatista)