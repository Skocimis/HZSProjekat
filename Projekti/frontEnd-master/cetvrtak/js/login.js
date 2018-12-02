/*
(function () {
    function toJSONString(form) {
        var objekatTim = {};
        var objekatClan = {};
        var nizClanova = [];

        var informOTimu = $(".opsteInformacije, :input");
        var clanoviTima = $(".clanTima, :input");

        for (var i = 0; i < informOTimu.length; ++i) {
            var element = informOTimu[i];
            var kljucTim = element.name;
            var vrednostTima = element.value;

            if (kljucTim == "imeTima" || kljucTim == "opisTima" || kljucTim == "slikaTima") {
                objekatTim[kljucTim] = vrednostTima;
            }

        }

        for (var y = 0; y < clanoviTima.length; ++y) {
            var clan = clanoviTima[y];
            var kljucClan = clan.name;
            var idClana = clan.id;
            var vrednostClan = clan.value;

            if (kljucClan == "ime1" || kljucClan == "prezime1") {
                objekatClan[kljucClan] = vrednostClan;
                nizClanova[0] = objekatClan;
            }

            if (kljucClan == "ime2" || kljucClan == "prezime2") {
                objekatClan[kljucClan] = vrednostClan;
                nizClanova[1] = objekatClan;
            }

            if (kljucClan == "ime3" || kljucClan == "prezime3") {
                objekatClan[kljucClan] = vrednostClan;
                nizClanova[2] = objekatClan;
            }

            objekatTim["clanovi"] = nizClanova;

        }

        return JSON.stringify(objekatTim);
    }

    document.addEventListener("DOMContentLoaded", function () {
        var form = document.getElementById("forma");
        var output = document.getElementById("output");
        form.addEventListener("submit", function (e) {
            e.preventDefault();
            var json = toJSONString(this);
            output.innerHTML = json;

            //ispisivanje json podataka u formu
            var noviObjekat = JSON.parse(json);

            var imeTimaLabel = document.createElement('label');
            var imeTimaInput = document.createElement('input');
            imeTimaInput.readOnly = true;

            imeTimaLabel.textContent = "Ime tima";
            imeTimaInput.value = noviObjekat.imeTima;

            var novaForma = document.getElementById("novaForma");
            novaForma.appendChild(imeTimaLabel);
            novaForma.appendChild(imeTimaInput);

        }, false);

    });

})();
*/
//window.localStorage.setItem('testTim', 'ae98b051-be1f-472a-af17-798bb28a11d6');



var form = document.getElementById("forma");
form.addEventListener("submit", function (e) {
    e.preventDefault();
    //var nazivPolje = $('#nazivTima').val();
    //console.log(nazivPolje);
    //var sifraPolje = window.localStorage.getItem(nazivPolje);

    var requestURL = "http://localhost:5000/teams/";

    var request = new XMLHttpRequest();
    var aa = document.getElementById('sifraTima');
    request.open('GET', requestURL + aa.value);
    request.responseType = 'json';
    request.send();

    request.onload = function () {
        var tim = request.response;
        console.log(tim);
        //samo prikaz u konzoli zbog demonstracije
        var div = document.getElementById('prikaz');
        var myH1 = document.createElement('input');
        var label = document.createElement('p');
        label.textContent = 'Ime tima';
        div.appendChild(label);

        myH1.value = tim['name'];
        div.appendChild(myH1);
        var myPar = document.createElement('input');
        myPar.value = tim['description'];
        var label2 = document.createElement('p');
        label2.textContent = 'Opis tima';
        div.appendChild(label2);
        div.appendChild(myPar);

        var clanovi = tim['team_members'];
        ispisiClanove(clanovi, div);

    }

}, false);

function ispisiClanove(clanovi, div) {

    for (var j = 0; j < clanovi.length; j++) {
        var myArticle = document.createElement('article');
        var ime = document.createElement('input');
        var prezime = document.createElement('input');
        var email = document.createElement('input');
        var brojTelefona = document.createElement('input');
        var skola = document.createElement('input');
        var mestoSkole = document.createElement('input');

        ime.value = clanovi[j].first_name;
        prezime.value = clanovi[j].last_name;
        email.value = clanovi[j].email;
        brojTelefona.value = clanovi[j].phone_number;
        skola.value = clanovi[j].school;
        mestoSkole.value = clanovi[j].city;

        myArticle.appendChild(ime);
        myArticle.appendChild(prezime);
        myArticle.appendChild(email);
        myArticle.appendChild(brojTelefona);
        myArticle.appendChild(skola);
        myArticle.appendChild(mestoSkole);

        myArticle.classList.add('clanoviTima');

        div.appendChild(myArticle);

    }
    var dugmence = document.createElement('input');
    dugmence.setAttribute('type', 'submit');

    div.appendChild(dugmence);
    var dugg = document.getElementById('dug2');
    dugg.style.visibility = 'visible';
}
function obrisiTim (uuidTima){
    var requestURL = "http://localhost:5000/teams/"+uuidTima;
    var request = new XMLHttpRequest();
    request.open('DELETE', requestURL);
    request.send();

}

/*
TESTIRANJE ZA BRISANJE
var requestURL = "http://142.93.173.116:5000/teams/";

var request = new XMLHttpRequest();

request.open('DELETE', requestURL + '0452b67e-8f12-4010-95c2-53481bb927a9');

request.send();
*/