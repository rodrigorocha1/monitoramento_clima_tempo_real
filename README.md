# Projeto: Sistema de Emissão de Alertas em Tempo Real da Região de Ribeirão Preto

## 1. Objetivo

O projeto propõe uma arquitetura em tempo real para a região de Ribeirão Preto, utilizando uma API e exibindo os dados em um dashboard. 

**Apache Kafka** é uma plataforma open-source de processamento de streams desenvolvida pela Apache Software Foundation, escrita em Scala e Java. O objetivo do projeto é fornecer uma plataforma unificada, de alta capacidade e baixa latência para tratamento de dados em tempo real.

## 2. Escopo

- Coleta dos dados da região de Ribeirão Preto.
- Geração de alertas em tempo real de acordo com as regras climáticas.
- Visualização de dados em um dashboard.

## 3. Requisitos Funcionais e Não Funcionais

### Requisitos Funcionais
- A aplicação deve coletar dados climáticos da API em intervalos de 10 minutos.
- O sistema deve emitir alertas quando forem detectadas condições de risco.
- Suporte a múltiplas cidades.
- Armazenamento de dados para análises futuras.

### Requisitos Não Funcionais
- O dashboard deve ser atualizado a cada 6 minutos.
- O sistema deve ser implementado em Linux.
- Uso do Apache Kafka para a coleta dos dados.

## 4. Funcionalidades

- Coleta de dados meteorológicos.
- Processamento de dados e aplicação de regras de negócio.

## 5. Diagrama de Classe

![Diagrama do Pipeline](https://static.wixstatic.com/media/123393_e7f05bbd1d7a48d59859d01150117f43~mv2.png)
> Diagrama de classe para aplicação em tempo real
## 6 – Demonstração
[Link para a Demonstração](https://www.youtube.com/watch?v=SdjyYmXV8i8)


