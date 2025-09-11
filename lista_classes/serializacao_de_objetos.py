import json

class Usuario:
    def __init__(self, nome, email, id):
        self.nome = nome
        self.email = email
        self.id = id


    def to_dict(self):
        return {"nome": self.nome, "email": self.email, "id": self.id}
    
    @classmethod
    def from_dict(cls, dados_dict):
        cls.__init__(nome=dados_dict["nome"], email=dados_dict["email"], id=dados_dict["id"])
    

class GerenciadorUsuarios:    
    def __init__(self, lista_usuarios = []):
        self.lista_usuarios = lista_usuarios


    def salvar_em_json(self):
        with open('dados.json', 'w') as json_file:
                json.dump(self.lista_usuarios, json_file)

    
    def carregar_de_json(self, caminho_arquivo):
         with open(caminho_arquivo, 'r') as json_file:
              self.lista_usuarios = json.load(json_file)

g1 = GerenciadorUsuarios()
g1.carregar_de_json('dados.json')
print(g1.lista_usuarios) 