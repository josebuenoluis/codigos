
// Función para generar una clave aleatoria de 128 bits
function generateKey() {
    const randomKey = CryptoJS.lib.WordArray.random(16).toString(CryptoJS.enc.Hex);
    document.getElementById('key').value = randomKey;
}

// Función para cifrar
function encrypt() {
    const key = document.getElementById('key').value;
    const plaintext = document.getElementById('plaintext').value;

    if (!key || !plaintext) {
	alert("Por favor, introduce una clave y un texto claro.");
	return;
    }

    // Cifrar el texto
    const encrypted = CryptoJS.AES.encrypt(plaintext, CryptoJS.enc.Hex.parse(key), {
	mode: CryptoJS.mode.ECB,
	padding: CryptoJS.pad.Pkcs7
    });

    // Mostrar texto cifrado en Base64 y Hexadecimal
    document.getElementById('ciphertext-base64').value = encrypted.toString();
    document.getElementById('ciphertext-hex').value = encrypted.ciphertext.toString(CryptoJS.enc.Hex);
}

// Función para descifrar
function decrypt() {
    const key = document.getElementById('key').value;
    const ciphertextBase64 = document.getElementById('ciphertext-base64').value;

    if (!key || !ciphertextBase64) {
	alert("Por favor, introduce una clave y un texto cifrado.");
	return;
    }

    try {
	// Descifrar el texto
	const decrypted = CryptoJS.AES.decrypt(ciphertextBase64, CryptoJS.enc.Hex.parse(key), {
	    mode: CryptoJS.mode.ECB,
	    padding: CryptoJS.pad.Pkcs7
	});

	document.getElementById('plaintext').value = decrypted.toString(CryptoJS.enc.Utf8);
    } catch (e) {
	alert("Error al descifrar. Verifica la clave y el texto cifrado.");
    }
}

// Función para convertir de Hex a Base64
function convertHexToBase64() {
    const hexText = document.getElementById('ciphertext-hex').value;
    if (!hexText) {
	alert("Por favor, introduce un texto en Hexadecimal.");
	return;
    }

    try {
	const wordArray = CryptoJS.enc.Hex.parse(hexText);
	const base64Text = CryptoJS.enc.Base64.stringify(wordArray);
	document.getElementById('ciphertext-base64').value = base64Text;
    } catch (e) {
	alert("Error al convertir Hex a Base64.");
    }
}

// Función para convertir de Base64 a Hex
function convertBase64ToHex() {
    const base64Text = document.getElementById('ciphertext-base64').value;
    if (!base64Text) {
	alert("Por favor, introduce un texto en Base64.");
	return;
    }

    try {
	const wordArray = CryptoJS.enc.Base64.parse(base64Text);
	const hexText = CryptoJS.enc.Hex.stringify(wordArray);
	document.getElementById('ciphertext-hex').value = hexText;
    } catch (e) {
	alert("Error al convertir Base64 a Hex.");
    }
}
function goToPage() {
            window.location.href = 'aes-128-cbc.html'; // Cambia por la URL de destino
        }
