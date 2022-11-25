const formular = document.getElementById("registracni_formular");
const nick_label = document.getElementById("nick_label");
const nick = document.getElementById("nick");
const je_plavec_label = document.getElementById("je_plavec_label");
const je_plavec = document.getElementById("je_plavec");
const kanoe_kamarad_label = document.getElementById("kamarad_do_lode_label");
const kanoe_kamarad = document.getElementById("kamarad_do_lode");
const odeslat_button = document.getElementById("odeslat_button");

function over_registraci () {
    if (!nick.value) {
        window.alert("Nick nebyl vyplnen");
        return
    }

    const options = {
        method: "post",
        headers: {
            "Content-Type": "application/json"
        },
        body: {
            nick: nick.innerText,
            je_plavec: je_plavec.value,
            kanoe_kamarad: kanoe_kamarad.innerText
        }
    };

    fetch("/registrace", options);
}

