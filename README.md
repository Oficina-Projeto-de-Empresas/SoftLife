## Rotas 
---
### Produtos
```
/produto/  - Lista todos os produtos disponiveis para compra 

/produto/{id} - Mostrar informações do produto selecionado
```

### Usuarios
```
/usuario/{id}  - Apresenta dados do cliente que pode ser alterado

/usuario/{id}/carrinho/  - Mostra o carrinho do cliente 

/usuario/{id}/pedidos  - Lista todos pedidos realizados

/usuario/{id}/pedidos/{id_pedido}  - Informa detalhes do pedido
```

### Administrador
```
/Admin/home - N/A

/Admin/user - Apresenta número de usuarios e seus dados.

/Admin/produto  - Controle de estoque, com crud para adicionar, criar e excluir produtos 

/Admin/dashboard  - Apresentação grafica de dados como produtos vendidos e controle de estoque.
```

---

# Todo - Á fazer 

- Remodelar os models 
- fazer funcionar login  de usuarios
- finalizar a conf de admin **configurar para portugues** --Pendente
- criar as rotas de **produtos** e usuarios