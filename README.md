<h2> Back-end Challenge 🏅 2021 - Space Flight News - This is a challenge by <a href="https://coodesh.com">Coodesh</a> </h2>

<p> Este projeto é um desafio back-end, proposto pela Coodesh para testar as minhas habilidades em desenvolvimento.</br>
A proposta é criar uma api REST no qual possa realizar os dados do projeto <a href="https://api.spaceflightnewsapi.net/v3/documentation"> Space Flight News </a>, uma API pública com informações relacionadas a voos espaciais.</p>

https://www.loom.com/share/35bf2c018623472e956df1ee76e7dd22

<h3>Começando</h3>

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

<ul>
  <li>Python 3.10</li>
  <li>MySQL (hospedado na Heroku) </li>
  <li>pip 21.2.3 </li>  
  <li>Fastapi 0.70.1 </li>
  <li>SQLAlchemy 1.4.29 </li>
  <li>PyMySql 1.0.2 </li>
  <li>Pydantic </li>
  <li>virtualenv 20.13.0</li>
</ul>

<h3>Building</h3>

<ol>
  <li>
    <h4> Instale o python </h4>
  </li>
  <li>
    <h4>Baixando o projeto! </h4>
      <h5>No terminal execute</h5>
      <ul>  
        <li>cd "diretorio de sua preferencia"</li>
        <li>git clone https://github.com/DeversonBasilio/spaceflight_api</li>
      </ul>
  </li>
  <li>
    <h4>Criando Enviroment </h4>
      <h5>No terminal execute</h5>
      <ul>  
        <li>cd spaceflight_api</li>
        <li>pip install --user virtualenv</li>
        <li>python -m virtualenv venv</li>
        <li>src\venv\Scripts\activate</li>
      </ul>
  </li>
  <li>
    <h4>Instalando Pacotes </h4>
    <h5>No terminal execute</h5>
    <ul>
      <li>pip install -r src\requirements.txt</li>  
    </ul>    
  </li>
 
  <li>
      <h4>Testando</h4>
      <h5>No terminal execute</h5>
    <ul>
      <li>
        python -m uvicorn main:app --reload
      </li>
    </ul>
  </li>  
 </ol>
 
 <h3>Testando </h3>
 
 <h4>No terminal, dentro da pasta do projeto execute</h4>
  <ul>
    <li>
      python -m uvicorn main:app --reload
    </li>
  </ul>
  
   <h4>Em seu navegador, acesse o link para o localhost da api: <a href="http://127.0.0.1:8000"> http://127.0.0.1:8000 </a> </h4>
   <h4>Para acessar as rotas da api, utilize: <a href="http://127.0.0.1:8000/docs"> http://127.0.0.1:8000/docs </a> </h4>
