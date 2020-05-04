'use strict'

var express = require('express');
var ElementoController = require('../controllers/elemento');

var router = express.Router();

var multipart = require('connect-multiparty');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/elemento/:id?',ElementoController.getElemento);
router.get('/elemento/:especie?',ElementoController.getElementosPorEspecie);
router.get('/elementos',ElementoController.getElementos);

router.post('/elemento/:id?',ElementoController.crearElemento);
router.post('/elemento/:especie?',ElementoController.crearElementosPorEspecie);
router.post('/elementos',ElementoController.crearElementos);

module.exports = router;
