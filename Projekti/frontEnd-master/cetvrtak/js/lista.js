
var div = document.getElementById('listaTimova');

var requestURL = "http://localhost:5000/teams/";

var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function () {
    var timovi = request.response;
    ispisiOpsteInformacije(timovi);
}

function ispisiOpsteInformacije(jsonObj) {
    for (var i = 0; i < jsonObj.length; i++) {
        var elementNiza = jsonObj[i];

        var myDiv = document.createElement('div');
        var myH1 = document.createElement('h1');
        myH1.textContent = elementNiza['name'];
        div.appendChild(myH1);

        var myPar = document.createElement('p');
        myPar.textContent = 'Opis tima: ' + elementNiza['description'];
        div.appendChild(myPar);

        var clanovi = elementNiza['team_members'];
        ispisiClanove(clanovi, myDiv);
        
        div.appendChild(document.createElement('br'));
    }
    myDiv.appendChild(document.createElement('br'));

}

function ispisiClanove(clanovi, myDiv) {

    for (var j = 0; j < clanovi.length; j++) {
        var myArticle = document.createElement('article');
        var ime = document.createElement('h2');
        var prezime = document.createElement('h2');
        var email = document.createElement('p');
        var brojTelefona = document.createElement('p');
        var skola = document.createElement('p');
        var mestoSkole = document.createElement('p');

        ime.textContent = 'Ime: ' + clanovi[j].first_name;
        prezime.textContent = 'Prezime: ' + clanovi[j].last_name;
        email.textContent = "Email: " + clanovi[j].email;
        brojTelefona.textContent = 'Broj telefona: ' + clanovi[j].phone_number;
        skola.textContent = 'Skola: ' + clanovi[j].school;
        mestoSkole.textContent = 'Mesto skole: ' + clanovi[j].city;

        myArticle.appendChild(ime);
        myArticle.appendChild(prezime);
        myArticle.appendChild(email);
        myArticle.appendChild(brojTelefona);
        myArticle.appendChild(skola);
        myArticle.appendChild(mestoSkole);

        myArticle.classList.add('clanoviTima');

        myDiv.appendChild(myArticle);
    

    }

    div.appendChild(myDiv);
    div.classList.add('container');
}

