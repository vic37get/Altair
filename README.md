# Altair

### Criando venv caso já não tenha
```
sudo apt install python3.8-venv
python3 -m venv altair_venv
```
### Ativando venv
```
source altair_venv/bin/activate
```

### Instalando depêndencias
```
pip install -r requirements.txt
```

### Depois para iniciar o servidor Django utilize o comando abaixo
```
python3 manage.py runserver
```

## Passo a Passo para o uso do protótipo :walking:
O sistema Altair conta com dois tipos de usuários do sistema, o Gestor (Usuário que tem o poder de criar uma licitação e submetê-la) e o Auditor (usuário que tem o poder de verificar indícios e avaliar licitações enviadas pelo usupario gestor.).

### Criação de usuário 	:adult:
Para iniciar o uso do protótipo é necessário que se crie um usuário, a criação é bem simples, é necessário que se passe: nome, nome de usuário, email, cargo (podendo ser Auditor ou Gestor) e senha.

Após a criação do usuário é requerida a realização de login.

### Usuário Gestor :man_health_worker:

Ao entrar na aplicação é visível as licitações que já foram criadas por este usuário, também é possível criar uma nova licitação.
Para isso basta acionar o comando "Nova Licitação".

#### Modelos :gear:
É requerido que se escolha um modelo de licitação, sendo ele: CAPITULO, SEÇÕES ou NUMÉRICO. Isso serve para informar o tipo de padrão de seções desejado, por exemplo, ao escolher o padrão CAPITULO as seções serão criadas da seguinte forma:
* CAPITULO I - DO OBJETO
* CAPITULO II - DAS CONDIÇÕES DE PARTICIPAÇÃO

Já escolhendo o padrão NUMÉRICO as seções serão criadas da seguinte forma:
1. DO OBJETO
2. DAS CONDIÇÕES DE PARTICIPAÇÃO

Após escolher o padrão de documento é chegada a hora de construir a licitação. O menu lateral esquerdo é bastante útil para isso, possibilitando que se possa adicionar seções, salvar o documento no banco de dados, enviar o documento e baixar o documento.

#### Submetendo o documento :inbox_tray:
Clicando no menu esquerdo em enviar, é possível submeter o documento para que o mesmo seja avaliado por um Auditor. Ao clicar no botão enviar, é requerido o preenchimento de um formulário que requer algumas informações sobre aquela licitação.

Após o envio do documento, na página inicial, o status daquela licitação é alterado para Submetida.

#### Enviando um documento externo :envelope_with_arrow:
É possível realizar o envio de um documento externo a partir do botão Modulos -> Enviar Licitação no menu principal. Com isso é requerido o preenchimento de um formulário que pede informações sobre a licitação e ao seu final é solicitado o documento em si. O sistema faz verificações para autorizar ou não o envio do documento com base no padrão de documento solicitado pela aplicação, que requer um documento com todas as seções preenchidas, e com seções obrigatórias como a seção "DO OBJETO" por exemplo, além de verificações de tipo de arquivo e estrutura.
Após o envio o status dessa licitação é alterado para Submetida.

#### Visualizando e alterando informações de usuário :information_source:
É possível visualizar e alterar informações do usuário a partir do menu principal no botão lateral de ícone de usuário. Clicando nele é possível clicar no botão perfil, onde se pode visualizar e alterar informações de usuário.

### Usuário Auditor :man_office_worker:
Ao entrar na aplicação é visível as licitações que estão destinadas para este usuário avaliar.
Para isso basta acionar o comando "Abrir" em qualquer licitação.

#### Avaliar :heavy_check_mark:
Ao abrir a página de avaliação, é possível ver o documento PDF no canto esquerdo da tela, bem como, as informações da licitação no quadro principal. É possível verificar os indícios de fraude a partir do botão "Verificar indícios".

O "tamanho do contexto" serve para setar o tamanho da saída desejada do verificador de indícios.

É possível avaliar a licitação acionando o comando "Avaliar", então é solicitado do Auditor se existe indícios de fraude na licitação e os comentários que o Auditor pode fazer para o Gestor acerca da licitação.
Após isso, o feedback é enviado para o Gestor e essa licitação tem status "Avaliada" com feedback provido do Auditor disponível para que o Gestor possa ler.

#### Visualizando e alterando informações de usuário :information_source:
É possível visualizar e alterar informações do usuário a partir do menu principal no botão lateral de ícone de usuário. Clicando nele é possível clicar no botão perfil, onde se pode visualizar e alterar informações de usuário.
