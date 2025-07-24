# Sistema de Reserva de Salas de Reunião

## Descrição

Este projeto implementa um sistema de reserva de salas de reunião com interface web interativa utilizando **Streamlit**.  
O backend usa **SQLite** para armazenar dados de salas, usuários e reservas. O código é estruturado com orientação a objetos para melhor organização e manutenção.

---

## Funcionalidades

- Cadastro de salas de reunião com nomes únicos  
- Cadastro de usuários com nome e email únicos  
- Realização de reservas de salas para datas e horários específicos  
- Verificação automática de conflitos para evitar sobreposição de reservas  
- Listagem e filtro de reservas por data  
- Cancelamento de reservas existentes  

---

## Tecnologias Utilizadas

- **Python**  
- **Streamlit**: para construção da interface web interativa  
- **SQLite3**: banco de dados leve para armazenamento local  
- **Orientação a Objetos**: organização do código em classes para melhor manutenção
  
##Conceitos e Aprendizados

Este projeto é um excelente exemplo prático para aplicar:

Lógica de Programação Avançada: validação de conflitos, tratamento de erros e organização modular

Manipulação de Banco de Dados SQLite: criação de tabelas, consultas, inserções e exclusões

Orientação a Objetos (OO): encapsulamento de entidades do sistema (salas, usuários, reservas)

Desenvolvimento Web com Streamlit: construção de interfaces reativas, layouts, formulários e interação com o usuário
