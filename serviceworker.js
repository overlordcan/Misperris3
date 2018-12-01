var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    'static/core/css/estilos.css',
    'static/core/img/Apolo.jpg',
    'static/core/img/Bigotes.jpg',
    'static/core/img/Chocolate.jpg',
    'static/core/img/correo.png',
    'static/core/img/crowfunding.jpg',
    'static/core/img/Duque.jpg',
    'static/core/img/facebook.png',
    'static/core/img/google.png',
    'static/core/img/icono-login.png',
    'static/core/img/img_perro.gif',
    'static/core/img/instagram.png',
    'static/core/img/logo.png',
    'static/core/img/Luna.jpg',
    'static/core/img/Oso.jpg',
    'static/core/img/perro.png',
    'static/core/img/Pexel.jpg',
    'static/core/img/rescate.jpg',
    'static/core/img/Tom.jpg',
    'static/core/img/Wifi.jpg',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'static/core/js/inicializacion.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/images/bx_loader.gif',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/images/controls.png'

];

self.addEventListener('install', function (event) {
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function (cache) {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function (event) {
    event.respondWith(
        caches.match(event.request).then(function (response) {
            if (response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyC52ltpfVKkjkfZLESLYfUEGeUDaUYW2Hw",
    authDomain: "mis-perris-d8868.firebaseapp.com",
    databaseURL: "https://mis-perris-d8868.firebaseio.com",
    projectId: "mis-perris-d8868",
    storageBucket: "mis-perris-d8868.appspot.com",
    messagingSenderId: "771089628780"
};

firebase.initializeApp(config);

var messaging = firebase.messaging();

//vamos a escuchcar cuando llegue una notificación desde el archivo de firebase

messaging.setBackgroundMessageHandler(function (playload) {

    var title = "titulo de la notificación"
    var options = {
        body: "cuerpo de la notificacion",
        icon: "/static/core/img/logo.png"
    }

    this.registration.showNotification(title, option)

})
