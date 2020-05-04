'use strict'

var express = require('express');
var EspecieController = require('../controllers/especie');

var router = express.Router();

var multipart = require('connect-multiparty');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/especie/:id?',EspecieController.getEsepcie);
router.get('/especie',EspecieController.getEspecies);

router.post('/especie/:id?',EspecieController.crearEspecie);
router.post('/especie',EspecieController.crearEspecies);

module.exports = router;
