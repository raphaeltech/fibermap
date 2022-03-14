<p align="center"> 
<h1 align="center">Fibermap</h1><br>
<h2 align="center">Sistema para documentação de redes de internet FTTH</h2>
</p>

<p>Me chamo Raphael Maia sou aluno do 4° periodo do curso de Analise e Desenvolvimento de Sistemas na universidade Candido Mendes - Campos dos Goytacazes - RJ. Para meu trabalho de conclusão de curso escolhi desenvolver o Software Fibermap.</p>
<p>Com intuito de sanar a dificuldade em obter sistemas voltado para a area de mapeamento e documentação de redes FTTH (Ópticas), senti a vontade de criar esse sistema para atender algumas areas na empresa em que hoje trabalho, trata-se de uma empresa do ramo de Telecomunicações, mais especificamente um provedor de internetl, temos hoje redes ópticas e UTP em 4 municipios no estado do Rio de Janeiro</p>

Esse sistema esta sendo desenvolvido em python, utilizando o framwork Django em sua versão 3.2.6 junto com outras bibliotecas listadas abaixo:

* dj-database-url==0.5.0
* Django==2.2.6
* django-bootstrap-form==3.4
* django-heroku==0.3.1
* djangorestframework==3.10.3
* mysqlclient==2.1.0
* psycopg2==2.9.3
* pytz==2019.3
* sqlparse==0.3.0
* whitenoise==6.0.0
* gunicorn==20.0.4

<p>Para banco de dados estou utilizando o Mysql-Server em sua versão 8.0.26.</p>

<h3 align="center">Principais caracteristicas e funcionalidades</h3>

<h4>Funcionalidades</h4>

* Cadastro de Usuários.
    <p>Consiste no cadastro de usuários do sistemas podendo esses serem técnicos, projetistas, engenheiros, vendedores e equipe de marketing.</p>
* Cadastramento de Ativos.
    <p>Consiste em um cadastro centralizado onde todos os equipamentos utilizado na rede estarão registrados de forma organizada, contento suas principais caractristicas.</p>
* Cadastro de Clientes.
    <p>Consiste no cadastros de todos os clientes ativos e inativos da empresa, e suas respectivas coordenadas geograficas, tornando assim mais facil a manutenção futura assim como controle de portas livres por caixas de atendimento. Esse cadastro podera ser feito de forma manual, ou automatizada atravéz de integração via API do Fibermap com o sistema ERP da empresa contratando do Fibermap.<p/>
* Cadastro de Fusões.
    <p>Essa é uma area primordial do sistema pois através dela que temos o controle e documentação da rede de fato, nessa área estará registradas todas as caixas de emendas da rede (CEO), contendo suas coordenadas geograficas, tipos de cabo, destino dos cabos e fusões em si, com isso conseguiremos mostrar em tela para o cliente uma visão explodida da caixa de emenda (CEO), e tornar cada vez mais fácil a manutenção em campo da rede.</p>
* Emissão de relatórios em diversos formatos.
    <p>Nessa área o cliente poderá emitir diversos relatórios que o ajudara nas tomadas de decisões na empresa. Como exemplo de alguns relatórios dou maior destaque a esses quatro que são eles:</p>
    
    * Numero de clientes inativos e ativos.
    * Numero de portas livres em toda a rede e por áreas especificas.
    * Valor total de todo o iventário ou seja toda a rede do provedor.
    * Area com maior potencial de venda. 

<h4>Caracteristicas</h4>
