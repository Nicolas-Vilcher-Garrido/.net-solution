Descrição do Projeto


Este repositório contém uma solução em .NET para análise de dados de vendas utilizando Clean Architecture, DDD (Domain-Driven Design) e Entity Framework Core para gerenciamento de dados. A solução é composta por dois hosts: um WebAPI e um WorkerService, com a lógica de negócios separada em camadas para seguir boas práticas de arquitetura e facilitar a escalabilidade e manutenção.

Estrutura do Projeto
A solução foi estruturada da seguinte maneira:

WebAPI: Um projeto que fornece uma API RESTful para interagir com os dados.
WorkerService: Um serviço em segundo plano que processa tarefas em segundo plano, como o agendamento de jobs usando Hangfire.
Camadas DDD:
Domain: Contém as entidades e interfaces de repositórios.
Application: Implementa os casos de uso da aplicação e a lógica de negócios.
Infrastructure: Contém a implementação de acesso a dados com Entity Framework Core e repositórios.
Jobs: Contém os jobs do Hangfire, que são agendados e executados periodicamente.
Funcionalidades
Armazenamento de Dados: Utiliza o padrão Repository com Entity Framework Core para persistir os dados no banco de dados MSSQL.
Upsert de Dados: Implementação de upsert (inserção ou atualização de dados) utilizando o Hangfire para executar o job a cada hora.
Frontend: A solução também inclui um frontend em Vue.js (TypeScript) que exibe os dados em uma tabela filtrável.
Jobs Agendados: Utiliza o Hangfire para agendar tarefas de forma eficiente e processar dados automaticamente.
Principais Tecnologias
.NET Core (C#): Framework principal para o desenvolvimento da aplicação.
Entity Framework Core: ORM utilizado para o gerenciamento da persistência de dados.
Hangfire: Framework para agendamento de tarefas em segundo plano.
Vue.js (TypeScript): Framework para o desenvolvimento do frontend.
MSSQL: Banco de dados relacional utilizado para armazenar os dados.
